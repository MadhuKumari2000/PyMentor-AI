
import streamlit as st
from config import model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Python Quiz",
    page_icon="📝",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("📝 Python Quiz")

st.markdown(
    "Generate Python quizzes to test your knowledge."
)

st.divider()

# -----------------------------
# User Input
# -----------------------------
st.subheader("🎯 Quiz Settings")

topic = st.text_input(
    "Python Topic",
    placeholder="Example: Loops, Functions, OOP, Lists"
)

difficulty = st.selectbox(
    "Difficulty",
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
if st.button("📝 Generate Quiz", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a Python topic.")
        st.stop()

    prompt = f"""
You are an expert Python instructor.

Generate {questions} multiple-choice questions on the topic:

Topic: {topic}

Difficulty: {difficulty}

IMPORTANT FORMATTING RULES:

For EVERY question, follow EXACTLY this format.

Question 1:
<Write the question here>

A. <Option A>

B. <Option B>

C. <Option C>

D. <Option D>

Answer:
<Correct Option>

Explanation:
<One or two sentence explanation>

Leave ONE blank line after every option.

Leave ONE blank line after the answer.

Repeat the same format for every question.

DO NOT write options in a single line.

DO NOT use tables.

DO NOT use bullet points.

Return the response in proper Markdown.
"""

    with st.spinner("Generating Quiz..."):

        try:

            response = model.generate_content(prompt)

            st.divider()

            st.subheader("📝 Quiz")

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Gemini API limit reached. Please wait a minute and try again."
            )

st.divider()

with st.expander("💡 Quiz Tip", expanded=True):

    st.success(
        "Try answering every question before looking at the answer."
    )
