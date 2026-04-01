from langchain_chroma import Chroma


def create_vectorstore(chunks, embeddings):
    texts = [c["text"] for c in chunks]

    metadatas = [
        {
            "source": c["source"],
            "section": c["section"]
        }
        for c in chunks
    ]

    return Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory="vectorstore_db"
    )