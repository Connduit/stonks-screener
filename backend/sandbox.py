import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.historical.screener import ScreenerClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, MostActivesRequest, MarketMoversRequest
from alpaca.trading.requests import GetCalendarRequest, GetAssetsRequest

from alpaca.data.live.stock import StockDataStream

from alpaca.trading.enums import AssetStatus, AssetClass, AssetExchange

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

# TODO: options... make multiple request_params for each AssestExchange i want (faster but more api calls), 
# or i can have a single request_params that gets all Assets from every exchange and filter out the exchanges i don't want later (slower but less api calls)
request_params = GetAssetsRequest(
    status=AssetStatus.ACTIVE,
    asset_class=AssetClass.US_EQUITY,
    exchange=AssetExchange.NASDAQ#,
    #attributes=#Comma separated values to query for more than one attribute. attrbutes are in alpacatrading.models.Asset .attributes memeber field
)
#latest_trades_dict = {k: v.price for k,v in latest_trades_dict.items() if v.price >= min_price and v.price <= max_price}
all_assets = trading_client.get_all_assets(request_params)
all_asset_tickers = [asset.symbol for asset in all_assets]
#print(all_assets)
print(type(all_assets))
print(len(all_assets))
print(len(all_asset_tickers)) # length of data/tickers.json is 6680
print(all_asset_tickers)


if __name__ == "__main__":
    pass
