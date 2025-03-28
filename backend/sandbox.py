import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, MostActivesRequest, MarketMoversRequest
#from datetime import datetime, timedelta
#from alpaca.data.historical.screener import ScreenerClient

from datetime import datetime, timedelta
import os
import json



API_KEY = "PKVYRNH1J4SJ7WUIGHBF"
SECRET_KEY = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

stocks = ["NVDA", "QBTS"]
#tickers = {}
tickers = []

print(os.getcwd())

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

###
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.live import StockDataStream
from alpaca.trading.client import TradingClient
import asyncio

API_KEY = "PKVYRNH1J4SJ7WUIGHBF"
SECRET_KEY = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"
BASE_URL = 'https://paper-api.alpaca.markets'  # or use live URL if you are on a live account

# Initialize Alpaca Trading Client for API requests
trading_client = TradingClient(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Initialize Alpaca Data Client for real-time data
data_client = StockDataStream(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Function to check stock conditions (top gainers, volume, etc.)
def check_conditions(data):
    symbol = data.symbol
    price = data.price
    volume = data.size
    price_change = ((price - data.prev_close) / data.prev_close) * 100  # Percentage change

    # Example conditions: top gainers (> 5%) and high volume (> 1M)
    if price_change > 5:
        print(f"Top Gainer: {symbol} | Price: ${price} | Change: {price_change:.2f}%")
    
    if volume > 1000000:
        print(f"High Volume: {symbol} | Volume: {volume} | Price: ${price}")

# Callback to handle real-time trade updates
async def trade_callback(data):
    check_conditions(data)

# Subscribe to trade updates for specific tickers
async def main():
    # Subscribe to trades for a list of stocks
    await data_client.subscribe_trades(trade_callback, 'AAPL', 'TSLA', 'AMZN', 'NVDA', 'MSFT')
    await data_client.run()

# Run the event loop to process WebSocket data
asyncio.run(main())

