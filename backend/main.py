"""
HYTALE AI - AI-Powered Study Assistant
Main FastAPI application server
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 HYTALE AI Server Starting...")
    yield
    # Shutdown
    print("🛑 HYTALE AI Server Shutting Down...")

# Initialize FastAPI app
app = FastAPI(
    title="HYTALE AI",
    description="AI-Powered Study Assistant with RAG",
    version="0.1.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "HYTALE AI Study Assistant",
        "version": "0.1.0"
    }

@app.get("/api/health")
async def health():
    """API health check"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
