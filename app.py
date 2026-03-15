import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Meme Generator", layout="wide")

# Custom CSS
st.markdown("""
<style>

.main-title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#ff4b4b;
}

.subtitle{
    text-align:center;
    color:#555;
    margin-bottom:30px;
}

.upload-box{
    padding:20px;
    border-radius:12px;
    background-color:#f0f2f6;
}

.caption-box{
    padding:15px;
    border-radius:10px;
    background-color:#ffffff;
    border:1px solid #ddd;
    margin-bottom:10px;
    color:#000000;      /* 🔴 Fix: text color */
    font-size:18px;
    font-weight:500;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-title">😂 AI Meme Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload an image and let AI create hilarious meme captions</p>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1,1])

with col1:

    st.markdown("### 📤 Upload Image")

    uploaded_file = st.file_uploader("Choose a meme image", type=["jpg","png","jpeg"])

    humor_style = st.selectbox(
        "Select Humor Style",
        ["Sarcastic", "Dark Humor", "Wholesome", "Relatable", "Savage"]
    )

    generate = st.button("🚀 Generate Meme Captions")

with col2:

    st.markdown("### 🖼 Meme Preview")

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

# Caption output
st.markdown("### 💬 Generated Captions")

if generate:
    
    captions = [
        "When the code works on the first try 👀",
        "That moment when the bug fixes itself",
        "Programmer logic: It works, don't touch it",
        "When AI writes better code than you",
        "Debugging: Removing the bugs you just created"
    ]

    for cap in captions:
        st.markdown(f'<div class="caption-box">{cap}</div>', unsafe_allow_html=True)
