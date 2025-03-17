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
def properRVOL(ticker):
      stock_10d = ticker.history(start=today-datetime.timedelta(days=16), interval="1d")
      print(stock_10d)
      return currVol / pastVol

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
    # TODO: this gap is wrong... should be prev_close - now_open
    #gap = stock_data_yesterday.iloc[-1]["Close"] - stock_data_yesterday.iloc[0]["Close"] # TODO: only works after market closes?? will def have to fix this... this will just equal 0 atm
    # TODO: see which is more efficient, storiong off get_info() or calling it multiple times
    floatShares = ticker.get_info()["floatShares"] # TODO: this doesn't match warrior trading or yahoo... it's close tho



    # TODO: need to check which is the correct volume... volume, regularMarketVolume, or volume from ticker.history??
    relativeVolume = ticker.get_info()["volume"]/ticker.get_info()["averageVolume"]
    #stock_10d = ticker.history(start=today-datetime.timedelta(days=15), interval="1d")  # 14 = 10 trading days if there's no holidays
    stock_10d = ticker.history(start=today-datetime.timedelta(days=16), interval="1d")  # 14 = 10 trading days if there's no holidays

    #stock_10d = ticker.history(start=yesterday-datetime.timedelta(days=20), end="2025-03-14", interval="1d")  # 14 = 10 trading days if there's no holidays
    #stock_10d_download = yf.download("QBTS", period="11d", interval="1d")
    #print(stock_10d_download)

    # TODO: NOTE: yfinance doesn't include pre/post market volume data for some reason?
    avg = sum(stock_10d.head(10)["Volume"])/10
    relativeVolume = sum(stock_10d.tail(1)["Volume"])/avg # TODO: .tail() returns a series so we need to call sum to convert it back to float... there has to be a better way to do this tho

    rvol_val = properRVOL(ticker)
    
    relativeVolumePercent = -1
    stock_now_5m = ticker.history(period="1d", interval="5m")
    x = stock_now_5m["Volume"].tail(11)
    ##print(x)
    ##print(x.head(10))
    avg5m = sum(x.head(10))/10
    #currentVolume5m = x.tail(1)
    ##print(stock_now.between_time("15:55", "15:59")["Volume"])
    #currentVolume5m = sum(stock_now.between_time("15:55", "15:59")["Volume"])/5 # average 1 min volume over the past 5 mins
    currentVolume5m = sum(stock_now.between_time("15:55", "15:59")["Volume"])
    ##print(avg5m)
    ##print(currentVolume5m)
    #popped_row = stock_now_5m.iloc[-1] # TODO: this is correct.. like im pretty sure
    #stock_now_5m.drop(stock_now_5m.index[-1])
    #print(stock_now_5m)
    #print(sum(stock_now.between_time("15:55", "15:59")["Volume"])/5)
    #av5m = sum(stock_now.between_time("15:55", "15:59")["Volume"])/5
    #print(popped_row["Volume"])
    #print(sum(stock_now_5m["Volume"])/len(stock_now_5m))
    #print(sum(stock_now_5m["Volume"].tail(10))/10)
    #print(av5m)
    #relativeVolumePercent = (av5m - popped_row["Volume"])/av5m*100 # convert to percentage
    relativeVolumePercent = (avg5m - currentVolume5m)/avg5m*100 # convert to percentage
    #relativeVolumePercent = (currentVolume5m - avg5m)/currentVolume5m*100 # convert to percentage
    ##print(relativeVolumePercent)
    ##print()
    ##print()

    my_data = ticker.history(interval="5m", period="1d")
    #relvol5m = currentVolume5m/5

    if symbol == "QBTS":
        print("QBTS DATA:")

    # Calculate average volume for the last 10 intervals (excluding the current candle)
    # CORRECT STUFF: START - ACCORDING TO TRADINGVIEW
    average_volume = my_data['Volume'].iloc[:-1].tail(10).mean()
    cVol = my_data['Volume'].iloc[-1]
    relvol5m = cVol/average_volume
    # CORRECT STUFF: END
    ##print(relvol5m)
    # Latest 5-minute volume

    last_volume = sum(stock_now.between_time("15:55", "15:59")["Volume"]) # TODO: equivalent to stock_now_5m["Volume"].iloc[-1]

    # TODO: for some reason it looks like it's not looking at the 5 min interval

    test123 = stock_now.between_time("09:30", "16:00")['Volume'].iloc[:-1].tail(10).mean()


    # Comparison
    ##print(f"Latest 5-min Volume: {last_volume}")
    ##print(f"Average 5-min Volume: {average_volume}")
    ##print(f"Volume Surge: {last_volume / average_volume:.2f}x")

    #val = (test123 - last_volume)/last_volume
    val = (last_volume - test123)/test123
    #print(f"does this work: {last_volume/test123*100}")
    ##print(f"does this work: {val}")

    temp = stock_now_5m.between_time("09:30", "15:59")/last_volume
    #last_volume

    # AvgVol = ta.sma(volume[1],10) # ON 5-min interval
    #relativeVolumePercent = (AvgVol - current5minVol)/current5minVol

    #stock_10d.tail(3)["Close"]
    #print(stock_10d.tail(3)["Close"].head(2)) # TODO: is this the most efficent way to do this?
    #print(stock_10d.tail(3)["Close"].head(2).iloc[0]) # TODO: is this the most efficent way to do this?

    #prev_close = stock_10d.tail(3)["Close"].head(2).iloc[1]
    prev_close = stock_10d.tail(2)["Close"].iloc[0]
    now_open = stock_10d.tail(2)["Open"].iloc[-1]

    #gap = (now_open - prev_close)/prev_close
    gap = (now_open - prev_close)/prev_close*100 # convert to percentage

    now_close = stock_10d.tail(2)["Close"].iloc[-1]
    changeFromClose = (now_close - prev_close)/prev_close*100 # convert to percentage

    shortInterest = ticker.get_info()["sharesShort"]







    # TODO: note: can only fetch 8 days worth of 1min data at a time
    #stock_8d_1m = ticker.history(start=today-datetime.timedelta(days=7), interval="1m")  # 14 = 10 trading days if there's no holidays
    #print(sum(ticker.history(start="2025-03-07", end="2025-03-08", interval="1m").between_time("15:55","16:00")["Volume"]))
    
    #print(stock_now.between_time("15:55","16:00"))
    #print(ticker.history(start="2025-03-12", end="2025-03-13", interval="1m").between_time("15:55","16:00"))
    #avg10d = (sum(stock_now.between_time("15:55","16:00")["Volume"]) + 
    """ last5min = sum(stock_now.between_time("15:55", "16:00")["Volume"])
    stock_now_5m = ticker.history(period="1d", interval="5m")
    #print(sum(stock_now_5m["Volume"])/last5min)

    d = yf.download(symbol, interval="5m", period="5d")
    # Filter for regular trading hours (9:30 AM - 4:00 PM)
    d = d.between_time('09:30', '16:00')

    # Calculate the average 5-minute volume for regular intervals
    d['Avg_5m_Vol'] = d['Volume'].rolling(window=20).mean()

    #print(d)

    # Identify the most recent 5-minute candle's volume
    last_volume = d['Volume'].iloc[-1]

    # Compare the last 5-minute volume with the calculated average
    #print(f"Last 5-Min Volume: {last_volume}")
    #print(f"Average 5-Min Volume: {d['Avg_5m_Vol'].iloc[-1]}")
    #print()
    #print(d["Avg_5m_Vol"].iloc[-1]/last_volume)
    #print()
    #print(f"Relative Volume (RVOL): {last_volume / d['Avg_5m_Vol'].iloc[-1]:.2f}")
    """

    """
    avg10d = (
                sum(ticker.history(start="2025-03-13", end="2025-03-14", interval="1m").between_time("15:55","16:00")["Volume"]) + 
                sum(ticker.history(start="2025-03-12", end="2025-03-13", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-11", end="2025-03-12", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-10", end="2025-03-11", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-07", end="2025-03-08", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-06", end="2025-03-07", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-05", end="2025-03-06", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-04", end="2025-03-05", interval="1m").between_time("15:55","16:00")["Volume"]) +
                sum(ticker.history(start="2025-03-03", end="2025-03-04", interval="1m").between_time("15:55","16:00")["Volume"]) + 
                sum(ticker.history(start="2025-02-28", end="2025-03-01", interval="1m").between_time("15:55","16:00")["Volume"])
                #ticker.history(start="2025-03-04", end="2025-03-05", interval="1m").between_time("15:55","16:00")
            )/10

    print(ticker.get_info()["volume"]/avg10d)
    """
    #print(stock_8d_1m)
    #print()
    #stock_
    #print(stock_10d_1m.between_time("15::55", "16:00"))

    """
    stock_5d_5m = ticker.history(start=today-datetime.timedelta(days=6), end=yesterday, interval="5m")
    print(stock_5d_5m)
    avg_5d = sum(stock_5d_5m["Volume"])/5
    relativeVolumePercent = ticker.get_info()["volume"]/avg_5d
    print(relativeVolumePercent)
    """

    """
    proper volume calculation: 
        if market is closed... get volume from stock_data_yesterday
        if market is open... get volume from stock_now.iloc[-1]

        stock_now.between_time("09:30", "16:00")


    gap:
        TODO: maybe it's ok that gap = 0 when time is: 8pm < currentTime < 4am

    """


    # TODO: for news i should just make another webpage to brings u to a link of news acticles
    news = ticker.get_news()[0]["content"] # [0] means get first article
    #news["title"]
    #news["pubDate"]
    #news["displayTime"]
    #news["canonicalUrl"]
    #news["canonicalUrl"]["url"]

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
            "relativeVolume" : [relativeVolume],
            "relativeVolumePercent" : [relativeVolumePercent],
            "changeFromClose" : [changeFromClose],
            "shortInterest" : [shortInterest],
            "News" : [news["title"]]
    }

    import pandas as pd
    return pd.DataFrame(finalDataFrame)



# Fetch stock data
symbols = ["AAPL", "MSFT", "GOOG", "NVDA", "QBTS", "RDUS", "NAOV"] # TODO: fetch all stock symbols from file 
data = {} # TODO: this is data for the most active stocks

# https://yfinance-python.org/reference/index.html
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    # has key value = currentPrice, volume, regularMarketVolume, floatShares, shortRatio, previousClose, open, regularMarketOpen, regularMarketPreviousClose, 
    #print(ticker.info) 
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
