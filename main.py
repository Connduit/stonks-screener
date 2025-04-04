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
    #print(len(tickers))


if __name__ == "__main__":
    main()