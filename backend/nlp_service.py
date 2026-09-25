import json
import re
from pathlib import Path

import joblib


# ============================================================
# MODEL PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent / "model"

MODEL_PATH = MODEL_DIR / "sentiment_model.joblib"
VECTORIZER_PATH = MODEL_DIR / "tfidf_vectorizer.joblib"


# ============================================================
# LOAD MODEL
# ============================================================

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Sentiment model not found: {MODEL_PATH}"
    )

if not VECTORIZER_PATH.exists():
    raise FileNotFoundError(
        f"TF-IDF vectorizer not found: {VECTORIZER_PATH}"
    )

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# ============================================================
# CONTRACTIONS
# ============================================================

CONTRACTIONS = {
    "can't": "can not",
    "cannot": "can not",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "isn't": "is not",
    "it's": "it is",
    "mightn't": "might not",
    "mustn't": "must not",
    "needn't": "need not",
    "shouldn't": "should not",
    "wasn't": "was not",
    "weren't": "were not",
    "won't": "will not",
    "wouldn't": "would not",
    "i'm": "i am",
    "you're": "you are",
    "we're": "we are",
    "they're": "they are",
    "i've": "i have",
    "we've": "we have",
    "they've": "they have",
    "i'd": "i would",
    "you'd": "you would",
    "we'd": "we would",
    "they'd": "they would",
}


# ============================================================
# TEXT PREPROCESSING
# ============================================================

def preprocess_text(text: str) -> str:

    text = str(text).lower()

    for contraction, replacement in sorted(
        CONTRACTIONS.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        text = re.sub(
            rf"\b{re.escape(contraction)}\b",
            replacement,
            text
        )

    # Remove URLs
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    # Remove HTML
    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Keep letters, numbers and spaces
    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# ============================================================
# SENTIMENT PREDICTION
# ============================================================

def predict_sentence(text: str):

    processed_text = preprocess_text(text)

    features = vectorizer.transform(
        [processed_text]
    )

    prediction = model.predict(
        features
    )[0]

    probabilities = model.predict_proba(
        features
    )[0]

    classes = model.classes_

    probability_map = {
        str(label): round(
            float(probability),
            4
        )
        for label, probability in zip(
            classes,
            probabilities
        )
    }

    confidence = float(
        max(probabilities)
    )

    return (
        str(prediction),
        confidence,
        probability_map
    )


# ============================================================
# ASPECT KEYWORDS
# ============================================================

ASPECT_KEYWORDS = {

    "Food": [
        "food",
        "dish",
        "meal",
        "taste",
        "flavor",
        "flavour",
        "delicious",
        "menu",
        "cuisine"
    ],

    "Service": [
        "service",
        "waiter",
        "waitress",
        "staff",
        "server",
        "customer service"
    ],

    "Price": [
        "price",
        "prices",
        "cost",
        "expensive",
        "cheap",
        "value",
        "money",
        "affordable"
    ],

    "Ambience": [
        "ambience",
        "ambiance",
        "atmosphere",
        "decor",
        "interior",
        "music",
        "environment"
    ],

    "Location": [
        "location",
        "area",
        "parking",
        "place",
        "neighborhood",
        "neighbourhood"
    ],

    "Cleanliness": [
        "clean",
        "dirty",
        "cleanliness",
        "bathroom",
        "restroom"
    ],

    "Waiting Time": [
        "wait",
        "waiting",
        "slow",
        "quick",
        "fast",
        "minutes",
        "minute",
        "long time",
        "delay",
        "delayed"
    ]
}


ASPECT_KEYWORDS_SORTED = {
    aspect: sorted(
        keywords,
        key=len,
        reverse=True
    )
    for aspect, keywords in ASPECT_KEYWORDS.items()
}


# ============================================================
# SENTENCE SPLITTING
# ============================================================

def split_sentences(text: str):

    text = str(text).strip()

    if not text:
        return []

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


# ============================================================
# FIND ASPECT KEYWORD
# ============================================================

def find_keyword_positions(
    sentence: str,
    keywords
):

    positions = []

    for keyword in keywords:

        pattern = (
            rf"(?<!\w)"
            rf"{re.escape(keyword)}"
            rf"(?!\w)"
        )

        for match in re.finditer(
            pattern,
            sentence,
            flags=re.IGNORECASE
        ):

            positions.append(
                (
                    match.start(),
                    match.end(),
                    keyword
                )
            )

    return positions


# ============================================================
# CLAUSE SPLITTING
# ============================================================

def split_into_clauses(sentence: str):

    parts = re.split(
        r"\s+"
        r"(?:but|however|although|though|while|whereas|yet)"
        r"\s+",
        sentence,
        flags=re.IGNORECASE
    )

    return [
        part.strip(" ,;:")
        for part in parts
        if part.strip(" ,;:")
    ]


# ============================================================
# EXTRACT ASPECT CONTEXT
# ============================================================

def extract_aspect_context(
    sentence: str,
    keyword_start: int,
    keyword_end: int
):

    clauses = split_into_clauses(
        sentence
    )

    current_position = 0

    selected_clause = sentence

    for clause in clauses:

        start = sentence.lower().find(
            clause.lower(),
            current_position
        )

        if start == -1:
            continue

        end = start + len(clause)

        if start <= keyword_start < end:

            selected_clause = clause

            break

        current_position = end

    # Short clause: use the whole clause
    words = selected_clause.split()

    if len(words) <= 18:
        return selected_clause

    # Long clause: use local context
    keyword_text = sentence[
        keyword_start:keyword_end
    ]

    local_match = re.search(
        rf"(?<!\w)"
        rf"{re.escape(keyword_text)}"
        rf"(?!\w)",
        selected_clause,
        flags=re.IGNORECASE
    )

    if local_match is None:
        return selected_clause

    prefix = selected_clause[
        :local_match.start()
    ].split()

    suffix = selected_clause[
        local_match.end():
    ].split()

    window_before = 7
    window_after = 7

    context_words = (
        prefix[-window_before:]
        +
        [keyword_text]
        +
        suffix[:window_after]
    )

    return " ".join(
        context_words
    )


# ============================================================
# ASPECT SENTIMENT ANALYSIS
# ============================================================

def analyze_aspects(text: str):

    results = []

    sentences = split_sentences(
        text
    )

    for sentence in sentences:

        sentence_matches = {}

        for aspect, keywords in (
            ASPECT_KEYWORDS_SORTED.items()
        ):

            positions = find_keyword_positions(
                sentence,
                keywords
            )

            if positions:

                positions.sort(
                    key=lambda item: (
                        -(item[2].count(" ") + 1),
                        item[0]
                    )
                )

                sentence_matches[
                    aspect
                ] = positions[0]

        for aspect, (
            start,
            end,
            keyword
        ) in sentence_matches.items():

            context = extract_aspect_context(
                sentence,
                start,
                end
            )

            sentiment, confidence, probabilities = (
                predict_sentence(context)
            )

            results.append(
                {
                    "aspect": aspect,
                    "sentiment": sentiment,
                    "confidence": round(
                        confidence,
                        4
                    ),
                    "keyword": keyword,
                    "context": context,
                    "probabilities": probabilities
                }
            )

    return results


# ============================================================
# COMPLETE REVIEW ANALYSIS
# ============================================================

def analyze_review(text: str):

    # Overall sentiment
    sentiment, confidence, probabilities = (
        predict_sentence(text)
    )

    # Aspect-level sentiment
    aspects = analyze_aspects(text)

    # Convert aspect list to JSON string
    aspects_json = json.dumps(
        aspects
    )

    return {
        "text": text,

        "sentiment": sentiment,

        "confidence": round(
            confidence,
            4
        ),

        "probabilities": probabilities,

        "aspects": aspects,

        # IMPORTANT:
        # main.py expects this key.
        "aspects_json": aspects_json
    }