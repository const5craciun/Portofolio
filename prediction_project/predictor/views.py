from django.shortcuts import render
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict(request):
    context = {}
    if request.method == "POST":
        ticker = request.POST.get('ticker', 'AAPL').upper()
        
        # Fetch 60 days of data
        data = yf.download(ticker, period="60d", interval="1d")
        
        if not data.empty:
            data['Day'] = np.arange(len(data))
            X = data[['Day']].values
            y = data['Close'].values
            
            # Simple Regression
            model = LinearRegression()
            model.fit(X, y)
            
            # Predict next day
            next_day = np.array([[len(data)]])
            prediction = model.predict(next_day)[0]
            
            context = {
                'ticker': ticker,
                'current_price': round(float(y[-1]), 2),
                'predicted_price': round(float(prediction), 2),
            }
            
    return render(request, 'predict.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')