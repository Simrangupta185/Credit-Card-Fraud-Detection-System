import streamlit as st
import pandas as pd
import joblib

# Load model
data = joblib.load("models/fraud_model.pkl")

model = data["model"]
scaler = data["scaler"]
features = data["features"]

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Credit Card Fraud Detection")
st.write(
    "Enter transaction details to estimate whether the transaction "
    "is potentially fraudulent."
)

st.divider()

time = st.number_input(
    "Transaction Time",
    min_value=0.0,
    value=10000.0
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=100.0
)

st.subheader("Transaction Features")

values = {}

for feature in features:
    if feature not in ["Time", "Amount"]:
        values[feature] = st.number_input(
            feature,
            value=0.0,
            format="%.6f"
        )

if st.button("🔍 Detect Fraud", use_container_width=True):

    transaction = pd.DataFrame([values])

    transaction["Time"] = time
    transaction["Amount"] = amount

    # Ensure correct column order
    transaction = transaction[features]

    # Scale Time and Amount
    transaction[["Time", "Amount"]] = scaler.transform(
        transaction[["Time", "Amount"]]
    )

    prediction = model.predict(transaction)[0]
    probability = model.predict_proba(transaction)[0][1]

    st.divider()

    if prediction == 1:
        st.error("⚠️ Potential Fraudulent Transaction")
    else:
        st.success("✅ Transaction Appears Legitimate")

    st.metric(
        "Fraud Probability",
        f"{probability * 100:.2f}%"
    )