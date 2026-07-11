
import streamlit as st
from config import model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Interview Questions",
    page_icon="🎤",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🎤 Python Interview Questions")

st.markdown(
    "Practice Python interview questions with AI-generated answers."
)

st.divider()

# -----------------------------
# User Input
# -----------------------------
st.subheader("🎯 Interview Settings")

topic = st.text_input(
    "Interview Topic",
    placeholder="Example: OOP, Functions, Exception Handling"
)

difficulty = st.selectbox(
    "Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

questions = st.selectbox(
    "Number of Questions",
    [5, 10, 15]
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("🎤 Generate Questions", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    prompt = f"""
You are an experienced Python interviewer.

Generate {questions} interview questions on:

Topic: {topic}

Difficulty: {difficulty}

For every question include:

## Question

## Ideal Answer

## Interview Tip

Use Markdown formatting.

Keep answers concise but interview-ready.
"""

    with st.spinner("Preparing interview questions..."):

        try:

            response = model.generate_content(prompt)

            st.divider()

            st.subheader("🎯 Interview Preparation")

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Gemini API limit reached. Please wait a minute and try again."
            )

st.divider()

with st.expander("💡 Interview Tip", expanded=True):

    st.success(
        "Practice answering aloud before checking the ideal answer. This improves confidence in real interviews."
    )
