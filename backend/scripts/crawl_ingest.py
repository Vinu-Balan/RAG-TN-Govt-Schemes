from app.ingestion.crawler import crawl_website
from app.ingestion.parser import clean_text, extract_sections
from app.ingestion.chunker import chunk_sections
from app.rag.embedder import get_embeddings
from app.vectorstore.chroma_client import create_vectorstore

BASE_URL = "https://www.tn.gov.in/scheme_beneficiary_list.php?id=MTk="

print("Starting crawl...")

pages = crawl_website(BASE_URL, max_pages=80)

all_chunks = []

for url, raw_text in pages:
    clean = clean_text(raw_text)

    if len(clean) < 200:
        continue

    sections = extract_sections(clean)

    chunks = chunk_sections(sections)

    for chunk in chunks:
        chunk["source"] = url

    all_chunks.extend(chunks)

print(f"\nTotal chunks created: {len(all_chunks)}")

# Debug sample
if all_chunks:
    print("\nSample chunk:\n", all_chunks[0]["text"][:300])

embeddings = get_embeddings()

db = create_vectorstore(all_chunks, embeddings)

print("\nIngestion complete!")