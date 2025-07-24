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
