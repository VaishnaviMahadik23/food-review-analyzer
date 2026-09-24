import json
import os
import re

import joblib
from nltk.tokenize import sent_tokenize

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "sentiment_model.joblib")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.joblib")

ASPECT_KEYWORDS = {
    "Food": ["food", "dish", "meal", "taste", "flavor", "delicious", "menu", "cuisine"],
    "Service": ["service", "waiter", "waitress", "staff", "server", "customer service"],
    "Price": ["price", "prices", "cost", "expensive", "cheap", "value", "money", "affordable"],
    "Ambience": ["ambience", "ambiance", "atmosphere", "decor", "interior", "music", "environment"],
    "Location": ["location", "area", "parking", "place", "neighborhood"],
    "Cleanliness": ["clean", "dirty", "cleanliness", "bathroom", "restroom"],
    "Waiting Time": ["wait", "waiting", "slow", "quick", "fast", "minutes", "long time"],
}

CONTRACTIONS = {
    "don't": "do not", "doesn't": "does not", "didn't": "did not",
    "isn't": "is not", "wasn't": "was not", "weren't": "were not",
    "can't": "can not", "couldn't": "could not", "wouldn't": "would not",
    "shouldn't": "should not", "won't": "will not",
}

_model = None
_vectorizer = None


def load_models():
    global _model, _vectorizer
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(MODEL_PATH)
    if not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(VECTORIZER_PATH)
    _model = joblib.load(MODEL_PATH)
    _vectorizer = joblib.load(VECTORIZER_PATH)


def preprocess_text(text):
    text = text.lower()
    for contraction, replacement in CONTRACTIONS.items():
        text = text.replace(contraction, replacement)
    text = re.sub(r"http\\S+|www\\S+|https\\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z0-9\\s]", " ", text)
    return re.sub(r"\\s+", " ", text).strip()


def predict_sentence(sentence):
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        load_models()

    processed = preprocess_text(sentence)
    vector = _vectorizer.transform([processed])
    prediction = _model.predict(vector)[0]
    probabilities = _model.predict_proba(vector)[0]
    confidence = float(probabilities.max())
    probability_map = {
        str(label): round(float(probability), 4)
        for label, probability in zip(_model.classes_, probabilities)
    }
    return str(prediction), confidence, probability_map


def analyze_aspects(review):
    try:
        sentences = sent_tokenize(review)
    except LookupError:
        sentences = re.split(r"(?<=[.!?])\\s+", review.strip())

    results = []
    for aspect, keywords in ASPECT_KEYWORDS.items():
        matched = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(re.search(r"\\b" + re.escape(keyword) + r"\\b", sentence_lower) for keyword in keywords):
                matched.append(sentence)

        if not matched:
            continue

        predictions = []
        for sentence in matched:
            sentiment, confidence, _ = predict_sentence(sentence)
            predictions.append({
                "sentiment": sentiment,
                "confidence": confidence,
                "evidence": sentence,
            })

        selected = max(predictions, key=lambda item: item["confidence"])
        results.append({
            "aspect": aspect,
            "sentiment": selected["sentiment"],
            "confidence": round(selected["confidence"], 4),
            "evidence": selected["evidence"],
        })
    return results


def analyze_review(review):
    sentiment, confidence, probabilities = predict_sentence(review)
    aspects = analyze_aspects(review)
    return {
        "sentiment": sentiment,
        "confidence": round(confidence, 4),
        "probabilities": probabilities,
        "aspects": aspects,
        "aspects_json": json.dumps(aspects),
    }
