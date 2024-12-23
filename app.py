import streamlit as st
import qrcode
from PIL import Image
import io
import pandas as pd

# Initialize database (simulated)
transactions_db = []

# Fraud detection function (simulated)
def detect_fraud(transaction):
    fraud_patterns = ["test", "dummy"]  # Placeholder patterns
    if any(pattern in transaction["description"].lower() for pattern in fraud_patterns):
        return True
    return False

# Generate QR Code function
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Convert PIL image to byte stream
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Streamlit UI
st.title("AI-Powered QR Code Payment System")

# Step 1: QR Code Generation
st.header("Generate QR Code for Payment")
payee_name = st.text_input("Payee Name", "John Doe")
amount = st.number_input("Amount (INR)", min_value=1.0, value=100.0, step=1.0)
description = st.text_input("Description", "Payment for services")

if st.button("Generate QR Code"):
    qr_data = f"Payee: {payee_name}, Amount: {amount}, Description: {description}"
    qr_image = generate_qr(qr_data)
    st.image(qr_image, caption="Scan to Pay", use_column_width=True)

# Step 2: Transaction Validation
st.header("Simulate Payment Transaction")
uploaded_qr = st.file_uploader("Upload Scanned QR Code Data (Simulated)", type=["txt"])

if uploaded_qr:
    transaction_data = uploaded_qr.read().decode("utf-8")
    st.write("Uploaded QR Data:", transaction_data)

    # Parsing QR Data
    try:
        parsed_data = {
            "payee_name": transaction_data.split(",")[0].split(":")[1].strip(),
            "amount": float(transaction_data.split(",")[1].split(":")[1].strip()),
            "description": transaction_data.split(",")[2].split(":")[1].strip(),
        }
        st.write("Parsed Transaction Data:", parsed_data)

        # Fraud detection
        is_fraud = detect_fraud(parsed_data)
        if is_fraud:
            st.error("Transaction flagged as fraud! Please verify.")
        else:
            st.success("Transaction is valid!")
            # Add to database
            transactions_db.append(parsed_data)
    except Exception as e:
        st.error(f"Error parsing QR data: {e}")

# Step 3: Transaction History
st.header("Transaction History")
if transactions_db:
    df = pd.DataFrame(transactions_db)
    st.dataframe(df)
else:
    st.write("No transactions yet.")
