import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import StreamingResponse


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

chat_history = []

@app.post("/chat")
async def chat(req: ChatRequest):
    if client is None:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not configured")

    chat_history.append({"role": "user", "content": req.message})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *chat_history
        ]
    )
    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    return {"reply": reply}


@app.post('/chat-stream')
async def chat_stream(req: ChatRequest):
    chat_history.append({"role": "user", "content": req.message})
    def generate():
        stream = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *chat_history
            ],
            stream=True
        )
        for chunk in stream:
            reply = chunk.choices[0].delta.content or ''
            chat_history.append({"role": "assistant", "content": reply})
            yield reply
    return StreamingResponse(generate(), media_type="text/plain")