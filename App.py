import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model & scaler
model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title
st.title("Diabetic Retinopathy Prognosis Predictor")
st.write("Enter patient details to predict the risk of retinopathy.")

# Inputs
age = st.number_input("Age", min_value=0, max_value=120, value=60)
systolic_bp = st.number_input("Systolic Blood Pressure", min_value=50, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=40, max_value=150, value=80)
cholesterol = st.number_input("Cholesterol Level", min_value=50, max_value=300, value=180)

# Prediction button
if st.button("Predict"):

    # Create input dataframe
    input_data = pd.DataFrame(
        [[age, systolic_bp, diastolic_bp, cholesterol]],
        columns=['age', 'systolic_bp', 'diastolic_bp', 'cholesterol']
    )

    # Scale input
    scaled_data = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_data)
    probability = model.predict_proba(scaled_data)

    # Output
    if prediction[0] == "retinopathy":
        st.error("Prediction: Retinopathy Risk Detected")
    else:
        st.success("Prediction: No Retinopathy Detected")

    # Confidence
    st.write(f"Confidence Level: {np.max(probability)*100:.2f}%")