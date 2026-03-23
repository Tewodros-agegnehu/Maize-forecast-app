import streamlit as st
from model import predict_next_3_months
from utils import get_user_prices
import pandas as pd

st.set_page_config(page_title="Maize Price Forecaster", layout="centered")

st.title("🇪🇹 Maize Price Forecaster for Amhara Farmers")
st.markdown("**Predict 1–3 months ahead prices** to decide when to store or sell")

# Input
prices = get_user_prices()

if st.button(" Get Forecast", type="primary") and prices:
    with st.spinner("Calculating forecasts..."):
        pred1, pred2, pred3 = predict_next_3_months(prices)
    
    st.success(" Forecast Ready!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Next 1 Month", f"{pred1:,.0f} ETB")
    with col2:
        st.metric("Next 2 Months", f"{pred2:,.0f} ETB")
    with col3:
        st.metric("Next 3 Months", f"{pred3:,.0f} ETB")
    
    st.info("These predictions are based on your recent price history using Linear Regression.")

# Footer
st.caption("Built for the Machine Learning Assignment | Data from WFP")