from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.predict import generate_poem

app = FastAPI(title="Poem Generator API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Prompt(BaseModel):
    text: str
    temperature: float = 0.8
    words: int = 40


@app.get("/api/v1/health")
def health():
    return {"status": "healthy"}


@app.post("/api/v1/generate")
def generate(prompt: Prompt):

    poem = generate_poem(
        prompt.text,
        max_len=50,
        words=prompt.words,
        temperature=prompt.temperature
    )

    return {
        "generated_poem": poem,
        "temperature": prompt.temperature
    }