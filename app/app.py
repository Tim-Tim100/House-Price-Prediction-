# app.py
import streamlit as st
import pandas as pd
import joblib
import json

# Load model and features
try:
    model = joblib.load("xgb_model.pkl")
    with open("features.json", "r") as f:
        features = json.load(f)
except Exception as e:
    st.error(f"Error loading model or features: {e}")
    st.stop()

# App title
st.title("🏡 House Price Prediction App")

# Input section
st.header("Enter House Details")
inputs = {
    "Living Area (sqft)": st.slider("Living Area (sqft)", 500, 10000, 2500),
    "Construction Grade": st.slider("Construction Grade", 1, 13, 7),
    "View Rating": st.slider("View Rating", 0, 4, 1),
    "Waterfront": st.selectbox("Waterfront", [0, 1]),
    "Latitude": st.number_input("Latitude", min_value=47.0, max_value=48.0, value=47.6),
    "Longitude": st.number_input("Longitude", min_value=-123.0, max_value=-121.0, value=-122.3),
    "House Age": st.slider("House Age", 0, 120, 20),
    "Renovated (Yes=1)": st.selectbox("Renovated", [0, 1]),
    "Living-to-Lot Ratio": st.slider("Living-to-Lot Ratio", 0.0, 1.0, 0.25),
    "Has Basement (Yes=1)": st.selectbox("Has Basement", [0, 1]),
    "Bathrooms": st.slider("Bathrooms", 1, 5, 2),
    "Bedrooms": st.slider("Bedrooms", 1, 10, 3),
}

# Show map of location
st.subheader("📍 House Location")
map_df = pd.DataFrame({
    "lat": [inputs["Latitude"]],
    "lon": [inputs["Longitude"]]
})
st.map(map_df, zoom=11)

# Prediction button
if st.button("Predict Price"):
    try:
        df_input = pd.DataFrame([inputs])[features]
        prediction = model.predict(df_input)[0]
        st.success(f"💰 Predicted Price: ${prediction:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")