"""App configuration"""
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """Application settings"""
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    faiss_db_path: str = os.getenv("FAISS_DB_PATH", "./data/faiss_db")
    pdf_upload_path: str = os.getenv("PDF_UPLOAD_PATH", "./data/uploads")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    max_upload_size: int = 50 * 1024 * 1024  # 50 MB
    
    class Config:
        env_file = ".env"

settings = Settings()
