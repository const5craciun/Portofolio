from django.shortcuts import render
from projects.simple_prediction_regression.stock_linear_regression import predict_stock_price

def ml_predictor(request):
    context = {}

    if request.method == "POST":
        ticker = request.POST.get("ticker", "AAPL")

        result = predict_stock_price(ticker)

        if result:
            result["ticker"] = ticker
            context = result

    return render(request, "projects_html/stock_pred_lr/stock_prediction_lr.html", context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Projects main page
def projects_index(request):
    return render(request, 'projects_html/index.html')

# NLP project page
def nlp_topic_modeling(request):
    return render(request, 'projects_html/nlp_tm/nlp_topic_modeling.html')

