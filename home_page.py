import streamlit as st
st.cache(suppress_st_warning=True)
def show_home_page():
    # Set page title and icon
    # st.set_page_config(
    #     page_title="Solar Panel Fault Detection Project",
    #     page_icon="☀️"
    # )

    # Project title and logo
    st.image("Assets/solar_home.jpg", use_column_width=True)

    # Introduction
    st.write(
        "Welcome to the Solar Panel Fault Detection Project! This project is designed to identify potential faults in solar panels based on input sensor data. "
        "Explore the features, technology stack, and team behind this project to understand how it works."
    )

    # Key Features
    st.header("Key Features💡")
    st.markdown(
        "- Real-time monitoring of solar panel health\n"
        "- Accurate fault classification using machine learning\n"
        "- User-friendly interface for easy interaction"
    )

    # How It Works
    st.header("How It Works⚙️")
    # st.image("how_it_works_diagram.png", caption="System Architecture", use_column_width=True)
    st.write(
        "The solar panel fault detection system processes sensor data using a machine learning model. "
        "The model classifies faults, and users receive predictions and maintenance suggestions."
    )

    # Technology Stack
    st.header("Technology Stack💻")
    st.markdown(
        "- Machine Learning Framework: TensorFlow\n"
        "- Web Application: Streamlit\n"
        "- Data Processing: Pandas, NumPy\n"
        "- Visualization: Matplotlib"
    )

    # Data Sources
    st.header("Data Sources🗄️")
    st.write(
        "The solar panel fault detection system utilizes sensor data collected from various sources. "
        "This data is processed and used to train the machine learning model for accurate fault detection."
    )

    # Model Information
    st.header("Model Information⭐")
    st.write(
        "The machine learning model is a Convolutional Neural Network (CNN) trained on a diverse dataset. "
        "It excels in classifying different fault types in solar panels with high accuracy."
    )

    # Accuracy and Validation
    st.header("Accuracy and Validation🎯")
    st.write(
        "The model has been rigorously tested and validated using real-world data. "
        "It demonstrates high accuracy in fault classification, providing reliable predictions."
    )

    # Maintenance Suggestions
    st.header("Maintenance Suggestions⚒️")
    st.write(
        "The system generates maintenance suggestions based on the fault predictions. "
        "These suggestions are tailored to help users address specific issues and ensure the proper functioning of solar panels."
    )

    # Data Section
    st.header("Data Section📃")
    st.write(
        "The CSV data contains the following columns:\n"
        "- Time: Time of real measurement in seconds. The average sampling is 𝑇! = 9.9989 𝜇𝑠.\n"
        "- Ipv: PV array current measurement.\n"
        "- Vpv: PV array voltage measurement.\n"
        "- Vdc: DC voltage measurement.\n"
        "- ia: Phase_A current measurement.\n"
        "- ib: Phase_B current measurement.\n"
        "- ic: Phase_C current measurement.\n"
        "- va: Phase_A voltage measurement.\n"
        "- vb: Phase_B voltage measurement.\n"
        "- vc: Phase_C voltage measurement.\n"
        "- Iabc: Positive-sequence estimated current magnitude.\n"
        "- If: Positive-sequence estimated current frequency.\n"
        "- Vabc: Positive-sequence estimated voltage magnitude.\n"
        "- Vf: Positive-sequence estimated current frequency."
    )
    
if __name__ == "__main":
    show_home_page()