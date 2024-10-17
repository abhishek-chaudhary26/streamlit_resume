import streamlit as st
import base64

# Function to load local image and convert it to base64
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image

# Load the local image (replace 'logo.png' with the actual path to your logo)
logo_base64 = load_logo('logo.png')

# Setting up the page title and layout
st.set_page_config(page_title="My Portfolio", layout="wide")

# CSS for the top navigation bar and styling
st.markdown(f"""
    <style>
        /* Top navigation bar */
        .top-nav {{
            background-color: transparent;
            overflow: hidden;
            height: 60px;
            padding: 0 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width:100%;
        }}

        /* Logo */
        .logo {{
            float: left;
            display: flex;
            align-items: center;
        }}

        .logo img {{
            height: 40px;
            margin-right: 10px;
        }}

        .logo span {{
            color: #ECDFCC;
            font-size: 24px;
            font-weight: bold;
        }}

        /* Links */
        .nav-links {{
            float: right;
        }}

        .nav-links a {{
            color: #ECDFCC;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
        }}

        .nav-links a:hover {{
            background-color: #E47B4B;
            color: #ECDFCC;
        }}

        /* Active link */
        .nav-links a.active {{
            background-color: #E47B4B;
            color: #ECDFCC;
        }}
    </style>
    """, unsafe_allow_html=True)

# Top navigation bar
st.markdown(f"""
    <div class="top-nav">
        <div class="logo">
            <img src="data:image/png;base64,{logo_base64}" alt="logo">
            <span>My Portfolio</span>
        </div>
        <div class="nav-links">
            <a href="#home" class="active">Home</a>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
            <a href="#certificates">Certificates</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Placeholder for the rest of your page content
st.title("Welcome to My Portfolio")
st.write("This is my portfolio website with a transparent top navigation bar.")
