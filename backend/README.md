# RAG Government Assistant Backend

A FastAPI-based RAG (Retrieval-Augmented Generation) system for Indian government schemes information.

## Features

- **Web Crawling**: Automated crawling of government websites to collect scheme information
- **Document Processing**: Text cleaning, deduplication, and section extraction
- **Vector Storage**: ChromaDB for efficient document storage and retrieval
- **LLM Integration**: Ollama-powered Llama3 model for natural language responses
- **Streaming API**: Real-time streaming responses for better user experience
- **CORS Support**: Cross-origin resource sharing for frontend integration

## Tech Stack

- **FastAPI**: High-performance async web framework
- **LangChain**: Framework for LLM applications
- **ChromaDB**: Vector database for document embeddings
- **Ollama**: Local LLM inference
- **BeautifulSoup**: HTML parsing and web scraping
- **Requests**: HTTP client for web crawling

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rag-gov-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn langchain-ollama langchain-chroma beautifulsoup4 requests
   ```

3. **Install and run Ollama**
   ```bash
   # Install Ollama from https://ollama.ai
   ollama pull llama3
   ```

## Usage

### Data Ingestion

Run the crawling and ingestion script:

```bash
python -m scripts.crawl_ingest
```

This will:
- Crawl government websites for scheme information
- Process and clean the text data
- Create embeddings and store in vector database

### Start the API Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://127.0.0.1:8000`

### API Endpoints

- `GET /`: Health check endpoint
- `POST /chat`: Chat endpoint with streaming support

#### Chat Request Format

```json
{
  "query": "What are the schemes for farmers?"
}
```

#### Chat Response Format

The API returns streaming JSON responses:

```json
{"type": "token", "content": "Based on"}
{"type": "token", "content": " the information"}
{"type": "end", "sources": ["https://example.gov.in/scheme1"]}
```

## Project Structure

```
app/
├── api/
│   └── routes.py          # API endpoints
├── ingestion/
│   ├── crawler.py         # Web crawler
│   ├── parser.py          # Text processing
│   ├── chunker.py         # Document chunking
│   └── scrapper.py        # Additional scraping utilities
├── rag/
│   ├── embedder.py        # Embedding configuration
│   ├── llm.py            # LLM configuration
│   └── pipeline.py       # RAG pipeline logic
├── vectorstore/
│   └── chroma_client.py  # Vector database client
└── main.py               # FastAPI application

scripts/
├── crawl_ingest.py       # Data ingestion script
├── test_*.py            # Testing scripts
└── ...

vectorstore_db/           # ChromaDB storage
```

## Configuration

The system uses the following default configurations:

- **LLM Model**: llama3 (via Ollama)
- **Embedding Model**: llama3 embeddings
- **Vector Database**: ChromaDB with local persistence
- **Crawling**: Tamil Nadu government schemes website
- **Chunking**: Section-based chunking with metadata

## Testing

Run individual test scripts:

```bash
python -m scripts.test_scrapper
python -m scripts.test_ingest
python -m scripts.test_llm
python -m scripts.test_query
```

## Development

### Adding New Data Sources

1. Update the crawler configuration in `scripts/crawl_ingest.py`
2. Modify parsing logic in `app/ingestion/parser.py` if needed
3. Test the ingestion pipeline

### Customizing the LLM

Edit `app/rag/llm.py` to change model parameters or switch to different Ollama models.

### Extending the API

Add new endpoints in `app/api/routes.py` following the existing patterns.

## Deployment

### Production Considerations

1. **Security**: Configure CORS properly for production domains
2. **Scalability**: Consider using a production vector database like Pinecone
3. **Monitoring**: Add logging and monitoring for the API endpoints
4. **Rate Limiting**: Implement rate limiting for the chat endpoint

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.