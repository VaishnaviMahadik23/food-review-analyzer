from typing import Optional
from pydantic import BaseModel, Field


class ReviewRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Food review text")


class ReviewResponse(BaseModel):
    id: Optional[int] = None
    text: str
    sentiment: str
    confidence: float
    aspects: str = "[]"
    created_at: Optional[str] = None


class AnalyticsResponse(BaseModel):
    total_reviews: int
    positive: int
    negative: int
    neutral: int
