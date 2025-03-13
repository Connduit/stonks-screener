"""
fetch data and parse it and store it as a json
"""
import yfinance as yf
# from yfinance import EquityQuery
import json
import os


# Fetch stock data
symbols = ["AAPL", "MSFT", "GOOG"] # TODO: fetch all stock symbols from file 
data = {}
"""
equity_query = yf.EquityQuery("and", [
                    yf.EquityQuery('eq', ['region', 'us']),
                    yf.EquityQuery("gte", ["intradayprice", 5]),
                    yf.EquityQuery("btwn", ["dayvolume", 50_000_000, 1_000_000_000_000]) # Needs to be done like this because sometimes stocks with 0 volume show up as over 1trillion
                    #yf.EquityQuery("gt", ["dayvolume", 50000000])
                    ])

#equity_query = yf.EquityQuery('eq', ['region', 'us'])
result = yf.screen(equity_query, size = 250) # default size is 100? max is 250?
#result = yf.screen("aggressive_small_caps")
#result = yf.screen("day_gainers")
#result = yf.screen("most_actives")
print(result.keys())
print()
for key in result.keys():
    print(result[key])

print()
print()
for val in result["quotes"]:
    print(val)

result_symbols = [val["symbol"] for val in result["quotes"]]
print(result_symbols)

#print(result)
"""

import requests

def get_polygon_tickers():
    url = f'https://api.polygon.io/v3/reference/tickers?apiKey={a73jrAdWlq0ke5BtQiqYNBZuE8AjZKS2}'

    response = requests.get(url)
    tickers = response.json()

    print(tickers["results"])

    return tickers['results']

# Replace with your API key
api_key = "your_polygon_api_key"
tickers = get_polygon_tickers()
for ticker in tickers[:10]:  # Display the first 10 tickers
    print(ticker['symbol'])



# https://yfinance-python.org/reference/index.html
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    data[symbol] = ticker.history(period="1d").to_dict(orient='records') # TODO: instead of calling history... call .get_info() and then parse down to just the data I need in the front end

# Ensure the directory exists, create it if necessary
"""
output_dir = 'assets'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save data as JSON
with open(os.path.join(output_dir, 'stock_data.json'), 'w') as file:
    json.dump(data, file, indent=4)
"""

with open("stock_data.json", "w+") as file:
    json.dump(data, file, indent=4)

print("Stock data saved successfully!")
