"""API routes for queries"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/query", tags=["query"])

@router.post("/")
async def query_documents(query: str):
    """Query documents with RAG"""
    return {"answer": "Query processing will be implemented", "sources": []}
