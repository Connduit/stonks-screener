# TODO

### NOTES

    - right now there's no reason to have google sheets stuff if im making a json file to then upload to google sheets. maybe this will be more useful it im directly uploading to drive instead of making any json file.
    - RelativeVolume (TradingView) = volume/ta.sma(volume[1], 10)
        - meaning get the average of 10 volume not including the current day tho
        - chatgpt formula:
	        RV = (current volume of in-progress candle)/(average volume for time period)
		     * (time elapsed)/(time remaining)
	- yfinance sucks at getting news... maybe use alpaca-py? data/news might be delayed by 15 mins tho
 	- auto commit update yml run for 9am isn't working 
  	- I HAVE A FEELING RVOL5MIN uses RVOL at TIME...............
   	- SUM OF VOLUME AT TIME X FOR N DAYS (NOT INCLUDING THE CURRENT DAY)
    		- x = volume[1] at TIME... then volume/x == ANSWER


### Where I Left Off

    - stock data isn't being stored in google sheet

    

### Future Ideas
    
    - use go, svelte, js, ts, css, html, and wasm files when using live data from a paid api
    - maybe use azure web app?

### Stuff to implemented for different scanners
    - https://finviz.com/help/screener.ashx

### Long Term
	- switch from python to npm
 	- use paid api
  	- dont use paid API, and just scape web data
   	- TODO: if i continue to use python where i save off json... i should precalculate averages and stuff (during non trading hours, i.e., EOD)
    		- Example: 
      			- 10d volume averages. moving average at historical date/time X. (Should probs use alpaca for historical stuff)
			- all intraday stuff will have to be calculated on the fly (probably with apis)

### Links

    - possible sources:
        https://github.com/kacperadach/ichimoku_screener/
        https://github.com/pranjal-joshi/Screeni-py/
        https://github.com/devfinwiz/Stock_Screeners_Raw
        https://github.com/asafravid/sss
        

    - possible apis:
        https://site.financialmodelingprep.com/developer/docs/stable
        https://polygon.io/
        https://finnhub.io/dashboard
		https://site.financialmodelingprep.com/top-stock-gainers
 		https://www.tiingo.com/documentation/fundamentals
  		IMPORTANT: https://www.marketbeat.com/market-data/trading-halts/
    				https://www.nasdaqtrader.com/Trader.aspx?id=TradeHalts

    - possible inspiration
        https://stockfetcher.com/#
        https://finviz.com/
        https://www.chartmill.com/stock/stock-screener
        https://www.stockrover.com/screening-strategies/
        https://youtu.be/9iowl419L4s?t=113
        https://youtu.be/7RbjGk9eNJU?t=758
		https://media.warriortrading.com/2021/03/17110245/GapScanner.png
 		https://media.warriortrading.com/2020/12/10070038/APVO-1-Scanners-and-P-L.png

