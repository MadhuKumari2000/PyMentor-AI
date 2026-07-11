
import streamlit as st
from config import model

# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(
    page_title="Learn Python",
    page_icon="📖",
    layout="wide"
)

# ------------------------------------
# Header
# ------------------------------------
st.title("📖 Learn Python")
st.markdown(
    "Master Python concepts with AI-generated explanations designed for every level."
)

st.divider()

# ------------------------------------
# Input Section
# ------------------------------------
st.subheader("🎯 Choose Your Topic")

topic = st.text_input(
    "Enter a Python topic",
    placeholder="Example: Variables, Lists, Functions, Loops, OOP..."
)

learning_mode = st.selectbox(
    "🎓 Learning Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Interview Preparation",
        "Quick Revision"
    ]
)

# ------------------------------------
# Generate Button
# ------------------------------------
if st.button("🧠 Explain Topic", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a Python topic.")
        st.stop()

    prompt = f"""
You are an expert Python instructor.

Teach the topic: {topic}

Learning Level:
{learning_mode}

Structure the explanation using Markdown.

Include:

# Overview

# Why it is Important

# Syntax

# Simple Example

# Real World Example

# Common Mistakes

# Best Practices

# Practice Question

# Summary

Explain according to the selected learning level.

Use simple English.

Avoid unnecessary technical jargon.
"""

    with st.spinner("Generating explanation..."):

        response = model.generate_content(prompt)

    st.divider()

    st.subheader("📚 AI Explanation")

    # This keeps the background black
    st.markdown(response.text)

    st.divider()

    with st.expander("💡 Learning Tip", expanded=True):

        st.success(
            "Practice every concept immediately after reading it. "
            "Writing code yourself is the fastest way to learn Python."
        )
