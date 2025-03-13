import yfinance as yf
import json
import os

# Fetch stock data
symbols = ["AAPL", "MSFT", "GOOG"]
data = {}

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

with open("stock_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Stock data saved successfully!")
