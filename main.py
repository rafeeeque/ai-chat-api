import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

app = FastAPI(
    title="AI Chat API",
    description="Minimal AI chat backend powered by FastAPI and OpenAI.",
    version="0.1.0",
)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: ChatRequest):
    if client is None:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not configured")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": req.message}
        ]
    )
    return {"reply": response.choices[0].message.content}