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

equity_query = yf.EquityQuery('eq', ['region', 'us'])
#result = yf.screen(equity_query)
#result = yf.screen("aggressive_small_caps")
result = yf.screen("day_gainers")
print(result.keys())
print()
for key in result.keys():
    print(result[key])

#print(result)

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
