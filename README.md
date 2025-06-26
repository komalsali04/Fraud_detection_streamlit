# 💳 Credit Card Fraud Detection App

This is a lightweight web application built using **Streamlit** that predicts fraudulent transactions based on credit card data. It uses a **Logistic Regression model** trained on a balanced subset of the Kaggle credit card fraud dataset.

> 🚀 Live Demo: [Click Here](https://credit-card-fraud-detector-app.streamlit.app/)

---

## 📌 Features

- Upload a CSV file of transactions
- Predict fraudulent vs. legitimate transactions
- Download the prediction results as CSV
- SHAP integration for model explainability (coming soon)
- Built with Streamlit for easy browser-based use

---

## 🧠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## 📁 Project Structure
credit_card_fraud_detection/

├── app.py # Streamlit app code

├── fraud_model.pkl # Trained logistic regression model

├── requirements.txt # Python dependencies

├── sample_input.csv # Example input format

└── README.md # Project overview


---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fraud-detection-streamlit.git
cd fraud-detection-streamlit

##Create and Activate Virtual Environment##
python -m venv venv
.\venv\Scripts\activate     # Use source venv/bin/activate on Mac/Linux

##Install Dependencies##
pip install -r requirements.txt

##Run the app##
streamlit run app.py

 ```
📥File upload format

Make sure your uploaded CSV file matches the input format expected by the model. You can test with the included:

sample_input.csv



🎯 Model Details
- Trained using Logistic Regression on a balanced subset (492 fraud & 492 normal)

- Preprocessing includes feature scaling and class balancing

- .pkl model loaded at runtime for prediction



💡 Future Improvements
- Add SHAP-based explanations for predictions

- Allow raw dataset uploads and apply preprocessing on-the-fly

- Host as a Flask app with authentication


---
### 🧑‍💻 Author
**Komal Sali**

AI/ML Engineering Student \| Data Enthusiast \| [LinkedIn](https://www.linkedin.com/in/komal-sali-a819b6257/)

---
