from langchain_chroma import Chroma
from app.rag.embedder import get_embeddings
from app.rag.llm import get_llm
import json
import asyncio


async def query_rag_stream(query: str):
    try:
        # -----------------------------
        # INIT
        # -----------------------------
        embeddings = get_embeddings()
        llm = get_llm()

        db = Chroma(
            persist_directory="vectorstore_db",
            embedding_function=embeddings
        )

        retriever = db.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 5, "fetch_k": 10}
        )

        docs = retriever.invoke(query)

        # -----------------------------
        # HYBRID MODE
        # -----------------------------
        use_rag = False
        context = ""
        sources = []

        if docs:
            combined = " ".join([d.page_content for d in docs])
            if len(combined.strip()) > 100:
                use_rag = True

        if use_rag:
            context = "\n\n".join(
                [doc.page_content for doc in docs if doc.page_content]
            )

            sources = list({
                doc.metadata.get("source")
                for doc in docs
                if doc.metadata.get("source")
            })

            prompt = f"""
You are an AI assistant for Tamil Nadu government schemes and general queries.

- Use context when relevant
- Otherwise answer normally
- Keep answers clean and readable
- Use headings and bullet points
- Never expose any phone numbers
- Don't add placeholder text like [source1], [source2], [insert link], [insert phone number] etc.
- Every bullet point should be followed by a line break for better readability.

Context:
{context}

Question:
{query}

Answer:
"""
        else:
            prompt = f"""
You are a helpful AI assistant.

Answer clearly and naturally using structured formatting.

Question:
{query}

Answer:
"""

        # Fix streaming logic
        full_text = ""

        async for chunk in llm.astream(prompt):
            text = chunk.content if hasattr(chunk, "content") else str(chunk)

            if not text:
                continue

            # Only send NEW part
            if text.startswith(full_text):
                new_text = text[len(full_text):]
            else:
                # fallback (rare case)
                new_text = text

            full_text = text

            if new_text:
                yield json.dumps({
                    "type": "token",
                    "content": new_text
                }) + "\n"

            await asyncio.sleep(0.003)

        # -----------------------------
        # FINAL
        # -----------------------------
        yield json.dumps({
            "type": "end",
            "sources": sources if use_rag else []
        }) + "\n"

    except Exception as e:
        yield json.dumps({
            "type": "end",
            "answer": "Something went wrong.",
            "sources": [],
            "error": str(e)
        }) + "\n"