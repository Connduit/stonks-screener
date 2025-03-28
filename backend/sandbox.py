from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, TimeFrame, MostActivesRequest, MarketMoversRequest
#from datetime import datetime, timedelta
#from alpaca.data.historical.screener import ScreenerClient

import os
import json



api_key = "PKVYRNH1J4SJ7WUIGHBF"
api_secret = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

trading_client = TradingClient(api_key, api_secret, paper=True)
data_client = StockHistoricalDataClient(api_key, api_secret)

stocks = ["NVDA", "QBTS"]

print(os.getcwd())
"""
{
    AAPL,

}
"""

#tickers = {}
tickers = []

# TODO: async otherlisted.txt
with open("nasdaqlisted.txt", "r") as file:
    for line in file:
        [symbol, security_name, market_category, test_issue, financial_status, _, etf, next_shares] = line.strip().split("|")
        # Market Category: Q = Highest, G = Medium, S = Lowest
        # Financial Status: N = Normal
        #print(line)
        #tickers[symbol] = DataFrame.to_dict(orient="records")
        if (test_issue == "N"):
            if ("." in symbol):
                pass
                #print("'.' in symbol")
            tickers.append(symbol)

"""
A = NYSE MKT
N = New York Stock Exchange (NYSE)
P = NYSE ARCA
Z = BATS Global Markets (BATS)
V = Investors' Exchange, LLC (IEXG)
"""
print(len(tickers))
print(len(list(set(tickers))))

count = 0

with open("otherlisted.txt", "r") as file:
    for line in file:
        #ACT Symbol|Security Name|Exchange|CQS Symbol|ETF|Round Lot Size|Test Issue|NASDAQ Symbol
        #print(line)
        [act_symbol, security_name, exchange, cqs_symbol, etf, round_lot_size, test_issue, nasdaq_symbol] = line.strip().split("|")
        # Market Category: Q = Highest, G = Medium, S = Lowest
        # Financial Status: N = Normal
        #print(line)
        #tickers[symbol] = DataFrame.to_dict(orient="records")
        if (test_issue == "N"):
            if not act_symbol.isalpha():
                #print(f"act_symbol = {act_symbol}")
                count += 1

            tickers.append(nasdaq_symbol)

print(len(tickers))
print(len(list(set(tickers))))
print(f"count = {count}")

API_KEY = "PKVYRNH1J4SJ7WUIGHBF"
SECRET_KEY = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

# Create data client
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

from datetime import datetime, timedelta
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')

import yfinance as yf

t = yf.Ticker("AACT.U")
print(t.fast_info["open"])
print(t)
for symbol in tickers:
    t = yf.Ticker(symbol)
    fi = t.get_fast_info()
    # if t.isin = "-", then stock exists. else t.isin will return None



with open("tickers.json", "w+") as file:
    json_string = json.dump(tickers, file)




if __name__ == "__main__":
    pass
