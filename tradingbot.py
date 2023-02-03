import requests
import time

def get_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + symbol
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()["price"])
    else:
        return None

def main():
    symbol = "BTCUSDT"
    last_price = None
    while True:
        price = get_price(symbol)
        if price:
            if last_price and price < last_price:
                print("Price has decreased, triggering sell")
            last_price = price
        time.sleep(60)

if __name__ == "__main__":
    main()
