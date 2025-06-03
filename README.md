# stonks-screener

### Setup
downloadTickers.py
    
    - Download text file of securities through nasdaq ftp at https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs
    - Saves off two text files, "nasdaqlisted.txt" (securities from the nasdaq exchange) and "otherlisted.txt" (securities from other exchanges)

parseTickers.py
    
    - Filters out securities that are duplicates, tests, or are simply unwanted
    - TODO: Add option to pass in parameters for what contents I want to filter by instead of hard coding what filter options
    - Saves off a list of all tickers that passed the filters in a json file called tickers.json

getCurrentData.py
    
    - Attempts to get current (intraday) stock data for all the stocks that exist in tickers.json

getHistoricalData.py
    
    - Attemps to get historical stock data for all the stocks that exist in tickers.json

getTickers_viaAlpaca.py
    
    - Attempts to get all tickers through the alpaca api; however, it doesn't have as many filter options as parseTickers.py 

getData_alpaca.py
    
    - Attempts to get stock data for provided tickers through alpaca api. (This file is still a work in progress)


### Limitations

    https://docs.alpaca.markets/docs/about-market-data-api#subscription-plans
