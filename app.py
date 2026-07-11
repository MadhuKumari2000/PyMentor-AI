
import streamlit as st


st.set_page_config(
    page_title="PyMentor AI",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Hide "app" title from sidebar */
[data-testid="stSidebarNav"] {
    padding-top: 0rem;
}

[data-testid="stSidebarNav"]::before {
    content: "🐍 PyMentor AI";
    display: block;
    font-size: 28px;
    font-weight: bold;
    color: #4DA3FF;
    margin-bottom: 10px;
    padding-left: 18px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>

/* Main page padding */
.main{
    padding-top:20px;
}

/* Hero title */
.hero-title{
    font-size:48px;
    font-weight:bold;
    color:#3776AB;
    text-align:center;
}

/* Hero subtitle */
.hero-subtitle{
    font-size:22px;
    color:#666666;
    text-align:center;
    margin-bottom:30px;
}

/* Card */
.feature-card{
    background:#F8F9FA;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #3776AB;
    margin-bottom:15px;
}

/* Card title */
.feature-title{
    font-size:22px;
    font-weight:bold;
}

/* Card description */
.feature-text{
    font-size:16px;
    color:#555555;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:20px;">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
width="90">

<h1 style="
color:#4DA3FF;
font-size:60px;
margin-bottom:5px;">
PyMentor AI
</h1>

<h3 style="color:white;">
Master Python, One Concept at a Time
</h3>

<p style="
font-size:22px;
color:#cccccc;">
Learn • Practice • Build • Debug • Grow
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Python Tip
# -----------------------------

import random

tips = [

"Use enumerate() instead of manually maintaining an index while looping.",

"Use f-strings for cleaner string formatting.",

"Remember that lists are mutable while tuples are immutable.",

"Use list comprehensions to write cleaner Python code.",

"Use virtual environments for every Python project.",

"Read error messages carefully—they usually tell you exactly what's wrong."

]

st.info(f"💡 **Python Tip of the Day**\n\n{random.choice(tips)}")

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.success("🤖 Powered by Gemini")

    st.caption("Version 1.0")

    st.caption("Made with ❤️ by Madhu")


# -----------------------------
# Home Page
# -----------------------------

st.markdown("## 🚀 Start Your Python Journey")

st.markdown("""
<div class="feature-card">

<div class="feature-title">
📖 Learn Python
</div>

<div class="feature-text">
Understand Python concepts with AI-generated explanations.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">

<div class="feature-title">
💻 Python Code Generator
</div>

<div class="feature-text">
Generate beginner-friendly Python programs with explanations.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">

<div class="feature-title">
📝 AI Quiz Generator
</div>

<div class="feature-text">
Practice Python with AI-generated multiple-choice quizzes.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">

<div class="feature-title">
🐞 Debug Assistant
</div>

<div class="feature-text">
Find mistakes in Python code and learn how to fix them.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">

<div class="feature-title">
📚 Revision Notes
</div>

<div class="feature-text">
Quick revision notes for exams and interviews.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">

<div class="feature-title">
🎤 Interview Questions
</div>

<div class="feature-text">
Practice Python interview questions with AI.
</div>

</div>
""", unsafe_allow_html=True)

st.success("👈 Select any page from the sidebar to begin learning.")
