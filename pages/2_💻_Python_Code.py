
import streamlit as st
from config import model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Python Code Generator",
    page_icon="💻",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("💻 Python Code Generator")

st.markdown(
    "Generate beginner-friendly Python programs with explanations."
)

st.divider()

# -----------------------------
# User Input
# -----------------------------
st.subheader("📝 Describe the Program")

program = st.text_area(
    "What program do you want?",
    placeholder="Example: Write a Python program to reverse a string."
)

difficulty = st.selectbox(
    "🎯 Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("⚙️ Generate Code", use_container_width=True):

    if program.strip() == "":
        st.warning("Please describe the program.")
        st.stop()

    prompt = f"""
You are an expert Python instructor.

Generate Python code for:

{program}

Difficulty Level:
{difficulty}

Return your response in the following exact format:

## Python Code
(Only the Python code inside one Markdown code block.)

## Explanation
Explain the code step by step.

## Time Complexity

## Space Complexity

## Tips
Provide 3 beginner-friendly tips.

The explanation should match the selected difficulty level.
"""

    with st.spinner("Generating Python code..."):

        try:

            response = model.generate_content(prompt)

            st.divider()



            response_text = response.text

            # Extract the Python code block if present
            if "```python" in response_text:
                start = response_text.find("```python") + len("```python")
                end = response_text.find("```", start)

                code = response_text[start:end].strip()
                explanation = (
                    response_text[:response_text.find("```python")]
                    + response_text[end + 3:]
                )

                st.markdown("### 💻 Python Code")
                st.code(code, language="python")

                # Remove Gemini's duplicate headings
                explanation = explanation.replace("## Python Code", "")
                explanation = explanation.replace("## Explanation", "")
                explanation = explanation.replace("# Python Code", "")
                explanation = explanation.replace("# Explanation", "")

                st.markdown("### 📖 Explanation")
                st.markdown(explanation.strip())

            else:
                st.markdown(response_text)

        except Exception:

            st.error(
                "⚠️ Gemini API limit reached. Please wait a minute and try again."
            )

st.divider()

with st.expander("💡 Coding Tip", expanded=True):

    st.success(
        "Don't just copy the code. Type it yourself and experiment with different inputs."
    )
