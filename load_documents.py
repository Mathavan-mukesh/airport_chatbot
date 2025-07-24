# load_documents.py
import os
from embed_store import add_documents_to_pinecone

def load_documents_from_folder(folder="data"):
    documents = []
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                documents.append(f.read())
    return documents

if __name__ == "__main__":
    docs = load_documents_from_folder()
    add_documents_to_pinecone(docs)
    print(f"✅ Uploaded {len(docs)} documents to Pinecone.")
