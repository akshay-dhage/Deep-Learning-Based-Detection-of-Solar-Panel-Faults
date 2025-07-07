# Import libraries
import pandas as pd
import numpy as np
import streamlit as st
from pickle import load
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# ***************************************************
# Load Models
model = load_model('Assets/model.h5')
scaler = load(open('Assets/scaler.pkl','rb'))
encoder = load(open('Assets/encoder.pkl','rb'))
# ***************************************************

# ***************************************************
# Functions
def pre_processing(data):
    unwanted_cols = []
    if 'Time' in data.columns:
        unwanted_cols.append('Time')
    if 'label' in data.columns:
        unwanted_cols.append('label')
    data.drop(columns=unwanted_cols,inplace=True)
    
    X = data.iloc[:,:]
    X = scaler.fit_transform(X)
    
    X_t = []
    window = 20

    for i in np.arange(0, len(X)-window,1):
                X_t.append(X[i:i+window])
    
    X_t = np.array(X_t)
    
    X_T = X_t.reshape((X_t.shape[0],X_t.shape[1],X_t.shape[2],1))

    return X_T

def post_processing(y_pred):
    y_pred = y_pred.argmax(axis=1)
    y_pred = encoder.inverse_transform(y_pred)
    
    return y_pred

def get_prediction(data):
    # Preprocessing
    processedData = pre_processing(data)
    
    # Prediction
    result = model.predict(processedData[:1000])
    
    # Post Processing
    processedResult =  post_processing(result)
    
    return processedResult

# ***************************************************

fault_dict = {  "F0": r"Normal",
                "F1": r"Inverter Fault",
                "F2": r"Feedback Sensor fault",
                "F3": r"Grid anomaly",
                "F4": r"PV array mismatch: 10 to 20% nonhomogeneous partial shading",
                "F5": r"PV array mismatch: 15% open circuit in PV array",
                "F6": r"MPPT/IPPT controller fault",
                "F7": r"Boost converter controller fault"}

maintenance_suggestions = {
    # "Normal": "No maintenance required. The solar panel is functioning correctly.",
    "Inverter Fault": "Check and repair the inverter. It may be malfunctioning.",
    "Feedback Sensor fault": "Inspect and replace the feedback sensor if necessary.",
    "Grid anomaly": "Investigate and address any anomalies in the grid connection.",
    "PV array mismatch: 10 to 20% nonhomogeneous partial shading": "Optimize the solar panel arrangement to reduce shading effects.",
    "PV array mismatch: 15% open circuit in PV array": "Inspect and repair the PV array for open circuits.",
    "MPPT/IPPT controller fault": "Examine and fix issues with the MPPT/IPPT controller.",
    "Boost converter controller fault": "Inspect and address problems with the boost converter controller.",
}




# ***************************************************

# ***************************************************
# StreamLit App
st.cache(suppress_st_warning=True)
def show_prediction_page():
    
    
    st.image("Assets/solar_pred.jpeg", use_column_width=True)
    st.markdown(
        """
        Welcome to the Solar Panel Fault Detection App! This app is designed to help identify potential faults 
        in solar panels based on input data. Upload a CSV file containing sensor data to get started.

        The app uses a CNN model to make predictions, and the results are presented in 
        an interactive pie chart. Additionally, based on the prediction it gives suggestions 
        for the maintenance of the solar pannels.

        To begin, simply use the file uploader to upload your CSV file and explore the results.
        """
    )
    
    uploaded_file = st.file_uploader("Upload sensor data",type='csv')

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        
        st.subheader("Uploaded Data:")
        st.write(data)
        
        with st.spinner("Processing..."):
            predictions = get_prediction(data)
        
        confidence_threshold = 25
        predictions_class = pd.Series([x[:-1] for x in predictions])
        prediction_counts = predictions_class.value_counts()
        prediction_counts_filtered = predictions_class.apply(lambda x: 'F0' if prediction_counts[x] / len(predictions) * 100 < 25 else x)
        prediction_counts_filtered = prediction_counts_filtered.replace(fault_dict).value_counts()
        # flag = False if prediction_counts_filtered.index[0]=='Normal' else True
        st.subheader("Predictions:")
        st.write(prediction_counts_filtered)
        
        fig, ax = plt.subplots()
        ax.set_title("Prediction Distribution")
        ax.pie(prediction_counts_filtered, labels=prediction_counts_filtered.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  
        st.pyplot(fig)
        
        suggestion_container = st.container(border=True)
        with suggestion_container:
            st.subheader("Maintenance Suggestion:🔎⚙️⚒️")
            fault_classes = prediction_counts_filtered.index
            if 'Normal' == fault_classes[0]:
                st.success("Everything looks normal")
                if len(fault_classes)>1:
                    st.write("To be on safe side")
            else:
                st.write("Immediate attention required!")
            for fault in fault_classes:
                if fault!='Normal':
                    suggestion = maintenance_suggestions.get(fault)
                    st.write(suggestion)
                

# Run Code
if __name__ == "__main__":
    show_prediction_page()