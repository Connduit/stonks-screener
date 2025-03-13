import requests

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

    response = requests.get(url)
    tickers = response.json()

    print(tickers.keys())

    print(tickers["results"])

    return tickers['results']

data = get_polygon_tickers()

"""
with open("ticker_symbols.json", "w+") as file:
    json.dump(data, file, indent=4)
"""
