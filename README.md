# HYTALE AI - AI-Powered Study Assistant

An intelligent study companion that uses RAG (Retrieval-Augmented Generation) to help students learn from PDFs, textbooks, and lecture notes.

## Project Structure

```
HYTALE AI/
├── backend/              # FastAPI Python backend
│   ├── app/
│   │   ├── models/      # Pydantic schemas
│   │   ├── routes/      # API endpoints
│   │   ├── services/    # Business logic
│   │   └── config.py    # Configuration
│   ├── main.py          # FastAPI app entry point
│   ├── requirements.txt  # Python dependencies
│   └── .env.example     # Environment variables template
├── frontend/            # React frontend
│   ├── src/
│   ├── index.html       # HTML entry point
│   ├── package.json     # Node dependencies
│   └── vite.config.js   # Vite configuration
└── docs/               # Documentation
```

## Features (In Development)

- 📄 PDF Upload & Processing
- 🔍 Semantic Search with FAISS
- 🤖 RAG-powered Answers
- 💬 Interactive Chat Interface
- 📊 Document Management
- 🎯 Study Progress Tracking

## Tech Stack

- **Backend**: Python, FastAPI, LangChain
- **Frontend**: React, Vite, Axios
- **Vector DB**: FAISS
- **LLM**: OpenAI GPT
- **Embeddings**: OpenAI Text Embeddings

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- OpenAI API key

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your OPENAI_API_KEY to .env
python main.py
```

Server runs on `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:3000`

## Development Roadmap

### Phase 1: Core Infrastructure ✅
- [x] Project setup
- [x] Backend scaffolding
- [x] Frontend scaffolding

### Phase 2: PDF Processing & Embeddings 🔄
- [ ] PDF parsing & text extraction
- [ ] Chunking strategy
- [ ] Embedding generation
- [ ] FAISS vector store

### Phase 3: RAG Implementation
- [ ] Document retrieval
- [ ] LLM integration
- [ ] Query processing
- [ ] Answer generation

### Phase 4: Frontend Development
- [ ] Document upload UI
- [ ] Query interface
- [ ] Results display
- [ ] Document management

### Phase 5: Polish & Optimization
- [ ] Performance optimization
- [ ] Error handling
- [ ] Testing
- [ ] Deployment

## API Endpoints (Planned)

- `GET /api/health` - Health check
- `POST /api/documents/upload` - Upload PDF
- `GET /api/documents` - List documents
- `POST /api/query` - Query documents
- `GET /api/query/history` - Query history

## Contributing

Development uses continuous git commits for progress tracking. Each feature phase generates meaningful commits.

## License

MIT

## Progress

Track progress across commits to see the feature development journey.
