import streamlit as st
import pandas as pd
import pickle

# --------------------------
# Load model and encoder
# --------------------------
with open("xgb_crop_yield_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

categorical_cols = ["State_Name", "District_Name", "Season", "Crop"]

# --------------------------
# Load dataset to get options for dropdowns
# --------------------------
data = pd.read_csv("crop_production.csv")
data.columns = data.columns.str.strip()  # clean column names

# Get unique values for dropdowns
states = sorted(data["State_Name"].dropna().unique())
districts = sorted(data["District_Name"].dropna().unique())
seasons = sorted(data["Season"].dropna().unique())
crops = sorted(data["Crop"].dropna().unique())

# --------------------------
# Streamlit App
# --------------------------
st.title("🌾 India Crop Yield Prediction")

st.write("Select the crop details to predict expected yield:")

state = st.selectbox("State Name", states)
district = st.selectbox("District Name", districts)
year = st.number_input("Crop Year", min_value=2000, max_value=2030, value=2023)
season = st.selectbox("Season", seasons)
crop = st.selectbox("Crop Name", crops)

if st.button("Predict Yield"):
    # Prepare input dataframe
    custom_data = pd.DataFrame({
        "State_Name": [state],
        "District_Name": [district],
        "Crop_Year": [year],
        "Season": [season],
        "Crop": [crop]
    })

    # Encode categorical columns
    custom_data[categorical_cols] = encoder.transform(custom_data[categorical_cols])

    # Predict
    predicted_yield = model.predict(custom_data)[0]
    st.success(f"🌱 Predicted Yield: {predicted_yield:.2f} tons/hectare")
