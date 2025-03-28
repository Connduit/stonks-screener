import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.screener import ScreenerClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, MostActivesRequest, MarketMoversRequest
from alpaca.data.live import StockDataStream


from datetime import datetime, timedelta
import os
import json
import requests
import asyncio



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

#most_active_request_params = MostActivesRequest()
#market_movers_request_params = MarketMoversRequest()

#MostActivesRequest()
#MarketMoversRequest()

from alpaca.data.live import StockDataStream
import asyncio
import os

# Load your API keys from environment variables or directly enter them
API_KEY = "PKVYRNH1J4SJ7WUIGHBF"
SECRET_KEY = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

# Create the WebSocket client
stream = StockDataStream(API_KEY, SECRET_KEY)

async def on_trade(data):
    print(f"Trade update: {data}")

async def on_bar(data):
    print(f"Bar update: {data}")

async def main():
    # Subscribe to trade data for AAPL and TSLA
    stream.subscribe_trades(on_trade, "AAPL", "TSLA")
    
    # Subscribe to bar data for AAPL and TSLA
    stream.subscribe_bars(on_bar, "AAPL", "TSLA")
    
    # Start the WebSocket
    await stream.run()

if __name__ == "__main__":
    asyncio.run(main())
