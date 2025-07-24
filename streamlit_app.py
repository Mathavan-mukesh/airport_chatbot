import streamlit as st
import requests

API_URL = "http://localhost:8000/query"

st.set_page_config(page_title="Changi & Jewel Airport Chatbot", layout="centered")
st.title("🛫 Changi & Jewel Airport Chatbot")
st.markdown("""
Ask me anything about **Changi Airport** or **Jewel Changi Airport** ✈️  
_(e.g., attractions, amenities, directions, food courts, etc.)_
""")

user_query = st.text_input("💬 Your Question:", placeholder="e.g., What are the food options in Jewel Changi?")

if st.button("Ask") and user_query.strip():
    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, json={"query": user_query})
            data = response.json()

            # Debugging (Optional)
            # st.write("Debug Response:", data)

            if response.status_code == 200 and "answer" in data:
                st.success("🤖 Answer:")
                st.markdown(f"> {data['answer']}")
            else:
                st.error(f"❌ API Error: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to backend: {e}")

st.markdown("---")
st.markdown(
    "<small>Built with 🤗 Hugging Face, Pinecone, FastAPI & Streamlit</small>",
    unsafe_allow_html=True,
)
