from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Govt RAG Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "RAG Government Assistant Running"}