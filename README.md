# 🛫 Changi & Jewel Airport Chatbot

This is a Retrieval-Augmented Generation (RAG) based chatbot that helps users ask questions about **Changi Airport** and **Jewel Changi Airport**, powered by a local LLM and vector search.

## ✨ Features

- 💬 Ask natural language questions about Changi/Jewel (e.g., food, shops, attractions)
- 🧠 Uses LLM (TinyLlama or similar) with semantic vector search (FAISS or Pinecone)
- 📄 Supports website content ingestion (from official Changi/Jewel websites)
- 📦 REST API backend (FastAPI)
- 🌐 Clean Streamlit UI
- ✅ Works offline (with local model) or online (with remote embedding/model)

## 🗂️ Project Structure

chatbot/  
├── app/                    # Core logic  
│   ├── embed_store.py      # VectorDB setup (FAISS or Pinecone)  
│   ├── load_documents.py   # Web scraping / PDF parsing  
│   ├── rag_chatbot.py      # Query answering logic (RAG + LLM)  
│   └── utils.py            # Cleaning, chunking, etc.  
├── main.py                 # FastAPI backend  
├── streamlit_app.py        # Streamlit front-end  
├── requirements.txt        # Python dependencies  
├── .gitignore  
└── README.md  

## 🚀 Quick Start

### 1. Install Dependencies

```bash
python -m venv chatbot_env  
source chatbot_env/bin/activate  
pip install -r requirements.txt  



# Run FastAPI Backend
uvicorn main:app --reload  

# Run Streamlit Frontend
streamlit run streamlit_app.py  


🧠 How It Works

    Data Source: Scraped and cleaned content from Changi/Jewel official websites.

    Embedding: Uses Hugging Face embeddings (e.g., BAAI/bge-small-en) to convert text into vectors.

    Vector Store: Stores embeddings in FAISS (or Pinecone for cloud).

    RAG Pipeline: Given a user query:

        It searches for similar chunks in the vector DB.

        Passes top results + question to the local LLM (TinyLlama or other).

        Returns an answer to the user.

🌍 Deployment

    FastAPI backend serves /query endpoint

    Can be deployed to Render, Railway, or any cloud platform

    Streamlit frontend can be deployed separately or together



📌 Tech Stack

    🐍 Python

    ⚡ FastAPI

    🧠 Hugging Face Transformers

    🔎 FAISS / Pinecone

    🧠 TinyLLaMA / Gemini

    🎨 Streamlit

    🕸️ BeautifulSoup (for scraping)



 ## Example Query
 {
  "query": "Where is Changi Airport located?"
}

## Response
{
  "answer": "Changi Airport is located in Singapore."
}


🙏 Acknowledgements

    Changi Airport Website

    Jewel Changi Website

    TinyLLaMA

    Hugging Face

    LangChain

