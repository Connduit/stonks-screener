"""
fetch data and parse it and store it as a json

TODO: maybe use function like get_fast_info to quickly see if stock is legit,
      then save off that data. then to actual get_info checks on saved off tickers

"""
import yfinance as yf
# from yfinance import EquityQuery
import json
import os


# TODO: rename function
#def getStuff():
def getStuff(ticker):
    """
    currentPrice
    volume on the day (if we're in active trading hours get volume so far)
    float
    relative daily volume 
    relative volume (5 min %)
    gap % - TODO: add premarket gap (preday close to current price (if we're in premarket)) or regular gap if market is already open
    change from close
    ATR (14 day) ????
    short interest ???

    """
    #from datetime import date
    import datetime
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    #ticker.history(period="1d", interval="1m", prepost=True).to_dict(orient='records')
    # TODO: need to check what this does during trading hours... i think it will just return yesterday value if market is still open today
    stock_data_yesterday = ticker.history(start=yesterday, interval="1d") 
    stock_now = ticker.history(period="1d", interval="1m", prepost=True) # TODO: see what happens after most market closes... past 8pm. Also what happens for stocks that are traadable 24hrs
    #currentPrice = stock_now.iloc[-1]
    print(stock_now)
    currentVolume = stock_now.iloc[-1]["Volume"] # TODO: idk how we should handle this during post market? probs fine how it is?
    currentPrice = stock_now.iloc[-1]["Close"]
    #currentPrice = stock_now.tail(1)
    print(currentPrice)
    #print(stock_data_yesterday)
    #test = ticker.history(start=yesterday, interval="1m", prepost=True)
    #print(test)
    #ticker.history(start="", end="", interval="1m", prepost=True).to_dict(orient='records')

    # TODO: maybe i can just return as a dict so i dont have to call .to_dict(orient="records")... yea this def doesn't need to be a df
    finalDataFrame = {
            "currentPrice" : [currentPrice],
            "currentVolume" : [currentVolume]
    }

    print(finalDataFrame)

    return finalDataFrame


# Fetch stock data
symbols = ["AAPL", "MSFT", "GOOG", "NVDA"] # TODO: fetch all stock symbols from file 
data = {}
"""
equity_query = yf.EquityQuery("and", [
                    yf.EquityQuery('eq', ['region', 'us']),
                    yf.EquityQuery("gte", ["intradayprice", 5]),
                    yf.EquityQuery("btwn", ["dayvolume", 50_000_000, 1_000_000_000_000]) # Needs to be done like this because sometimes stocks with 0 volume show up as over 1trillion
                    #yf.EquityQuery("gt", ["dayvolume", 50000000])
                    ])

#equity_query = yf.EquityQuery('eq', ['region', 'us'])
result = yf.screen(equity_query, size = 250) # default size is 100? max is 250?
#result = yf.screen("aggressive_small_caps")
#result = yf.screen("day_gainers")
#result = yf.screen("most_actives")
print(result.keys())
print()
for key in result.keys():
    print(result[key])

print()
print()
for val in result["quotes"]:
    print(val)

result_symbols = [val["symbol"] for val in result["quotes"]]
print(result_symbols)

#print(result)
"""

# https://yfinance-python.org/reference/index.html
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    # has key value = currentPrice, volume, regularMarketVolume, floatShares, shortRatio, previousClose, open, regularMarketOpen, regularMarketPreviousClose, 
    #print(ticker.info) 
    # TODO: note: 1d is the smallest period
    data[symbol] = ticker.history(period="1d").to_dict(orient='records') # TODO: instead of calling history... call .get_info() and then parse down to just the data I need in the front end
    res = getStuff(ticker)
    #data[symbol] = ticker.history(period="1d", interval="1m", prepost=True).to_dict(orient='records') # TODO: instead of calling history... call .get_info() and then parse down to just the data I need in the front end
    #print(ticker.history(period="1d", interval="1m", prepost=True))
    #print(ticker.fast_info)
    #print(ticker.history().columns)
    #print(data[symbol])
    #print()
    #data[symbol]["last_price"] = ticker.fast_info["lastPrice"]
    #data[symbol]["last_volume"] = ticker.fast_info["lastVolume"]
    data[symbol][0]["last_price"] = ticker.fast_info["lastPrice"] # TODO: last price seems to be the same as close
    data[symbol][0]["Price"] = res["currentPrice"][0]
    data[symbol][0]["MyVolume"] = res["currentVolume"][0]

# Ensure the directory exists, create it if necessary
"""
output_dir = 'assets'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save data as JSON
with open(os.path.join(output_dir, 'stock_data.json'), 'w') as file:
    json.dump(data, file, indent=4)
"""

with open("stock_data.json", "w+") as file:
    json.dump(data, file, indent=4)

print("Stock data saved successfully!")
