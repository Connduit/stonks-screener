"""
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

    
    #print(tickers["results"])

    #return tickers['results']

data = get_polygon_tickers()
#with open("ticker_symbols.json", "w+") as file:
    #json.dump(data, file, indent=4)
"""
# http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs

# NASDAQ-Listed Securities
#  File Name:      nasdaqlisted.txt
#  FTP Directory:  ftp://ftp.nasdaqtrader.com/symboldirectory
#   Field Name      Definition
#   Symbol 	        The one to four or five character identifier for each
#                   NASDAQ-listed security.
#   Security Name   Company issuing the security.
#   Market Category The category assigned to the issue by NASDAQ based on
#                   Listing Requirements. Values:
#     Q = NASDAQ Global Select MarketSM
#     G = NASDAQ Global MarketSM
#     S = NASDAQ Capital Market
#   Test Issue      Indicates whether or not it is a test security (y/n).
#   Finan. Status   Indicates when an issuer has failed to submit its
#                   regulatory filings on a timely basis, has failed to meet
#                   NASDAQ's continuing listing standards, and/or has filed for
#                   bankruptcy. Values include:
#       D = Deficient: Issuer Failed to Meet NASDAQ Continued Listing rqmts
#       E = Delinquent: Issuer Missed Regulatory Filing Deadline
#       Q = Bankrupt: Issuer Has Filed for Bankruptcy
#       N = Normal (Default): Issuer Is NOT Deficient, Delinquent, or Bankrupt.
#       G = Deficient and Bankrupt
#       H = Deficient and Delinquent
#       J = Delinquent and Bankrupt
#       K = Deficient, Delinquent, and Bankrupt
#   Round Lot       Indicates the number of shares that make up a round lot for
#                   the given security.
#   ETF             Indicates whether it is an exchange traded fund (y/n).
#   NextShares      Indicates whether it is a NextShare fund (y/n).
#   File Creation:  The last row of each Symbol Directory text file contains a
#                   timestamp that reports the File Creation Time. The file
#                   creation time is based on when NASDAQ Trader generates the
#                   file and can be used to determine the timeliness of the
#                   associated data. The row contains the words File Creation
#                   Time followed by mmddyyyyhhmm as the first field, followed
#                   by all delimiters to round out the row. An example:
#                   File Creation Time: 1217200717:03|||||

# Header
# Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size|ETF|NextShares
# Values separated by pipes ('|') and rows separated be newlines

import ftplib
import os
import datetime
from pprint import pprint

try:
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
except NameError:
    DIR_PATH = os.getcwd()  # for colab

with ftplib.FTP('ftp.nasdaqtrader.com') as ftp:
    directory = 'symboldirectory'
    filename = 'nasdaqlisted.txt'

    try:
        ftp.login()
        ftp.cwd(f'/{directory}/')
        with open(f'{DIR_PATH}/{filename}', 'wb') as f:
            res = ftp.retrbinary("RETR " + filename, f.write)
            if not res.startswith('226 Transfer complete'):
                print('Download failed')
                if os.path.isfile(f'{DIR_PATH}/{filename}'):
                    os.remove(f'{DIR_PATH}/{filename}')

    except ftplib.all_errors as e:
        print('FTP error:', e)
        if os.path.isfile(f'{DIR_PATH}/{filename}'):
            os.remove(f'{DIR_PATH}/{filename}')

# read into a dictionary
with open(f'{DIR_PATH}/{filename}', 'r') as f:
    content = f.read().splitlines()

header = content[0].split('|')
date = content[-1].split('|')[0][:]
date = date[len('File Creation Time: '):]
date = datetime.datetime.strptime(date, '%m%d%Y%H:%M')
content = content[1:-1]
print(date)
print(header)

securities = []
for c in content:
    c = c.split('|')
    security = {}
    for i in range(len(c)):
        security[header[i]] = c[i]
    securities.append(security)
pprint(securities)
