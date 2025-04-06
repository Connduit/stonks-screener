"""
main.py
"""
from backend.getTickers_viaAlpaca import getTickers
from backend.getHistoricalData import readHistoricalData
from backend.getCurrentData import getCurrentData


# TODO: rename this def and put somewhere else?
def chunk_list(tickers, size):
    for i in range(0, len(tickers), size):
        yield tickers[i:i + size]

def main():
    tickers = getTickers() # TODO: tickers not really needed in this file?
    historical_df = readHistoricalData()
    #historical_df.groupby("symbol")

    # TODO: Apply/compute filters
    #historical_df.groupby("column_name").agg({'col_name1':'mean', 'col_name2':'sum'})
    #historical_df_groupby = historical_df.groupby("symbol")
    historical_df[f"movAvg_{3}"] = historical_df.groupby("symbol")["close"].transform(lambda df: df.rolling(window=3).mean())
    #historical_df[f"avgVol{3}"] = historical_df.groupby("symbol")["volume"].transform(lambda df: df.rolling(window=3).mean())

    current_df = getCurrentData()
    #current_df["NVDA"] # this is just the most recent price traded
    #historical_df.loc["NVDA"].iloc[-1] # most recent bar

    # TODO: FILTERS

    # Gap = open - prev_close
    #   Premarket, active, and post market
    gap = current_df["NVDA"] - historical_df.loc["NVDA"].iloc[-1]["close"]

    # Change from Close (%) = close - prev_close
    #   Premarket, active, and post market

    # Float = yfinance

    # Short Interest = yfinance

    # Relative Volume = curr_vol / avg_vol_over_past_10_days
    #   Premarket, active, and post market

    """
    market_time_close
    market_time_open
    time_passed = (min(currentTime, market_time_close) - market_time_open)
    time_total = market_time_close - market_time_open
    currentCandleVolumeRatio = currentCandleVolume / time_passed
    currentCandleVolume = currentCandleVolumeRatio * time_total


    average_volume1 = ((stock_5m["Volume"].iloc[:-1].tail(10).mean())/(timePassed))*time_total
    average_volume = stock_5m["Volume"].iloc[:-1].tail(10).mean()

    return (average_volume / approximateCurrentVolume)


    # Relative Volume (5min)
    #   Premarket, active, and post market
    """

    # (Breaking) News



    print()


if __name__ == "__main__":
    main()