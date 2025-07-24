import streamlit as st
import requests

# Set FastAPI backend URL
API_URL = "http://localhost:8000/query"  # Change if deployed to a server

# Streamlit Page Setup
st.set_page_config(page_title="Changi & Jewel Airport Chatbot", layout="centered")
st.title("🛫 Changi & Jewel Airport Chatbot")
st.markdown(
    """
    Ask me anything about **Changi Airport** or **Jewel Changi Airport** ✈️  
    _(e.g., attractions, amenities, directions, food courts, etc.)_
    """
)

# User input
user_query = st.text_input("💬 Your Question:", placeholder="e.g., What are the food options in Jewel Changi?")

# Button to trigger query
if st.button("Ask") and user_query.strip():
    with st.spinner("Thinking..."):
        try:
            # Send POST request to FastAPI
            response = requests.post(API_URL, json={"query": user_query})
            if response.status_code == 200:
                # ✅ Corrected key from 'response' to 'answer'
                result = response.json().get("answer", "Sorry, I couldn't find the answer.")
                st.success("🤖 Answer:")
                st.markdown(f"> {result}")
            else:
                st.error(f"❌ API Error: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to backend: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<small>Built with 🤗 Hugging Face, Pinecone, FastAPI & Streamlit</small>",
    unsafe_allow_html=True,
)
