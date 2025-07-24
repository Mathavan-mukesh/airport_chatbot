import os
from dotenv import load_dotenv
from pinecone import Pinecone
from transformers import pipeline
from sentence_transformers import SentenceTransformer

load_dotenv()

PINECONE_API_KEY = os.getenv("pcsk_5BtdPt_827YhU6YbsvN6wHwquMokMqMDHGU1B73bTTXPWsS9n3vR8HznvYWfC46XUiWN4G")
INDEX_NAME = "changi-chatbot-index"

# Init Pinecone + index
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# Embedding model
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# LLM (TinyLLaMA)
llm = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=0  # use -1 if CPU
)

def get_embedding(query):
    return embed_model.encode(query).tolist()

def search_similar_context(query, top_k=3):
    query_embedding = get_embedding(query)
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in results["matches"]]

def query_rag(question):
    print(f"📩 User Query: {question}")
    
    docs = search_similar_context(question, top_k=3)
    print("📄 Retrieved Chunks:", docs)
    
    if not docs:
        return "Sorry, I couldn't find the answer."
    
    context = "\n".join(docs)
    prompt = f"Answer the question based on the context:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    print("🧠 Prompt to LLM:", prompt)

    try:
        result = llm(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].split("Answer:")[-1].strip()
        return "Error: Unexpected output format."
    except Exception as e:
        print("❌ Error:", e)
        return "LLM generation failed."
