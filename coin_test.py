from alpaca.data.live.stock import StockDataStream 
from alpaca.data.live.crypto import CryptoDataStream
import asyncio, os

API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

crypto_stream = CryptoDataStream(API_KEY, SECRET_KEY)
stock_stream = StockDataStream(API_KEY, SECRET_KEY)



#wss_client = StockDataStream(API_KEY, SECRET_KEY)
wss_client = CryptoDataStream(API_KEY, SECRET_KEY)

async def quote_data_handler(data):
    # quote data will arrive here
    print("inside quote")
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "BTC/USD")
print("running")
wss_client.run()