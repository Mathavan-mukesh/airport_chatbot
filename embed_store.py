import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "changi-chatbot"

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Delete existing index if it exists (Only do this if you're sure)
if INDEX_NAME in pc.list_indexes().names():
    print(f"⚠️ Deleting existing index '{INDEX_NAME}' to fix dimension mismatch...")
    pc.delete_index(INDEX_NAME)

# Create index with correct dimension (384 for MiniLM)
pc.create_index(
    name=INDEX_NAME,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)
print(f"✅ Index '{INDEX_NAME}' created with dimension 384")

# Connect to index
index = pc.Index(INDEX_NAME)

# Load embedding model
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")  # 384-dimension

# Function to embed text
def get_embedding(text: str):
    return embed_model.encode(text).tolist()

# Function to add documents
def add_documents_to_pinecone(documents: list):
    vectors = []
    for i, doc in enumerate(documents):
        embedding = get_embedding(doc)
        vectors.append((f"doc-{i}", embedding, {"text": doc}))
    index.upsert(vectors=vectors)
    print(f"✅ {len(documents)} documents added to Pinecone.")
