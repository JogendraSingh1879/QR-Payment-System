# AI-Powered QR Code Payment System
This project demonstrates a prototype for an AI-powered QR Code-based account payee system for retail banking. It allows users to generate QR codes for payments, simulate transactions, and validate them for fraud detection.

# Features
QR Code Generation: Create QR codes for payment details including payee name, amount, and description.
Fraud Detection: Simulated fraud detection using predefined patterns (can be extended with AI models).
Transaction Simulation: Upload simulated scanned QR data to validate and process transactions.
Transaction History: View transaction logs for analysis.
# Tech Stack
Python: Core programming language.
Streamlit: Web application framework for rapid prototyping.
Pillow: For generating QR code images.
Pandas: For handling and displaying transaction data.
QRCode: For creating QR codes.

# Usage
**Generate QR Code**
Enter the payee name, amount, and description.
Click the "Generate QR Code" button to display the QR code.

**View Transaction History**
All valid transactions are displayed in a table.

# Future Enhancements
Integrate AI models for real-time fraud detection.
Add a database for persistent transaction storage.
Enable real QR scanning via camera integration.
Support payment gateway APIs for end-to-end payment processing.
Add dynamic currency conversion for cross-border payments.
