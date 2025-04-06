
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.screener import ScreenerClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, StockLatestBarRequest, StockLatestQuoteRequest, StockLatestTradeRequest
from alpaca.trading.requests import GetCalendarRequest

from alpaca.data.live.stock import StockDataStream

from datetime import datetime, timedelta
import os
import json
import requests
import asyncio
import pandas as pd



API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

try:
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    DIR_PATH = os.path.join(DIR_PATH, "..", "data")
except NameError:
    DIR_PATH = os.getcwd()

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
screener_client = ScreenerClient(API_KEY, SECRET_KEY)
stock_data_stream_client = StockDataStream(API_KEY, SECRET_KEY)

def getCurrentData():
    tickers = []

    # TODO: get tickers via alphapy call instead?
    with open(f"{DIR_PATH}/tickers.json", "r") as file:
        tickers = json.load(file)

    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')
    #start_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

    calendar_filters = GetCalendarRequest(start=start_date, end=end_date)
    # has member vars: date, open, close
    #calendar = trading_client.get_calendar(calendar_filters)
    most_recent_trade_day = trading_client.get_calendar(calendar_filters)[-1].date

    # NOTE: Can only request 200 data points at a time which 
    # means if the timeframe == Day, we can only request 200
    # tickers at a time
    # TODO: figure out if 200 is the correct max size
    def chunk_list(tickers, size):
        for i in range(0, len(tickers), size):
            yield tickers[i:i + size]

    df = pd.DataFrame()
    latest_trades_dict = {}
    latest_bars_dict = {}
    # StockLatestQuoteRequest
    # StockLatestTradeRequest

    #StockLatestQuoteRequest ... get_stock_latest_quote
    #StockLatestTradeRequest ... get_stock_latest_trade


    # TODO: this chunk logic should be it's own function or even class that can take in any type of request
    for chunk in chunk_list(tickers, 200):
        #request_params = StockLatestQuoteRequest(
        # request_bars = StockBarsRequest(
            #symbol_or_symbols=chunk,
            #timeframe=TimeFrame.Minute
        #)
        # TODO: should i be getting all minute data for the current day or just the most recent trade 
        # (and get the rest of the current day's data from the logic defined already in getHistoricalData)?
        # TODO: figure out what's the better request type to use
        request_latest_trade = StockLatestTradeRequest(
            symbol_or_symbols=chunk,
            timeframe=TimeFrame.Minute
        )
        request_latest_bar = StockLatestBarRequest(
            symbol_or_symbols=chunk,
            timeframe=TimeFrame.Minute
        )
        #bars = data_client.get_stock_latest_quote(request_params)
        latest_trades = data_client.get_stock_latest_trade(request_latest_trade)
        latest_bars = data_client.get_stock_latest_bar(request_latest_bar)
        #df = pd.concat([df, pd.DataFrame(latest_trades)])
        latest_trades_dict.update(latest_trades)
        latest_bars_dict.update(latest_bars)

    #bars = data_client.get_stock_bars(request_params)
    #data = bars.df

    max_price = 100
    min_price = 0.01
    #df = df[min_price < df["price"] < max_price]
    latest_trades_dict = {k: v.price for k,v in latest_trades_dict.items() if v.price >= min_price and v.price <= max_price}
    latest_bars_dict = {k: v.close for k,v in latest_bars_dict.items() if v.close >= min_price and v.close <= max_price}
    #df = pd.DataFrame(list(latest_trades_dict.items()), columns=["symbol", "price"])
    #df.set_index("symbol", inplace=True)
    #print(len(latest_trades_dict))

    #df.to_csv(f"{DIR_PATH}/historicalData.csv") # historicalStockData.csv

    #df.to_json("historicalData.json", orient="index", indent=2)
    #df_symbol = df.reset_index()
    #df_symbol.set_index("symbol").to_json(f"{DIR_PATH}/historicalData.json", orient="index", indent=2) # historicalStockData.json

    return latest_trades_dict
    #return latest_bars_dict


if __name__ == "__main__":
    getCurrentData()