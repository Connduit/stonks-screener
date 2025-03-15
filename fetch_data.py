"""
fetch data and parse it and store it as a json

TODO: maybe use function like get_fast_info to quickly see if stock is legit,
      then save off that data. then to actual get_info checks on saved off tickers

"""
import yfinance as yf
# from yfinance import EquityQuery
import json
import os




"""
# TODO: note: these notes were taking from when it was 2am eastern time

    previousClose = the previous day's close (time zone shit was already converted)
    open = today's open
    regularMarketPreviousClose = previous days close
    regularMarketOpen = today's open
    volume == regularMarketVolume
    averageVolume = TODO: idk
    bid == ask == 0
    floatShares = float shares on the day?
    sharesOutstanding = TODO:
    sharesShort = TODO:
    shortRatio = TODO:
    shortPercentOfFloat = TODO: is this needed?
    symbol = ticker
    region = region... ie, US
    regularMarketChangePercent = from market open (9:30) to market close (4:00), price change as a %
    regularMarketPrice = close price?
    marketState = is market open or close?
    exchange = what stock exchange
    exchangeTimezoneName = name of tz
    exchangeTimezoneShortName = tz abreviation
    postMarketTime = TODO: no idea what this is... guessing it's an epoch time for when it closes
    regularMarketTime = TODO: similar to above
    postMarketPrice = closing price at 4pm
    postMarketChange = price change as a price from 4pm to 8pm... TODO: check if this percentage is only avaliable after 8pm
    regularMarketChange = price change as price from 9:30 to 4pm... TODO: check if this is only avalible after 4pm
    exchangeDataDelayedBy = price data delayed? 0 means realtime data?
    sourceInterval = data updates this often?
    postMarketChangePercent = post market change as %
    hasPrePostMarketData = self explanatory






"""


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

    # TODO: need to localalize times to be time of exchange (EST)?
    #from datetime import date
    import datetime
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    import pandas as pd
    today = pd.Timestamp.today()
    today = pd.Timestamp.today()
    #ticker.history(period="1d", interval="1m", prepost=True).to_dict(orient='records')
    # TODO: need to check what this does during trading hours... i think it will just return yesterday value if market is still open today
    stock_data_yesterday = ticker.history(start=yesterday, interval="1d") 

    #print(stock_data_yesterday.between_time(datetime.time(1), datetime.time(10,59,59))) # this doesn't work unless dataframe includes date not just time

    #import pandas as pd
    #dt = pd.to_datetime("2025-03-14 09:30:00")
    #print(stock_data_yesterday.loc[dt])
    #print(stock_data_yesterday.loc["2025-03-14 09:30:00-04:00"])
    stock_now = ticker.history(period="1d", interval="1m", prepost=True) # TODO: see what happens after most market closes... past 8pm. Also what happens for stocks that are traadable 24hrs... TODO: do i even care what happens when the market is completly closed?
    #currentPrice = stock_now.iloc[-1]
    # TODO: stock_now.tz_convert("America/New_York", level=1)
    # TODO: stock_now.tz_convert("America/New_York")

    currentVolume = stock_now.iloc[-1]["Volume"] # TODO: idk how we should handle this during post market? probs fine how it is? this only works if it's before 8pm
    currentPrice = stock_now.iloc[-1]["Close"]

    currentVolume = stock_data_yesterday.iloc[-1]["Volume"]
    gap = stock_data_yesterday.iloc[-1]["Close"] - stock_data_yesterday.iloc[0]["Close"] # TODO: only works after market closes?? will def have to fix this... this will just equal 0 atm
    # TODO: see which is more efficient, storiong off get_info() or calling it multiple times
    floatShares = ticker.get_info()["floatShares"]

    # TODO: need to check which is the correct volume... volume, regularMarketVolume, or volume from ticker.history??
    relativeVolume = ticker.get_info()["volume"]/ticker.get_info()["averageVolume"]

    """
    proper volume calculation: 
        if market is closed... get volume from stock_data_yesterday
        if market is open... get volume from stock_now.iloc[-1]

        stock_now.between_time("09:30", "16:00")


    gap:
        TODO: maybe it's ok that gap = 0 when time is: 8pm < currentTime < 4am

    """

    #currentPrice = stock_now.tail(1)
    #print(stock_data_yesterday)
    #test = ticker.history(start=yesterday, interval="1m", prepost=True)
    #print(test)
    #ticker.history(start="", end="", interval="1m", prepost=True).to_dict(orient='records')

    # TODO: maybe i can just return as a dict so i dont have to call .to_dict(orient="records")... yea this def doesn't need to be a df
    finalDataFrame = {
            "currentPrice" : [currentPrice],
            "currentVolume" : [currentVolume],
            "Gap" : [gap],
            "floatShares" : [floatShares],
            "relativeVolume" : [relativeVolume]
    }

    print(finalDataFrame)

    return finalDataFrame


# Fetch stock data
symbols = ["AAPL", "MSFT", "GOOG", "NVDA", "QBTS"] # TODO: fetch all stock symbols from file 
data = {} # TODO: this is data for the most active stocks
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
    #print(ticker.get_fast_info().last_price) # TODO: last price during active trade hours? 
    print(ticker.get_fast_info().shares)
    #print(ticker.history().columns)
    #print(data[symbol])
    #print()
    #data[symbol]["last_price"] = ticker.fast_info["lastPrice"]
    #data[symbol]["last_volume"] = ticker.fast_info["lastVolume"]
    data[symbol][0]["last_price"] = ticker.fast_info["lastPrice"] # TODO: last price seems to be the same as close
    data[symbol][0]["Price"] = res["currentPrice"][0]
    data[symbol][0]["MyVolume"] = res["currentVolume"][0]
    data[symbol][0]["Gap"] = res["Gap"][0]
    data[symbol][0]["Float"] = res["floatShares"][0]
    data[symbol][0]["RelativeVolume"] = res["relativeVolume"][0]

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
