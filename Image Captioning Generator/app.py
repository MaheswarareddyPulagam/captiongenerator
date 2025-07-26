import streamlit as st
from dotenv import load_dotenv
import os
from util import init_gemini, generate_caption
import google.generativeai as genai

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini model
model = init_gemini(API_KEY)

# Streamlit UI
st.set_page_config(page_title="AI Image Captioning", page_icon="📸")
st.title("📸 AI Image Caption Generator")
st.markdown("Upload an image and get a social media-ready caption powered by **Gemini Pro Vision**.")

user_prompt = st.text_input("Optional: Add a style prompt (e.g. 'funny', 'inspirational', 'for Instagram')")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    
    with st.spinner("Generating caption..."):
        caption = generate_caption(model, uploaded_file, user_prompt)
        st.success("✅ Caption Generated!")
        st.markdown(f"### 📝 Caption:\n{caption}")
