from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta
import pandas as pd

# Initialize Alpaca client
API_KEY = "PKVYRNH1J4SJ7WUIGHBF"
SECRET_KEY = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

# Create data client
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

# Calculate date range (3 months back from today)
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

# Request historical data
request_params = StockBarsRequest(
    symbol_or_symbols=["NVDA", "TSLA"],  # Add multiple tickers if needed
    timeframe=TimeFrame.Day,          # Options: Minute, Hour, Day, Week, etc.
    start=start_date,
    end=end_date
)

# Fetch data
bars = data_client.get_stock_bars(request_params)

# Convert data to a DataFrame for easier manipulation
data = bars.df
print(data.head())

nvda_data = data.loc["NVDA"]
avg_vol = nvda_data["volume"].mean()
#avg_vol = nvda_data.iloc[:-1]["volume"].mean()
print(avg_vol)
print(nvda_data.iloc[-1]["volume"]/avg_vol)

#time_passed = min(current_time, time_candle_close) - time_candle_open
#time_total = time_candle_close - time_candle_open
#current_ratio = volume / time_passed
#approximate_volume = current_ratio * time_total


# remaining_volume = (total_volume_traded_so_far / minutes_passed) * minutes_remaining
# rvol = (current_volume_of_active_candle/average_volume_for_time_period) * (time_elapsed/time_remaining)
#nvda_volume = 

data.to_json("data.json", orient="records", lines=True)
