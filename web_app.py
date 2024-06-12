import streamlit as st
import PIL
from PIL import Image, ImageOps
from color_classifier import predict_color # Importing predicting color function

# Function to display the image with the size and RGB color
def display_image(Red, Green, Blue):
    img = Image.new("RGB", (200, 200), color=(Red, Green, Blue))
    img = ImageOps.expand(img, border=1, fill='black')  # Add border to the image
    st.image(img, caption='RGB Color')

# Injecting custom CSS for the toggle button and dark/light mode
toggle_css = """
    <style>
    .toggle-btn {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background-color: #ddd;
        border: none;
        color: #333;
        padding: 0.5rem 1rem;
        cursor: pointer;
        border-radius: 5px;
        font-size: 16px;
    }
    .dark-mode .toggle-btn {
        background-color: #333;
        color: #ddd;
    }
    .dark-mode body {
        background-color: #333;
        color: #ddd;
    }
    .dark-mode .sidebar-content {
        background-color: #444;
    }
    .dark-mode .stButton>button {
        background-color: #555;
        color: #ddd;
    }
    </style>
    <button class="toggle-btn" onclick="toggleMode()">Toggle Dark Mode</button>
    <script>
    function toggleMode() {
        document.body.classList.toggle('dark-mode');
    }
    </script>
"""

if __name__ == "__main__":
    hide_st_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.markdown(toggle_css, unsafe_allow_html=True)

    st.sidebar.title("About")
    st.sidebar.info(
        "**RGB Color Classifier** can predict up to 11 distinct color classes based on the RGB input from the sliders.\n\n"
        "The 11 classes are *Red, Green, Blue, Yellow, Orange, Pink, Purple, Brown, Grey, Black, and White*.\n\n"
        "This app is created and maintained by [Garima Taneja](https://github.com/garimatanejaaa)\n\n"
    )

    Title_html = """
    <style>
        .title h1 {
          user-select: none;
          font-size: 43px;
          color: white;
          background: repeating-linear-gradient(-45deg, red 0%, yellow 7.14%, rgb(0,255,0) 14.28%, rgb(0,255,255) 21.4%, cyan 28.56%, blue 35.7%, magenta 42.84%, red 50%);
          background-size: 600vw 600vw;
          -webkit-text-fill-color: transparent;
          -webkit-background-clip: text;
          animation: slide 10s linear infinite forwards;
        }
        @keyframes slide {
          0% {
            background-position-x: 0%;
          }
          100% {
            background-position-x: 600vw;
          }
        }
    </style> 
    
    <div class="title">
        <h1>RGB Color Classifier</h1>
    </div>
    """
    st.markdown(Title_html, unsafe_allow_html=True)  # Title rendering

    Red = st.slider(label="RED value: ", min_value=0, max_value=255, value=0, key="red")
    Green = st.slider(label="GREEN value: ", min_value=0, max_value=255, value=0, key="green")
    Blue = st.slider(label="BLUE value: ", min_value=0, max_value=255, value=0, key="blue")

    st.write(f'Red: {Red}, Green: {Green}, Blue: {Blue}')
    display_image(Red, Green, Blue)

    if st.button("Predict"):
        result = predict_color(Red, Green, Blue)
        st.success(f'The Color is {result}!')

