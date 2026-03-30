from django.shortcuts import render
from projects.simple_prediction_regression.stock_linear_regression import predict_stock_price

def predict_lr(request):
    context = {}

    if request.method == "POST":
        ticker = request.POST.get("ticker", "AAPL")

        result = predict_stock_price(ticker)

        if result:
            context = result

    return render(request, "projects_html/stock_pred_lr/predict.html", context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Projects main page
def projects_index(request):
    return render(request, 'projects/index.html')

# NLP project page
def nlp_topic_modeling(request):
    return render(request, 'projects_html/nlp_tm/nlp_topic_modeling.html')

