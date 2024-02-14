import requests
import json

def get_stock_price(symbol):
    API_KEY = 'YOUR_API_KEY'
    BASE_URL = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data["Global Quote"]["05. price"]

print("The stock value of Apple is: ", get_stock_price("AAPL"))
