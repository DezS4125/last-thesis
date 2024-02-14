import requests
from bs4 import BeautifulSoup

def get_stock_price(symbol):
    url = f"https://www.marketwatch.com/investing/stock/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('bg-quote', class_='value').text
    return price

print(get_stock_price('AAPL'))
