import streamlit as st
import plotly.express as px
import pandas as pd
import base64
from PIL import Image
from io import BytesIO

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
            color: #697565;
            font-size: 24px;
            font-weight: bold;
        }}

        /* Links */
        .nav-links {{
            float: right;
        }}

        .nav-links a {{
            color: #697565;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
        }}

        .nav-links a:hover {{
            background-color: #3C3D37;
            color: #697565;
        }}

        /* Active link */
        .nav-links a.active {{
            background-color: #3C3D37;
            color: #697565;
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
        </div>
    </div>
    """, unsafe_allow_html=True)







# Function to encode image in base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

background_image = get_base64_of_bin_file('background_image.jpg')




# link css to cahnge color
st.markdown(
    """
    <style>
    a {
        color: #697565; /* Your desired link color */
        text-decoration: none; /* Optional: Removes underline */
    }
    a:hover {
        color: #697565; /* Hover color for the link */
    }
    </style>
    """, unsafe_allow_html=True
)

# Insert the base64 encoded image into the CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{background_image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)



# Title and Header
st.title("Hi there! I'm Abhishek")


col1, col2 = st.columns([2, 1])  # Column 1 is wider than Column 2

# In Column 1, add the resume content
with col1:

    st.write("""
    Hi there! I'm Abhishek, a passionate Data Scientist with a keen interest in transforming data into meaningful insights. 
    With a strong foundation in machine learning, statistical analysis, and data visualization, I thrive on solving complex 
    problems using data-driven approaches. 
    I’m excited to showcase my skills and experiences that equip me to contribute effectively in the field of data science.""")
# Short description or summary



    with open("Resume.pdf", "rb") as pdf_file:
    	PDFbyte = pdf_file.read()

    st.download_button(label="Download My Resume",
                   data=PDFbyte,
                   file_name="Resume.pdf",
                   mime='application/octet-stream')

with col2:
    st.image("image.png", caption="Bunny🐰", width=300)


#certifications
st.subheader("Certifications")
st.markdown("""<html>

    <ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
  <li>Fourth item</li>
</ul>
</html>
            -Supervised Machine Learning: Regression and Classification
            -authorized by DeepLearning.AI and Stanford University and offered through Coursera


    """)
st.write("[verifictaion link](https://coursera.org/verify/W5UTDME7S882)")


#Work Experience
# st.subheader("Experience")
# st.write("""
# ***coming soon***
# """)

# Skills
st.subheader("Skills")
skills = {
    "Programming Languages": "Python, SQL",
    "Libraries": "Pandas, Numpy, Scikit-learn, TensorFlow",
    "Tools": "Git, Docker, Jupyter Notebook, Streamlit",
}
for skill, detail in skills.items():
    st.write(f"**{skill}:** {detail}")

# Education
st.subheader("Education")
st.write("""
**Bachelor of Technology in Computer Science**  
KC Group of Institutions pandoga , UNA(H.P) 
2022 - present
""")
st.write("[KC Group of Institutions](https://www.kcinstitutes.com/una/defaultUNA.cshtml)")

st.subheader("Projects")



# CSS for styling the project cards and hover effect
st.markdown("""
    <style>
        .project-card {
            width: 300px;
            height: 400px;
            padding: 20px;
            margin: 20px;
            background-color: transparent;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s ease, transform 0.3s ease;
            cursor: pointer;
            text-align: center;
            position: relative;
        }

        .project-card:hover {
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
            transform: scale(1.05);
        }

        .project-card img {
            width: 100%;
            border-radius: 10px;
            height: 200px;
            object-fit: cover;
        }

        .project-title {
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
            color: #3C3D37;
        }

        .project-description {
            font-size: 14px;
            color: #3C3D37;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

import base64
import streamlit as st

# Function to load local image and convert it to base64
def load_local_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image


# Function to create a project card
def create_project_card(image_base64, title, description, link):
    return f"""
    <div class="project-card" style=" padding: 10px; text-align: center; margin-bottom: 20px; cursor: pointer; height: 400px;">
        <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">
            <img src="data:image/jpeg;base64,{image_base64}" alt="{title}" style="width: 100%; max-width: 200px; height: 200px; object-fit: cover; border-radius: 10px;">
            <div class="project-title" style="font-size: 20px; color : #AF8260; font-weight: bold; padding-top: 10px; height: 50px;">{title}</div>
            <div class="project-description" style="padding-top: 5px; color: #EEEDEB; height: 50px; overflow: hidden;">{description}</div>
        </a>
    </div>
    """

# Load local images (replace with your actual image paths)
image1_base64 = load_local_image('conor-luddy-IGa3Md8wP6g-unsplash.jpg')
image2_base64 = load_local_image('emiliano-vittoriosi-G_vWviqUCCg-unsplash.jpg')
image3_base64 = load_local_image('aidin-geranrekab-bV_P23FXxhI-unsplash.jpg')
image4_base64 = load_local_image('randa-marzouk-ilwI-AIAQr4-unsplash.jpg')

# Layout for the project cards (4 columns)
col1, col2, col3, col4 = st.columns(4)

# Create project cards in each column
with col1:
    st.markdown(create_project_card(
        image1_base64,  # Local image base64
        "Project 1",
        "This is a description of project 1.",
        "https://www.example.com/project1"  # Link to project
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_project_card(
        image2_base64,  # Local image base64
        "Project 2",
        "This is a description of project 2.",
        "https://www.example.com/project2"  # Link to project
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_project_card(
        image3_base64,  # Local image base64
        "Project 3",
        "This is a description of project 3.",
        "https://www.example.com/project3"  # Link to project
    ), unsafe_allow_html=True)

with col4:
    st.markdown(create_project_card(
        image4_base64,  # Local image base64
        "Project 4",
        "This is a description of project 4.",
        "https://www.google.com"  # Link to project
    ), unsafe_allow_html=True)


