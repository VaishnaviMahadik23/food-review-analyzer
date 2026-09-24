from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.database import create_tables, save_review, get_reviews, get_analytics
from backend.schemas import ReviewRequest, ReviewResponse, AnalyticsResponse
from backend.nlp_service import analyze_review

app = FastAPI(
    title="Food Review Analyzer API",
    description="NLP-based food review sentiment and aspect analysis API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    create_tables()


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Food Review Analyzer API"}


@app.post("/analyze-review", response_model=ReviewResponse)
def analyze_review_endpoint(request: ReviewRequest):
    review_text = request.text.strip()

    if not review_text:
        raise HTTPException(status_code=400, detail="Review text cannot be empty.")

    try:
        result = analyze_review(review_text)
        review_id = save_review(review_text, result)
        return {
            "id": review_id,
            "text": review_text,
            "sentiment": result["sentiment"],
            "confidence": result["confidence"],
            "aspects": result["aspects_json"],
        }
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail=(
                "NLP model files not found. Complete Phase 6 first so that "
                "model/sentiment_model.joblib and model/tfidf_vectorizer.joblib exist."
            ),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Review analysis failed: {exc}")


@app.get("/reviews", response_model=list[ReviewResponse])
def reviews_endpoint():
    return get_reviews()


@app.get("/analytics", response_model=AnalyticsResponse)
def analytics_endpoint():
    return get_analytics()