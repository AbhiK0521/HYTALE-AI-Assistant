"""API routes for documents"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/documents", tags=["documents"])

@router.get("/")
async def list_documents():
    """List all uploaded documents"""
    return {"documents": []}

@router.post("/upload")
async def upload_document():
    """Upload a new PDF document"""
    return {"status": "pending", "message": "Document upload endpoint"}
