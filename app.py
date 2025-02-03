import streamlit as st
import pickle
import numpy as np
import pandas as pd


# Load trained model with error handling
try:
    with open('dbprd.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure the 'dbprd.pkl' file is available.")
    st.stop()

st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50; 
            color: white;
            font-size: 18px;           
        }
        .stTextInput input {
            background-color: #f5f5f5;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("Diabetes Prediction App")
st.write("Enter the required details to check the prediction:")

# User input fields without help text
Pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
st.markdown("like: 1, 5, 10")

Glucose = st.number_input("Glucose Level", min_value=0)
st.markdown("like: 80, 120, 150")

BloodPressure = st.number_input("Blood Pressure", min_value=0)
st.markdown("like: 70, 80, 90")

SkinThickness = st.number_input("Skin Thickness", min_value=0)
st.markdown("like: 10, 15, 20")

Insulin = st.number_input("Insulin Level", min_value=0)
st.markdown("like: 50, 100, 200")

BMI = st.number_input("BMI", min_value=0.0, format="%.2f")
st.markdown("like: 22.5, 30.0, 35.0")

DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.2f")
st.markdown("like: 0.2, 0.5, 1.2")

Age = st.number_input("Age", min_value=0, step=1)
st.markdown("like: 25, 40, 60")

# Predict Button
if st.button("Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # Check for input validity before prediction (optional)
    if any(value == 0 for value in input_data[0]):
        st.warning("Please make sure all input values are entered correctly.")
    else:
        prediction = model.predict(input_data)
        
        
        prediction = model.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The model predicts that you **may have diabetes**. 🚨 Consult a doctor.")
        else:
            st.success("The model predicts that you **do not have diabetes**. 🎉")



st.markdown("Developed by **Hardik Chudasama** | Contact: chudasamahardik333@gmail.com")