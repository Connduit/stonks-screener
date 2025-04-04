from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetStatus, AssetClass, AssetExchange

import os



API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# TODO: add params that help get the tickers i want
def getTickers():

    # TODO: options... make multiple request_params for each AssestExchange i want (faster but more api calls), 
    # or i can have a single request_params that gets all Assets from every exchange and filter out the exchanges i don't want later (slower but less api calls)
    request_params = GetAssetsRequest(
        status=AssetStatus.ACTIVE,
        asset_class=AssetClass.US_EQUITY#,
        #exchange=AssetExchange.NASDAQ#,
        #attributes=#Comma separated values to query for more than one attribute. attrbutes are in alpacatrading.models.Asset .attributes memeber field
    )
    #latest_trades_dict = {k: v.price for k,v in latest_trades_dict.items() if v.price >= min_price and v.price <= max_price}
    all_assets = trading_client.get_all_assets(request_params)
    #all_asset_tickers = [asset.symbol for asset in all_assets]
    # TODO: figure out the difference between ARCA and NYSEARCA
    all_asset_tickers = [asset.symbol for asset in all_assets 
                         if (asset.exchange == AssetExchange.NASDAQ or asset.exchange == AssetExchange.NYSE or asset.exchange == AssetExchange.AMEX)] #and asset.tradable == True]
    #print(all_assets)
    #print(len(all_asset_tickers)) # length of data/tickers.json is 6680, but get_all_assets after being filtered returns 7940 as length
    return all_asset_tickers


if __name__ == "__main__":
    getTickers()
