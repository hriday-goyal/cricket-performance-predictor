
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('cricket_run_predictor_model.pkl')

# App title
st.title("🏏 Cricket Performance Predictor")
st.subheader("Enter player stats to predict runs")

# Input fields
runs_last_3 = st.number_input("Runs in last 3 matches", min_value=0, max_value=200, value=50)
average = st.number_input("Batting average", min_value=0.0, max_value=100.0, value=35.0)
strike_rate = st.number_input("Strike rate", min_value=0.0, max_value=300.0, value=130.0)

# Predict button
if st.button("Predict Runs"):
    features = pd.DataFrame([[runs_last_3, average, strike_rate]], 
                            columns=['runs_last_3_matches', 'average', 'strike_rate'])
    prediction = model.predict(features)[0]
    st.success(f"🎯 Predicted Runs: {prediction:.2f}")
