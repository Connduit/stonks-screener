import os
import json

print(os.getcwd())

#tickers = {}
tickers = []

# TODO: async otherlisted.txt
with open("nasdaqlisted.txt", "r") as file:
    for line in file:
        # Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size|ETF|NextShares
        [symbol, security_name, market_category, test_issue, financial_status, _, etf, next_shares] = line.strip().split("|")
        # Market Category: Q = Highest, G = Medium, S = Lowest
        # Financial Status: N = Normal
        #print(line)
        #tickers[symbol] = DataFrame.to_dict(orient="records")
        if (test_issue == "N"):
            if not symbol.isalpha():
                print("'.' in symbol")
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
        [act_symbol, security_name, exchange, cqs_symbol, etf, round_lot_size, test_issue, nasdaq_symbol] = line.strip().split("|")
        # Market Category: Q = Highest, G = Medium, S = Lowest
        # Financial Status: N = Normal
        #print(line)
        #tickers[symbol] = DataFrame.to_dict(orient="records")
        if (test_issue == "N"):
            if not act_symbol.isalpha(): # TODO: maybe having "." is okay
                print(f"act_symbol = {act_symbol}")
                count += 1

            tickers.append(nasdaq_symbol)

print(len(tickers))
print(len(list(set(tickers))))
print(f"count = {count}")

with open("tickers.json", "w+") as file:
    json_string = json.dump(tickers, file)



if __name__ == "__main__":
    pass
