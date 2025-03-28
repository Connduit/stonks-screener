import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.screener import ScreenerClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, MostActivesRequest, MarketMoversRequest

from alpaca.data.live.stock import StockDataStream

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
stock_data_stream_client = StockDataStream(API_KEY, SECRET_KEY)

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
#############################################



# Create the WebSocket client
stream = StockDataStream(API_KEY, SECRET_KEY)

# Callback function to handle incoming trade data
async def on_trade(data):
    print(f"{data.symbol} - Price: {data.price}, Volume: {data.size}, Timestamp: {data.timestamp}")

# Function to stop the stream after a timeout
async def stop_after_timeout(timeout_seconds):
    print(f"Waiting {timeout_seconds} seconds before stopping the stream...")
    await asyncio.sleep(timeout_seconds)  # Wait for the specified timeout
    await stream.stop()                   # Gracefully stop the WebSocket
    print("Stream stopped.")

# Main function to run the WebSocket
async def main():
    # Start the WebSocket stream
    stream.subscribe_trades(on_trade, "AAPL")  # Stream AAPL trade data
    
    # Run both the WebSocket and the timeout function concurrently
    task1 = asyncio.create_task(stream.run())   # Run WebSocket in background
    task2 = asyncio.create_task(stop_after_timeout(60))  # Timeout after 60 seconds
    
    # Wait for both tasks to complete
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())

