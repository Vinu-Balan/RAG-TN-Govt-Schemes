from app.ingestion.scraper import scrape_url
from app.ingestion.chunker import chunk_text
from app.rag.embedder import get_embeddings
from app.vectorstore.chroma_client import create_vectorstore

url = "https://www.tn.gov.in/scheme_beneficiary_list.php?id=MTk="

text = scrape_url(url)
chunks = chunk_text(text)

embeddings = get_embeddings()

db = create_vectorstore(all_chunks, embeddings, all_sources)

print("Ingestion successful!")