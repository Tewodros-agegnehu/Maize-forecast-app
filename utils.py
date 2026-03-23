import streamlit as st

def get_user_prices():
    """Streamlit widget for user input"""
    prices_text = st.text_area(
        "Enter the last 12 monthly average maize prices (ETB per 100 KG)\n"
        "One price per line — most recent on top",
        value="4800\n4600\n4500\n4700\n4900\n5100\n5200\n5300\n5400\n5500\n5600\n5700",
        height=250
    )
    
    try:
        prices = [float(x.strip()) for x in prices_text.strip().split('\n') if x.strip()]
        if len(prices) != 12:
            st.error("Please enter exactly 12 prices.")
            return None
        return prices
    except:
        st.error("Please enter valid numbers only.")
        return None