
import os
import streamlit as st
import google.generativeai as genai

# First try Streamlit Secrets (for deployment)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    # Otherwise use environment variable (for Colab)
    api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
