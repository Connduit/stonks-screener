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

async def quote_handler(quote):
    print(quote)

stream = StockDataStream(API_KEY, SECRET_KEY)

async def main():
    #stream.subscribe_trades(on_trade, "AAPL")
    symbols = ["TSLA", "AAPL", "NVDA", "SPY"]
    stream.subscribe_trades(quote_handler, *symbols)
    #stream.subscribe_quotes(quote_handler, "AAPL")
    #stream.subscribe_bars(on_bar, "AAPL")

    # Run the stream
    await stream.run()

if __name__ == "__main__":
    print('fart')
    asyncio.run(stream.run())
