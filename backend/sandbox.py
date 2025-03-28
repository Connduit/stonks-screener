import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.screener import ScreenerClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, MostActivesRequest, MarketMoversRequest

from datetime import datetime, timedelta
import os
import json
import requests



API_KEY = "PKVYRNH1J4SJ7WUIGHBF"
SECRET_KEY = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
screener_client = ScreenerClient(API_KEY, SECRET_KEY)

stocks = ["NVDA", "QBTS"]
#tickers = {}
tickers = []

print(os.getcwd())

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

# screener_client

###
from alpaca.data.live import StockDataStream
import asyncio

# Replace with your Alpaca API credentials
API_KEY = 'PKVYRNH1J4SJ7WUIGHBF'
API_SECRET = 'LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS'

# Initialize Alpaca Data Client for real-time data
data_client = StockDataStream(API_KEY, API_SECRET)

# Function to check stock conditions (top gainers, volume, etc.)
def check_conditions(data):
    symbol = data.symbol
    price = data.price
    volume = data.size
    price_change = ((price - data.prev_close) / data.prev_close) * 100  # Percentage change

    if price_change > 5:
        print(f"Top Gainer: {symbol} | Price: ${price} | Change: {price_change:.2f}%")
    
    if volume > 1000000:
        print(f"High Volume: {symbol} | Volume: {volume} | Price: ${price}")

# Callback to handle real-time trade updates
async def trade_callback(data):
    check_conditions(data)

# Main function to start WebSocket streaming
async def main():
    # Subscribe to trade updates
    data_client.subscribe_trades(trade_callback, 'AAPL', 'TSLA', 'AMZN', 'NVDA', 'MSFT')
    
    # Correct WebSocket run method
    await data_client.run()  # ✅ Correct Method

# Run the event loop
asyncio.run(main())

