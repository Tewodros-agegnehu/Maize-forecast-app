# 🇪🇹 Ethiopian Maize Price Forecaster

**A Machine Learning Project for Amhara Farmers**  
*Time-series forecasting of monthly wholesale maize prices using Linear Regression*

---

### 📋 Project Overview

This project develops an accurate and interpretable forecasting system for Ethiopian maize (white) prices. The goal is to help smallholder farmers in the Amhara region make better storage and selling decisions by predicting prices **1, 2, and 3 months ahead**.

The complete Machine Learning lifecycle (from problem definition to deployment) was implemented as part of an MSc Artificial Intelligence assignment. Due to course constraints, only **Linear Regression** was used.

**Live Demo**: [https://maize-forecast-app.streamlit.app](https://maize-forecast-app.streamlit.app) 

---

### ✨ Key Features

- Monthly national average maize price forecasting
- Uses lagged prices and rolling statistics (3-month window)
- Highly interpretable model with clear coefficient insights
- User-friendly **Streamlit web application**
- Outperforms naïve baseline significantly
- Fully reproducible and production-ready

---

### 📊 Model Performance

| Metric          | Validation     | Test (2025–2026) | Target     |
|-----------------|----------------|------------------|------------|
| **RMSE**        | 235.11 ETB     | **123.67 ETB**   | -          |
| **MAE**         | 168.38 ETB     | **95.92 ETB**    | -          |
| **MAPE**        | 4.17%          | **2.04%**        | < 8–10%    |
| **R²**          | 0.737          | **0.910**        | > 0.7      |

The model significantly outperforms the naïve persistence baseline (Test MAPE = 4.96%).

---

### 🗂 Project Structure
maize-forecast-app/
├── streamlit_app.py          # Main Streamlit application
├── model.py                  # Model loading and prediction logic
├── utils.py                  # Helper functions for user input
├── maize_price_model.pkl     # Trained Linear Regression model
├── scaler.pkl                # Fitted StandardScaler
├── requirements.txt
└── README.md


---

### 🛠 Technologies Used

- **Python** 3.10+
- **scikit-learn** – Linear Regression
- **pandas & numpy** – Data processing
- **joblib** – Model persistence
- **Streamlit** – Web application framework
- **WFP Dataset** – World Food Programme Price Database

---

### 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/tewodros-agegnehu/maize-forecast-app.git
   cd maize-forecast-app

Deployment
The application is deployed on Streamlit Community Cloud and is publicly accessible.
Live Link: 
