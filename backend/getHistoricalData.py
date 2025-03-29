from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, TimeFrame



api_key = "PKVYRNH1J4SJ7WUIGHBF"
api_secret = "LQ7H9QSaFU3Xx6zzL3fHwN9NOlBN8XmloVd9R1mS"

trading_client = TradingClient(api_key, api_secret, paper=True)
data_client = StockHistoricalDataClient(api_key, api_secret)

stocks = ["NVDA", "QBTS"]

from datetime import datetime, timedelta
end_time = datetime.now().date()
#start_time = 
request_params = StockBarsRequest(symbol_or_symbols="NVDA", timeframe=TimeFrame.Minute,)


from tradingview_screener import Query, col


all_stocks = Query().get_scanner_data()
print(all_stocks)

my_query = (Query()
 .select(
     'name',
     'description',
     'logoid',
     'update_mode',
     'type',
     'typespecs',
     'market_cap_basic',
     'fundamental_currency_code',
     'close',
     'pricescale',
     'minmov',
     'fractional',
     'minmove2',
     'currency',
     'change',
     'volume',
     'price_earnings_ttm',
     'earnings_per_share_diluted_ttm',
     'earnings_per_share_diluted_yoy_growth_ttm',
     'dividends_yield_current',
     'sector.tr',
     'sector',
     'market',
     'recommendation_mark',
     'relative_volume_10d_calc',
 )
 .where(
     col('exchange').isin(['AMEX', 'CBOE', 'NASDAQ', 'NYSE']),
     col('is_primary') == True,
     col('typespecs').has('common'),
     col('typespecs').has_none_of('preferred'),
     col('type') == 'stock',
 )
 .order_by('name', ascending=True, nulls_first=False)
 .limit(100)
 .set_markets('america')
 .set_property('preset', 'all_stocks')
 .set_property('symbols', {'query': {'types': ['stock', 'fund', 'dr', 'structured']}}))

print(my_query.get_scanner_data())