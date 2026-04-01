from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.rag.pipeline import query_rag_stream
import json

router = APIRouter()


@router.post("/chat")
async def chat(request: dict):
    query = request.get("query", "")

    async def generator():
        async for chunk in query_rag_stream(query):
            yield chunk

    return StreamingResponse(
        generator(),
        media_type="application/x-ndjson"
    )