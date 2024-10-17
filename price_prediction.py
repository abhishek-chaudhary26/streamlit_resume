import streamlit as st
import base64



# Function to load local image and convert it to base64
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image
# Setting up the page title and layout
st.set_page_config(page_title="Price Prediction Model", layout="wide")


# Load the local image (replace 'logo.png' with the actual path to your logo)
logo_base64 = load_logo('logo.png')


# Function to encode image in base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

background_image = get_base64_of_bin_file('background_image.jpg')
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
            <span>Price Prediction Model</span>
        </div>
        <div class="nav-links">
            <a href="#home" class="active">Home</a>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Create two columns
col1, col2 = st.columns(2)

# Create project cards in each column
with col1:
    options = ["hii", "hello"]
    selected_option1 = st.selectbox("Choose one of the options:", options)

    st.write(f"In column 1, you selected: {selected_option1}")

with col2:
    options2 = ["this", "hell"]
    selected_option2 = st.selectbox("Choose one of the options:", options2)
    st.write(f"In column 2, you selected: {selected_option2}")


    st.button("hello")


# Display selected options
with open("price_prediction.py", "r") as file:
    code = file.read()

with col1:
    
    st.code(code, language='python')


with col2:
    
    st.write(""" here the explanation comes""")
# Display selected options


    
