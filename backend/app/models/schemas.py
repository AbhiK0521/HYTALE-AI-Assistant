"""Pydantic models for API requests/responses"""
from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    """Request model for PDF query"""
    query: str
    top_k: int = 3

class QueryResponse(BaseModel):
    """Response model for query"""
    answer: str
    sources: List[dict]
    confidence: float

class PDFUploadResponse(BaseModel):
    """Response model for PDF upload"""
    filename: str
    pages: int
    status: str
    message: str
