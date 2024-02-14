import yfinance as yf

def print_apple_stock_price():
    apple = yf.Ticker("AAPL")
    print("The current stock price of Apple is: $", apple.info['currentPrice'])

print_apple_stock_price()
