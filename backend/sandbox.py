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
    asset_class=AssetClass.US_EQUITY#,
    #exchange=AssetExchange.NASDAQ#,
    #attributes=#Comma separated values to query for more than one attribute. attrbutes are in alpacatrading.models.Asset .attributes memeber field
)
#latest_trades_dict = {k: v.price for k,v in latest_trades_dict.items() if v.price >= min_price and v.price <= max_price}
all_assets = trading_client.get_all_assets(request_params)
#all_asset_tickers = [asset.symbol for asset in all_assets]
# TODO: figure out the difference between ARCA and NYSEARCA
all_asset_tickers = [asset.symbol for asset in all_assets if (asset.exchange == AssetExchange.NASDAQ or asset.exchange == AssetExchange.NYSE or asset.exchange == AssetExchange.AMEX) and asset.tradable == True]
#print(all_assets)
#print(type(all_assets))
#print(len(all_assets))
#print(len(all_asset_tickers)) # length of data/tickers.json is 6680, but get_all_assets after being filtered returns 7940 as length
#print(all_asset_tickers)

def chunk_list(tickers, size):
    for i in range(0, len(tickers), size):
        yield tickers[i:i + size]

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

filtered_tickers = []
filtered_bars = pd.DataFrame()

for chunk in chunk_list(all_asset_tickers, 200):
    request_params = StockBarsRequest(
        symbol_or_symbols=chunk,
        timeframe=TimeFrame.Day,
        start=start_date,
        #start=start_date,
        end=end_date,
        limit=200
    )
    bars = data_client.get_stock_bars(request_params)
    #print(bars.df.index)
    #print(bars.df.columns) # Index(['open', 'high', 'low', 'close', 'volume', 'trade_count', 'vwap'], dtype='object')
    df_latest_per_ticker = bars.df.groupby(level=0).apply(lambda x: x.xs(x.index.get_level_values(1).max(), level=1))
    # df_latest_per_ticker = 
    #print(bars.df.index)
    #print(bars.df.index.get_level_values("symbol"))
    #print(bars.df.index.get_level_values("timestamp"))
    #print(bars.df.index.get_level_values(1).max()) # gets the most recent datetime to use as an index for each ticker
    #print(bars.df.index.get_level_values("timestamp"))
    

    #print(bars.df.index.get_level_values("symbol"))
    filtered_df = df_latest_per_ticker[df_latest_per_ticker['volume'] > 15_000_000]
    #print(df_latest_per_ticker)
    #print(filtered_df.index)
    #print(filtered_df.droplevel(0))
    filtered_tickers.append(filtered_df.index)
    #filtered_tickers.append(filtered_df.index.get_level_values("symbol")) # // TODO: used level number because "symbol" index is used multiple times as key
    filtered_bars = pd.concat([filtered_bars, filtered_df])
    

# TODO: index of filtered_bars is a multiindex of [symbol, symbol]... change to just a single index?
#print(filtered_tickers)
#print(filtered_bars)
#print(len(filtered_bars))
#print(filtered_bars.index)
#print(filtered_bars.columns)

#print(filtered_bars)
print(filtered_bars.droplevel(0).sort_index())

request_params = StockBarsRequest(
        symbol_or_symbols="DGLY",
        timeframe=TimeFrame.Day,
        start=start_date,
        end=end_date
    )
bars = data_client.get_stock_bars(request_params)
print(bars.df)

if __name__ == "__main__":
    pass
