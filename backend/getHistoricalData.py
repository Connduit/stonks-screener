from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, TimeFrame 
from alpaca.trading.requests import GetCalendarRequest

from datetime import datetime, timedelta
import os
import json
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

tickers = []


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

# TODO: figure
for chunk in chunk_list(tickers, 200):
    request_params = StockBarsRequest(
        symbol_or_symbols=chunk,
        timeframe=TimeFrame.Day,
        start=most_recent_trade_day,
        #start=start_date,
        end=end_date,
        limit=200
    )
    bars = data_client.get_stock_bars(request_params)
    # TODO: remove vwap column here?
    df = pd.concat([df, bars.df])

#bars = data_client.get_stock_bars(request_params)
#data = bars.df

# TODO: remove vwap column here (outside of loop)?

df.to_csv(f"{DIR_PATH}/historicalData.csv") # historicalStockData.csv

#df.to_json("historicalData.json", orient="index", indent=2)
df_symbol = df.reset_index()
df_symbol.set_index("symbol").to_json(f"{DIR_PATH}/historicalData.json", orient="index", indent=2) # historicalStockData.json

if __name__ == "__main__":
    pass
