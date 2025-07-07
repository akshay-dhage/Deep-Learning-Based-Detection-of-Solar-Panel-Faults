import base64
import streamlit as st
from database import create_table, add_user, get_user
from prediction_page import show_prediction_page
from home_page import show_home_page
from about_page import about_us
import time

create_table()

# ***************************************************
# StreamLit App Config
st.set_page_config(
    page_title="Solar Panel Fault Detection",
    page_icon="☀️"
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpeg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('Assets/background.jpg')

def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        add_user(username, password)
        st.success("Account created! Please log in.")

def login(box):
    with box.container():
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = get_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.success(f"Logged in as {username}")
                return True
            else:
                st.error("Invalid credentials. Please try again.")
                return False

st.markdown(
    """
    <style>
        @keyframes colorChange {
            0% { color: #007BFF; }
            33% { color: #FFA500; }
            66% { color: #4CAF50; }
            100% { color: #007BFF; }
        }

        .title-animation {
            animation: colorChange 10s infinite;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def login_signup():
    menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])
    if menu == "Login":
        box = st.empty()
        if login(box):
            time.sleep(1.5)
            box.empty()
            main()
    elif menu == "Sign Up":
        signup()
    
def main():
    menu = st.sidebar.selectbox("Pages", ["Home", "About Us", "Prediction"])
    if menu == "Home":
        show_home_page()
    elif menu == "About Us":
        about_us()
    elif menu=='Prediction':
        show_prediction_page()

if __name__ == "__main__":
    st.markdown("<h1 class='title-animation'>Solar Panel Fault Detection App</h1>", unsafe_allow_html=True)
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if st.session_state.logged_in:
        main()
    else:
        login_signup()