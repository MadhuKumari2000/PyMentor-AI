
import streamlit as st
from config import model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Revision Notes",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("📚 Python Revision Notes")

st.markdown(
    "Generate concise revision notes for any Python topic."
)

st.divider()

# -----------------------------
# User Input
# -----------------------------
st.subheader("📝 Revision Settings")

topic = st.text_input(
    "Python Topic",
    placeholder="Example: Functions, OOP, Dictionaries"
)

note_type = st.selectbox(
    "Notes Type",
    [
        "Quick Revision",
        "Interview Notes",
        "Exam Notes",
        "Detailed Notes"
    ]
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("📚 Generate Notes", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a Python topic.")
        st.stop()

    prompt = f"""
You are an expert Python instructor.

Create {note_type} notes for:

Topic: {topic}

The notes should contain:

# Definition

# Key Points

# Syntax

# Example

# Common Mistakes

# Interview Tip

# Summary

Use simple English.

Use bullet points wherever possible.

Keep the notes concise and easy to revise.
"""

    with st.spinner("Generating revision notes..."):

        try:

            response = model.generate_content(prompt)

            st.divider()

            st.subheader("📖 Your Revision Notes")

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Gemini API limit reached. Please wait a minute and try again."
            )

st.divider()

with st.expander("💡 Revision Tip", expanded=True):

    st.success(
        "Revise regularly instead of studying everything at once. Short daily revision sessions improve long-term memory."
    )
