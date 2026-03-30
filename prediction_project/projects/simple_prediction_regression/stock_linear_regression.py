import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_stock_price(ticker):
    ticker = ticker.upper()

    data = yf.download(ticker, period="60d", interval="1d")

    if data.empty:
        return None

    data['Day'] = np.arange(len(data))
    X = data[['Day']].values
    y = data['Close'].values

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(data)]])
    prediction = model.predict(next_day)[0]

    return {
        "ticker": ticker,
        "current_price": round(float(y[-1]), 2),
        "predicted_price": round(float(prediction), 2),
    }