# app.py
import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open("fraud_model.pkl", "rb"))

st.set_page_config(page_title="Fraud Detector", layout="centered")
st.title("💳 Credit Card Fraud Detection App")

# File upload
uploaded_file = st.file_uploader("Upload transaction CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview", data.head())

    if st.button("Predict Fraud"):
        prediction = model.predict(data)
        data['Fraud Prediction'] = prediction
        st.write("### Prediction Results", data.head())

        fraud_count = data['Fraud Prediction'].sum()
        st.success(f"Detected {fraud_count} fraudulent transaction(s) out of {len(data)}")

        # Download results
        st.download_button(
            label="📥 Download Results",
            data=data.to_csv(index=False),
            file_name='fraud_predictions.csv',
            mime='text/csv'
        )
