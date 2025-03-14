import requests


####
# https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs#nasdaq

###
# https://datahub.io/core/nasdaq-listings
###
# https://datahub.io/core/nyse-other-listings


####
# Common Stock, Depositary Receipt, ETF
# NYSE ARCA, NASDAQ, NYSE

####


# NYSE = XNYS
# NASDAQ = XNAS

# TODO: use this instead??
#     : https://stockanalysis.com/stocks/
#     : https://stockanalysis.com/list/exchanges/

# rename function
def get_polygon_tickers():
    apiKey = "a73jrAdWlq0ke5BtQiqYNBZuE8AjZKS2"
    # TODO: url to be the correct query
    url = f"https://api.polygon.io/v3/reference/tickers?apiKey={apiKey}"
    url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&limit=1000?apiKey={apiKey}"
    url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&limit=1000?apiKey=a73jrAdWlq0ke5BtQiqYNBZuE8AjZKS2"

    response = requests.get(url)
    tickers = response.json()

    print(tickers.keys())

    print(tickers["status"])
    print(tickers["request_id"])
    print(tickers["error"])

    
    print(tickers["results"])

    return tickers['results']

data = get_polygon_tickers()

"""
with open("ticker_symbols.json", "w+") as file:
    json.dump(data, file, indent=4)
"""
