import requests

# rename function
def get_polygon_tickers():
    # TODO: url to be the correct query
    url = f'https://api.polygon.io/v3/reference/tickers?apiKey=a73jrAdWlq0ke5BtQiqYNBZuE8AjZKS2'

    response = requests.get(url)
    tickers = response.json()

    print(tickers["results"])

    return tickers['results']

get_polygon_tickers()
