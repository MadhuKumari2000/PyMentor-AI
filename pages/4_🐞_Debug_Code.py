
import streamlit as st
from config import model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Debug Python Code",
    page_icon="🐞",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🐞 Debug Python Code")

st.markdown(
    "Paste your Python code below and let AI help you identify and fix errors."
)

st.divider()

# -----------------------------
# User Input
# -----------------------------
st.subheader("📝 Paste Your Python Code")

code = st.text_area(
    "Python Code",
    height=300,
    placeholder="""Example:

def add(a,b)
    return a+b

print(add(5,10))
"""
)

# -----------------------------
# Debug Button
# -----------------------------
if st.button("🐞 Debug Code", use_container_width=True):

    if code.strip() == "":
        st.warning("Please paste your Python code.")
        st.stop()

    prompt = f"""
You are an expert Python debugging instructor.

Analyze the following Python code.

{code}

Return your answer in Markdown.

Include:

## Errors Found

## Corrected Python Code

## Explanation

## Best Practices

Explain everything in simple English.
"""

    with st.spinner("Analyzing your code..."):

        try:

            response = model.generate_content(prompt)

            st.divider()

            st.subheader("🛠️ Debug Report")

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Gemini API limit reached. Please wait a minute and try again."
            )

st.divider()

with st.expander("💡 Debugging Tip", expanded=True):

    st.success(
        "Read the error message carefully before fixing the code. "
        "Understanding the error is the fastest way to become a better programmer."
    )
