import streamlit as st
import numpy as np
import pandas as pd
import pickle

# 🌿 Page configuration
st.set_page_config(page_title="AgroSense", layout="wide")
st.title("🌾 AgroSense: AI-Powered Crop & Fertilizer Recommender")

# 📌 Sidebar with logo and information
with st.sidebar:
    st.image("https://i.imgur.com/G3Y3a3P.png", width=120)  # Replace with your logo
    st.markdown("## 🌾 AgroSense")
    st.markdown("**An ML-powered assistant for smart farming.**")
    st.markdown("---")
    st.markdown("### 🔍 Features")
    st.markdown("- 🌱 Crop Recommendation\n- 💊 Fertilizer Suggestion")
    st.markdown("### 📘 How to Use")
    st.markdown("1. Select a tab\n2. Fill in the inputs\n3. Get instant suggestions")
    st.markdown("---")
    st.markdown("🛠 Developed by: **Team AgroSense**")
    st.markdown("📌 Version: `1.0.0`")

# 🌾 Label-to-crop mapping
label_to_crop = {
    1: 'rice', 2: 'maize', 3: 'jute', 4: 'cotton', 5: 'coconut',
    6: 'papaya', 7: 'orange', 8: 'apple', 9: 'muskmelon', 10: 'watermelon',
    11: 'grapes', 12: 'mango', 13: 'banana', 14: 'pomegranate', 15: 'lentil',
    16: 'blackgram', 17: 'mungbean', 18: 'mothbeans', 19: 'pigeonpeas',
    20: 'kidneybeans', 21: 'chickpea', 22: 'coffee'
}

# 📦 Load model and scaler
model = pickle.load(open("crop_model.pkl", "rb"))
scaler = pickle.load(open("crop_scaler.sav", "rb"))

# 📁 Load fertilizer dataset
fertilizer_df = pd.read_csv("Fertilizer Prediction.csv")
fertilizer_df.columns = fertilizer_df.columns.str.strip()

# 🧭 Tabs for navigation
tab1, tab2 = st.tabs(["🌱 Crop Recommendation", "💊 Fertilizer Suggestion"])

# 🌱 Crop Recommendation Tab
with tab1:
    st.subheader("🌱 Enter Soil & Weather Details")

    with st.form("crop_form"):
        col1, col2 = st.columns(2)

        with col1:
            N = st.number_input("Nitrogen (N)", min_value=0, max_value=140, value=50)
            P = st.number_input("Phosphorus (P)", min_value=0, max_value=140, value=40)
            K = st.number_input("Potassium (K)", min_value=0, max_value=140, value=40)
            pH = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)

        with col2:
            temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
            rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

        submitted = st.form_submit_button("🚀 Recommend Crop")

        if submitted:
            input_data = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
            scaled_input = scaler.transform(input_data)
            prediction_label = model.predict(scaled_input)[0]
            crop_prediction = label_to_crop.get(prediction_label, "Unknown Crop")
            st.success(f"✅ Recommended Crop: **{crop_prediction.upper()}**")

# 💊 Fertilizer Suggestion Tab
with tab2:
    st.subheader("💊 Get Fertilizer Suggestion Based on Crop & Soil")

    with st.form("fertilizer_form"):
        soil_type = st.selectbox("Soil Type", fertilizer_df['Soil Type'].unique())
        crop_type = st.selectbox("Crop Type", fertilizer_df['Crop Type'].unique())
        submit_fert = st.form_submit_button("🔍 Suggest Fertilizer")

        if submit_fert:
            match = fertilizer_df[
                (fertilizer_df['Soil Type'] == soil_type) &
                (fertilizer_df['Crop Type'] == crop_type)
            ]

            if not match.empty:
                fertilizer = match['Fertilizer Name'].values[0]
                st.info(f"💊 Suggested Fertilizer for **{crop_type}** on **{soil_type}** soil: **{fertilizer}**")
            else:
                st.warning("⚠️ No matching fertilizer found for the selected combination.")

# 📌 Footer
st.markdown("---")
st.markdown("🔗 [GitHub Repo](https://github.com/sarthakgarg1204/AgroSense) | 🌿 Made with ❤️ by Team AgroSense")
