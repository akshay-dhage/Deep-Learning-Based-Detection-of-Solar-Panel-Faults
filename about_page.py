import streamlit as st

def about_us():
    st.title("About Us")

    about_us_text = """
    Our Solar Panel Fault Detection System project is a collaborative endeavor led by students:

    1. Gurhal Gayatri Ram
    2. Dhage Akshay Namdev
    3. Suryawanshi Nandkishor Bapu

    under the expert guidance of Prof. A. B. Jadhav. With a shared passion for renewable energy, 
    we have developed an advanced solution that addresses the crucial need for detecting faults in solar panels. 
    Through the integration of cutting-edge technologies, including machine learning and real-time monitoring, 
    our system offers a robust framework for accurately identifying and diagnosing issues in solar panels. 
    With Prof. A. B. Jadhav mentorship and our collective expertise, we are confident that our project will significantly 
    contribute to optimizing solar power systems, reducing downtime, and maximizing energy output.
    """

    st.markdown(about_us_text)
    
if __name__ == "main":
    about_us()