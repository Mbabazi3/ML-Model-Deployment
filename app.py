import streamlit as st
import pandas as pd
import joblib


# ==========================================
# LOAD MODEL PIPELINE
# ==========================================

model = joblib.load(
    "tips_rf_pipeline.pkl"
)


# ==========================================
# APP TITLE
# ==========================================

st.title("Tip Prediction App")

st.write(
    "Enter the customer details to predict "
    "the tip amount."
)


# ==========================================
# USER INPUT
# ==========================================

total_bill = st.number_input(
    "Total Bill ($)",
    min_value=0.0,
    value=20.0
)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

smoker = st.selectbox(
    "Smoker",
    ["Yes", "No"]
)

day = st.selectbox(
    "Day",
    ["Thur", "Fri", "Sat", "Sun"]
)

time = st.selectbox(
    "Time",
    ["Lunch", "Dinner"]
)

size = st.number_input(
    "Party Size",
    min_value=1,
    max_value=20,
    value=2
)


# ==========================================
# PREDICTION
# ==========================================

if st.button("Predict Tip"):

    # Create DataFrame using the ORIGINAL
    # feature names.
    input_data = pd.DataFrame({
        "total_bill": [total_bill],
        "sex": [sex],
        "smoker": [smoker],
        "day": [day],
        "time": [time],
        "size": [size]
    })

    # The pipeline automatically:
    #
    # 1. Encodes categorical features
    # 2. Passes numerical features through
    # 3. Sends the transformed data
    #    to Random Forest
    #
    prediction = model.predict(
        input_data
    )

    st.success(
        f"Predicted Tip: ${prediction[0]:.2f}"
    )