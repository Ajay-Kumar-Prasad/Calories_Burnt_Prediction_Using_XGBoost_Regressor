import streamlit as st
import pickle
import numpy as np

#Load model
with open("xgbregressor.pkl", "rb") as file:
    model = pickle.load(file)


st.title("Calories Burnt Prediction App")
st.markdown("Predict calories burnt based on your physical activity and body metrics using a trained XGBoost model.")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age (years)", min_value=1, max_value=100, value=25)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=60, max_value=200, value=110)
body_temp = st.number_input("Body Temperature (°F)", min_value=80.0, max_value=110.0, value=98.6)

# Encode gender
gender_encoded = 0 if gender == "Male" else 1

# Predict button
if st.button("Predict"):
    input_data = np.array([[age, gender_encoded, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Calories Burnt: **{prediction[0]:.2f}** kcal")
