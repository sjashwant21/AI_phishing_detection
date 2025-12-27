# AI Phishing Detection System

A machine learning-based system designed to detect phishing URLs. This project uses a Random Forest classifier to analyze URL features—such as length, special characters, and suspicious keywords—to determine if a link is legitimate or malicious.

## 📂 Project Structure

```text
phishing_detection/
├── data/
│   ├── dataset.csv          # Training dataset containing URLs and labels
│   └── generate_data.py     # Script to generate dummy training data
├── src/
│   ├── features.py          # Feature extraction logic (URL length, special chars, etc.)
│   ├── main.py              # Main CLI entry point for training and prediction
│   └── model.py             # Random Forest model wrapper for training/loading
├── requirements.txt         # Python dependencies
├── model.pkl                # Trained model file (generated after training)
└── README.md                # Project documentation
