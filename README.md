# Government RAG Assistant

An AI-powered chatbot system for Indian government schemes information using Retrieval-Augmented Generation (RAG) technology. This project combines web crawling, document processing, vector embeddings, and large language models to provide accurate, contextual answers about government programs and benefits.

## 🚀 Features

- **Intelligent Q&A**: Ask questions about Indian government schemes and get accurate, contextual answers
- **Real-time Streaming**: Live response streaming for better user experience
- **Source Citations**: Every answer includes links to official government sources
- **Web Crawling**: Automated data collection from government websites
- **Vector Search**: Efficient document retrieval using embeddings
- **Modern UI**: Clean, responsive chat interface built with Next.js
- **Local LLM**: Uses Ollama for privacy-focused, local AI inference

## 🏗️ Architecture

This project consists of two main components:

### Backend (`rag-gov-assistant/`)
- **FastAPI**: High-performance async web framework
- **LangChain**: RAG pipeline orchestration
- **ChromaDB**: Vector database for document storage
- **Ollama**: Local LLM inference (Llama3)
- **BeautifulSoup**: Web scraping and content extraction

### Frontend (`frontend/rag-govt/`)
- **Next.js 16**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Modern styling framework
- **React Markdown**: Rich text rendering
- **Streaming UI**: Real-time response display

## 📋 Prerequisites

Before running this project, ensure you have:

- **Python 3.11+** for the backend
- **Node.js 18+** for the frontend
- **Ollama** installed and running locally
- **Git** for cloning the repository

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd govt-rag-chatbot
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd rag-gov-assistant

# Install Python dependencies
pip install fastapi uvicorn langchain-ollama langchain-chroma beautifulsoup4 requests

# Install and setup Ollama
# Download from: https://ollama.ai
ollama pull llama3
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend/rag-govt

# Install Node.js dependencies
npm install
```

## 🚀 Running the Application

### 1. Data Ingestion (One-time setup)

```bash
# From the backend directory
cd rag-gov-assistant
python -m scripts.crawl_ingest
```

This will crawl government websites, process the data, and create the vector database.

### 2. Start the Backend API

```bash
# From the backend directory
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Start the Frontend

```bash
# From the frontend directory
cd frontend/rag-govt
npm run dev
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs (FastAPI automatic docs)

## 💡 Usage Examples

The chatbot can answer questions like:

- "What are the schemes available for women entrepreneurs?"
- "Tell me about farmer subsidy programs"
- "What are the eligibility criteria for education scholarships?"
- "How can startups get government funding?"
- "What benefits do senior citizens get?"

## 📁 Project Structure

```
govt-rag-chatbot/
├── rag-gov-assistant/          # Backend (FastAPI)
│   ├── app/
│   │   ├── api/routes.py       # API endpoints
│   │   ├── ingestion/          # Data processing
│   │   ├── rag/               # RAG pipeline
│   │   ├── vectorstore/        # Vector database
│   │   └── main.py            # FastAPI app
│   ├── scripts/               # Utility scripts
│   ├── vectorstore_db/        # ChromaDB storage
│   └── README.md              # Backend documentation
├── frontend/
│   └── rag-govt/              # Frontend (Next.js)
│       ├── app/               # Next.js app router
│       ├── public/            # Static assets
│       ├── package.json       # Dependencies
│       └── README.md          # Frontend documentation
└── README.md                  # This file
```

## 🔧 Configuration

### Backend Configuration

- **LLM Model**: Configured for Llama3 via Ollama
- **Vector Database**: Local ChromaDB with persistence
- **Crawling**: Tamil Nadu government schemes (configurable)
- **API Port**: 8000 (configurable)

### Frontend Configuration

- **API Endpoint**: http://127.0.0.1:8000/chat
- **Streaming**: NDJSON format for real-time responses
- **Styling**: Tailwind CSS with custom design system

## 🧪 Testing

### Backend Tests

```bash
cd rag-gov-assistant
python -m scripts.test_scrapper
python -m scripts.test_ingest
python -m scripts.test_llm
python -m scripts.test_query
```

### Frontend Development

```bash
cd frontend/rag-govt
npm run lint
npm run build
```

## 🚀 Deployment

### Backend Deployment

```bash
# Using Docker
docker build -t rag-backend .
docker run -p 8000:8000 rag-backend

# Or using uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend Deployment

```bash
# Build for production
npm run build
npm start

# Or deploy to Vercel
vercel --prod
```

### Production Considerations

1. **Environment Variables**: Set API URLs and secrets
2. **CORS**: Configure allowed origins for production
3. **SSL/TLS**: Enable HTTPS in production
4. **Monitoring**: Add logging and error tracking
5. **Scaling**: Consider production vector databases (Pinecone, Weaviate)

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow existing code style and patterns
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📊 Data Sources

The system currently crawls and indexes information from:

- Tamil Nadu Government Schemes Portal
- Official government websites
- Public domain policy documents

### Adding New Data Sources

1. Update crawler configuration in `scripts/crawl_ingest.py`
2. Modify parsing logic if needed
3. Re-run the ingestion pipeline

## 🔒 Privacy & Security

- **Local Processing**: All AI inference happens locally via Ollama
- **No Data Storage**: User queries are not stored (configurable)
- **Source Citations**: All answers include official source links
- **CORS Protection**: Configurable cross-origin policies

## 📈 Performance

- **Streaming Responses**: Real-time token streaming for better UX
- **Vector Search**: Efficient similarity search with embeddings
- **Caching**: Document chunks cached in vector database
- **Async Processing**: Non-blocking API calls

## 🐛 Troubleshooting

### Common Issues

1. **Ollama Connection Failed**
   - Ensure Ollama is running: `ollama serve`
   - Verify model is pulled: `ollama list`

2. **API Connection Issues**
   - Check backend is running on port 8000
   - Verify CORS settings
   - Check firewall/antivirus

3. **Data Ingestion Problems**
   - Check internet connection for crawling
   - Verify website accessibility
   - Review crawler logs

4. **Frontend Build Issues**
   - Clear cache: `rm -rf .next node_modules`
   - Reinstall: `npm install`
   - Check Node.js version

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain** for the RAG framework
- **Ollama** for local LLM capabilities
- **ChromaDB** for vector storage
- **Next.js** for the frontend framework
- **FastAPI** for the backend API

## 📞 Support

For questions, issues, or contributions:

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Documentation**: Check individual README files

---

**Disclaimer**: This AI assistant provides information based on publicly available government data. Always verify information with official government sources for the most current and accurate details.