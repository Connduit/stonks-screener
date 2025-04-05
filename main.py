"""
main.py
"""
from backend.getTickers_viaAlpaca import getTickers
from backend.getHistoricalData import readHistoricalData


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

    # TODO: FILTERS

    # Gap
    #   Premarket, active, and post market

    # Change from Close (%)
    #   Premarket, active, and post market

    # Float

    # Short Interest

    # Relative Volume
    #   Premarket, active, and post market

    # Relative Volume (5min)
    #   Premarket, active, and post market

    # (Breaking) News



    print()


if __name__ == "__main__":
    main()