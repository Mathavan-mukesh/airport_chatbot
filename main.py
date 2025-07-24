import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from rag_chatbot import query_rag

app = FastAPI(title="Changi Chatbot")

class Question(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "Welcome to Changi + Jewel Chatbot API"}

@app.post("/query")
def ask(question: Question):
    answer = query_rag(question.query)
    return {"question": question.query, "answer": answer}

# Run the app only if this script is executed directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Render's dynamic PORT or default to 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)
