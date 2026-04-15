# AI Chat App (FastAPI + OpenAI)

A beginner-friendly AI chat backend built with FastAPI and OpenAI's API.  
This project is intentionally simple now and structured to scale later.

## Why this project

- Build and ship a real AI feature end to end
- Learn API integration, environment management, and deployment basics
- Create a solid public GitHub project and LinkedIn portfolio piece

## Current features

- FastAPI backend with `POST /chat`
- OpenAI Chat Completions integration
- CORS support for local frontend development
- Environment variable based key management

## Tech stack

- Python
- FastAPI
- OpenAI Python SDK
- Uvicorn
- python-dotenv

## Project structure

```text
chat-app/
├── main.py
├── testAI.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Quick start

### 1) Clone and enter project

```bash
git clone <your-repo-url>
cd chat-app
```

### 2) Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

```bash
cp .env.example .env
```

Now open `.env` and add your real OpenAI key:

```env
OPENAI_API_KEY=your_real_key_here
```

### 5) Run the API server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Server docs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API usage

### Endpoint

`POST /chat`

### Request body

```json
{
  "message": "Explain AI in one sentence"
}
```

### Sample response

```json
{
  "reply": "AI is a field of computer science focused on building systems that can perform tasks that typically require human intelligence."
}
```

### cURL test

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello from curl"}'
```

## Security notes

- Never commit `.env` to GitHub
- Rotate API keys immediately if accidentally exposed
- For production, enforce tighter CORS origins and request validation

## Scale-up roadmap

Use this as the evolution path for your next versions:

1. Add conversation history (store in DB)
2. Add user auth (JWT / OAuth)
3. Add streaming responses for better UX
4. Add request rate limiting and monitoring
5. Add structured logging and error tracking
6. Containerize with Docker and deploy
7. Add tests and CI pipeline

## Suggested next commits

- `chore: add gitignore env example and dependency manifest`
- `docs: add detailed project setup and scaling roadmap`

## LinkedIn project description (copy/edit)

Built an AI Chat backend using FastAPI and OpenAI APIs with secure environment management, CORS-enabled frontend integration, and a scalable architecture roadmap. This project demonstrates practical LLM integration, API design, and production-minded engineering foundations.
