import joblib
import numpy as np

# Load model and scaler once
model = joblib.load('maize_price_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_next_3_months(recent_prices):
    """
    recent_prices: list of 12 most recent monthly prices (newest first)
    Returns: 1-month, 2-month, 3-month forecasts
    """
    if len(recent_prices) != 12:
        raise ValueError("Need exactly 12 prices")
    
    # Compute features
    lag_3 = recent_prices[2]
    lag_6 = recent_prices[5]
    lag_12 = recent_prices[11]
    roll_mean_3 = np.mean(recent_prices[0:3])
    roll_std_3 = np.std(recent_prices[0:3])
    
    features = np.array([[lag_3, lag_6, lag_12, roll_mean_3, roll_std_3]])
    features_scaled = scaler.transform(features)
    
    # 1-month forecast
    pred1 = model.predict(features_scaled)[0]
    
    # 2-month forecast (recursive)
    features2 = np.array([[pred1, lag_3, lag_6, 
                          np.mean([pred1] + recent_prices[0:2]), 
                          np.std([pred1] + recent_prices[0:2])]])
    pred2 = model.predict(scaler.transform(features2))[0]
    
    # 3-month forecast (recursive)
    features3 = np.array([[pred2, pred1, lag_3, 
                          np.mean([pred2, pred1] + recent_prices[0:1]), 
                          np.std([pred2, pred1] + recent_prices[0:1])]])
    pred3 = model.predict(scaler.transform(features3))[0]
    
    return round(pred1, 0), round(pred2, 0), round(pred3, 0)