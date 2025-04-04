"""
TODO: Def should probs rename this class/file

Filters class
    - takes in a dataframe (alpaca.barset.df) and generates filter attributes/fields
    - can also filter down the dataframe based on filter attributes/fields
"""

import pandas as pd

# parent class should be BaseDataSet instead of BarSet?
class Filters(pd.DataFrame):

    """
    def __init__(self, timeframe):
        #super().__init__()
        self.timeframe = timeframe # this is type alpaca.data.requests.TimeFrame
    """

    @property
    def _constructor(self):
        return Filters
    
    # add param for the time frame, or maybe add a new ?
    def addAverageVolume(self, length):
        self[f"movAvg_{length}"] = self["close"].rolling(window=length).mean()

    # add param for time of moving average (sma, ema, etc...)?
    def addMovingAvg(self, length):
        pass
