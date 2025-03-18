"""
fetch data and parse it and store it as a json

TODO: maybe use function like get_fast_info to quickly see if stock is legit,
      then save off that data. then to actual get_info checks on saved off tickers

TODO: use yf.download instead?

"""
import yfinance as yf
# from yfinance import EquityQuery
import json
import os




"""
# TODO: note: these notes were taking from when it was 2am eastern time
    get_info():

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

def getActiveVolume(ticker):
    import datetime
    today = datetime.date.today()
    
    currentTime = datetime.datetime.now()
    # TODO: have this include pre/post market too?
    time_close = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 16, 0) # 4PM
    time_open = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 9, 30) # 9:30AM
    #timePassed = (currentTime - time_open).total_seconds() * 1000
    timePassed = (min(currentTime, time_close) - time_open).total_seconds() * 1000
    time_total = (time_close - time_open).total_seconds() * 1000
    stock_10d = ticker.history(start=today-datetime.timedelta(days=16), interval="1d")
    ### print(stock_10d["Volume"])
    # TODO: must check volume isn't 0. this could happen if we attempt to retreive volume right as a new interval starts
    currentCandleVolume = stock_10d["Volume"].iloc[-1] # rename to activeCandleVolume or activeVolume?

    if (currentCandleVolume == 0):
        currentCandleVolume = stock_10d["Volume"].iloc[-2]
        timePassed = (time_close - time_open).total_seconds() * 1000
        time_total = timePassed
 
    currentCandleVolumeRatio = currentCandleVolume / timePassed
    #currentCandleVolumeRatio = currentCandleVolume / (time_total * timePassed)
    approximateCurrentVolume = currentCandleVolumeRatio * time_total
    return approximateCurrentVolume

# TODO: merge/combine this function with properRVOL by adding addition params like "period", "interval", and other useful stuff?
def properRVOL5M(ticker):
    # TODO: this is hard coded for 1day interval atm... fix later once 1d is working
    import datetime
    today = datetime.date.today()
    
    currentTime = datetime.datetime.now()
    time_close = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 16, 0) # 4PM
    time_open = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 9, 30) # 9:30AM
    #timePassed = (currentTime - time_open).total_seconds() * 1000
    timePassed = (min(currentTime, time_close) - time_open).total_seconds() * 1000
    time_total = (time_close - time_open).total_seconds() * 1000
    stock_5m = ticker.history(period="1d", interval="5m")
    ### print(stock_5m["Volume"])
    # TODO: must check volume isn't 0. this could happen if we attempt to retreive volume right as a new interval starts
    currentCandleVolume = stock_5m["Volume"].iloc[-1] # rename to activeCandleVolume or activeVolume?

    if (currentCandleVolume == 0):
        print(f"ticker: {ticker.get_info()['symbol']} has 0 volume... recalculating")
        currentCandleVolume = stock_5m["Volume"].iloc[-2]
        timePassed = (time_close - time_open).total_seconds() * 1000
        time_total = timePassed
 
    currentCandleVolumeRatio = currentCandleVolume / timePassed
    #currentCandleVolumeRatio = currentCandleVolume / (time_total * timePassed)
    approximateCurrentVolume = currentCandleVolumeRatio * time_total

    average_volume = ((stock_5m["Volume"].iloc[:-1].tail(10).mean())/(timePassed))*time_total
    """
    print(f"currentCandleVolume = {currentCandleVolume}")
    print(f"timePassed = {timePassed}")
    print(f"currentCandleVolumeRatio = {currentCandleVolumeRatio}")
    print(f"approximateCurrentVolume = {approximateCurrentVolume}")
    print(f"average_volume = {average_volume}")
    print(f"final = {approximateCurrentVolume/average_volume}")

    #reg5mRVOL = res/average_volume
    #print(f"reg5mRVOL = {reg5mRVOL}")
    print(f"volumeInPast5mins = {approximateCurrentVolume}")

    #print(f"final5mins = {reg5mRVOL/volumeInPast5mins}")
    print(f"final5mins = {average_volume/approximateCurrentVolume}")
    """

    return (average_volume/approximateCurrentVolume)*100 # TODO: NOTE: im like 99% sure this is correct now
    #return reg5mRVOL/volumeInPast5mins

def properRVOL(ticker):
    # TODO: this is hard coded for 1day interval atm... fix later once 1d is working
    import datetime
    today = datetime.date.today()
    
    currentTime = datetime.datetime.now()
    time_close = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 16, 0) # 4PM
    time_open = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 9, 30) # 9:30AM
    #timePassed = (currentTime - time_open).total_seconds() * 1000
    timePassed = (min(currentTime, time_close) - time_open).total_seconds() * 1000
    time_total = (time_close - time_open).total_seconds() * 1000
    stock_10d = ticker.history(start=today-datetime.timedelta(days=16), interval="1d")
    # TODO: must check volume isn't 0. this could happen if we attempt to retreive volume right as a new interval starts
    currentCandleVolume = stock_10d["Volume"].iloc[-1] # rename to activeCandleVolume or activeVolume?
 
    currentCandleVolumeRatio = currentCandleVolume / timePassed
    #currentCandleVolumeRatio = currentCandleVolume / (time_total * timePassed)
    res = currentCandleVolumeRatio * time_total
    average_volume = ((stock_10d["Volume"].iloc[:-1].tail(10).mean())/(timePassed))*time_total
    """
    print(stock_10d["Volume"])

    
    print(f"currentCandleVolume = {currentCandleVolume}")
    print(f"timePassed = {timePassed}")
    print(f"currentCandleVolumeRatio = {currentCandleVolumeRatio}")
    print(f"res = {res}")
    print(f"average_volume = {average_volume}")
    print(f"final = {res/average_volume}")
    """
    
    return res/average_volume


# TODO: rename function to getColumnData?
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

    # TODO: need to check what this does during trading hours... i think it will just return yesterday value if market is still open today
    ## stock_data_yesterday = ticker.history(start=yesterday, interval="1d") # TODO: this borks if the current trading day hasn't ended yet

    #print(stock_data_yesterday.between_time(datetime.time(1), datetime.time(10,59,59))) # this doesn't work unless dataframe includes date not just time


    stock_now = ticker.history(period="1d", interval="1m", prepost=True) # TODO: see what happens after most market closes... past 8pm. Also what happens for stocks that are traadable 24hrs... TODO: do i even care what happens when the market is completly closed?
    #currentPrice = stock_now.iloc[-1]
    # TODO: stock_now.tz_convert("America/New_York", level=1)
    # TODO: stock_now.tz_convert("America/New_York")


    """ Get Current Price """
    currentPrice = stock_now.iloc[-1]["Close"]

    stock_10d = ticker.history(start=today-datetime.timedelta(days=16), interval="1d")  # 14 = 10 trading days if there's no holidays... need to change to 17 days cuz weekend + holiday?
    """ Get Current Volume """
    #currentVolume = stock_10d["Volume"].iloc[-1] # TODO: if it is past 4pm, will this include post market volume?
    currentVolume = ticker.get_info()["volume"] # TODO: this seems to get slightly more accurate/ up to date volume ?
    #print(f"currentVolume = {currentVolume}")
    #print(f"get_info() volume = {ticker.get_info()['volume']}")

    # TODO: this gap is wrong... should be prev_close - now_open
    #gap = stock_data_yesterday.iloc[-1]["Close"] - stock_data_yesterday.iloc[0]["Close"] # TODO: only works after market closes?? will def have to fix this... this will just equal 0 atm
    # TODO: see which is more efficient, storiong off get_info() or calling it multiple times
    floatShares = ticker.get_info()["floatShares"] # TODO: this doesn't match warrior trading or yahoo... it's close tho



    # TODO: need to check which is the correct volume... volume, regularMarketVolume, or volume from ticker.history??
    relativeVolume = ticker.get_info()["volume"]/ticker.get_info()["averageVolume"]




    #stock_10d_download = yf.download("QBTS", period="11d", interval="1d")

    # TODO: NOTE: yfinance doesn't include pre/post market volume data for some reason?

    relativeVolume = properRVOL(ticker)
    
    

    my_data = ticker.history(interval="5m", period="1d")
    #relvol5m = currentVolume5m/5

    # Calculate average volume for the last 10 intervals (excluding the current candle)
    # CORRECT STUFF: START - ACCORDING TO TRADINGVIEW
    #average_volume = my_data['Volume'].iloc[:-1].tail(10).mean()
    #cVol = my_data['Volume'].iloc[-1]
    #relvol5m = cVol/average_volume
    # CORRECT STUFF: END
    ##print(relvol5m)
    # Latest 5-minute volume

    last_volume = sum(stock_now.between_time("15:55", "15:59")["Volume"]) # TODO: equivalent to stock_now_5m["Volume"].iloc[-1]




    #prev_close = stock_10d.tail(3)["Close"].head(2).iloc[1]
    prev_close = stock_10d.tail(2)["Close"].iloc[0]
    now_open = stock_10d.tail(2)["Open"].iloc[-1]
    prev_close = stock_10d["Close"].iloc[-2]
    now_open = stock_10d["Open"].iloc[-1]

    #gap = (now_open - prev_close)/prev_close
    # TODO: add premarket gap (preday close to current price (if we're in premarket)) or regular gap if market is already open
    # or just calculate gap as (current_price - prev_close)/prev_close if it is premarket
    # or TODO: maybe it's ok that gap = 0 when time is: 8pm < currentTime < 4am
    gap = (now_open - prev_close)/prev_close*100 # convert to percentage

    now_close = stock_10d.tail(2)["Close"].iloc[-1]
    # TODO: this only works if trade day is over
    changeFromClose = (now_close - prev_close)/prev_close*100 # convert to percentage

    shortInterest = ticker.get_info()["sharesShort"]
    relativeVolumePercent = properRVOL5M(ticker)



    # TODO: note: can only fetch 8 days worth of 1min data at a time
    #stock_8d_1m = ticker.history(start=today-datetime.timedelta(days=7), interval="1m")  # 14 = 10 trading days if there's no holidays


    # TODO: for news i should just make another webpage to brings u to a link of news acticles
    if not ticker.get_news():
        news_title = "No News"
    else:
        news_title = ticker.get_news()[0]["content"]["title"] # [0] means get first article
    #news["title"]
    #news["pubDate"]
    #news["displayTime"]
    #news["canonicalUrl"]
    #news["canonicalUrl"]["url"]



    # TODO: maybe i can just return as a dict so i dont have to call .to_dict(orient="records")... yea this def doesn't need to be a df
    finalDataFrame = {
            "currentPrice" : [currentPrice],
            "currentVolume" : [currentVolume],
            "Gap" : [gap],
            "floatShares" : [floatShares],
            "relativeVolume" : [relativeVolume],
            "relativeVolumePercent" : [relativeVolumePercent],
            "changeFromClose" : [changeFromClose],
            "shortInterest" : [shortInterest],
            "News" : [news_title]
    }

    import pandas as pd
    return pd.DataFrame(finalDataFrame)



# Fetch stock data
symbols = ["AAPL", "MSFT", "GOOG", "NVDA", "QBTS", "ANTE", "ADTX"] # TODO: fetch all stock symbols from file 
data = {} # TODO: this is data for the most active stocks

# https://yfinance-python.org/reference/index.html
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    # TODO: note: 1d is the smallest period
    #data[symbol] = ticker.history(period="1d").to_dict(orient='records') # TODO: instead of calling history... call .get_info() and then parse down to just the data I need in the front end
    res = getStuff(ticker)
    data[symbol] = res.to_dict(orient="records")
    #print(ticker.history(period="1d", interval="1m", prepost=True))
    #print(ticker.get_fast_info().last_price) # TODO: last price during active trade hours? 
    #print(ticker.get_fast_info().shares)
    #print(ticker.history().columns)
    #print(data[symbol])
    #print()
    #data[symbol]["last_price"] = ticker.fast_info["lastPrice"]
    #data[symbol]["last_volume"] = ticker.fast_info["lastVolume"]

with open("stock_data.json", "w+") as file:
    json.dump(data, file, indent=4)

print("Stock data saved successfully!")
