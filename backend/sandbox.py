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

request_params = GetAssetsRequest(
    status=AssetStatus.ACTIVE,
    asset_class=AssetClass.US_EQUITY,
    exchange=AssetExchange.NASDAQ#,
    #attributes=#Comma separated values to query for more than one attribute. (probs used for when i want to include multiple exchanges
)

all_assets = trading_client.get_all_assets(request_params)
print(all_assets)


if __name__ == "__main__":
    pass
