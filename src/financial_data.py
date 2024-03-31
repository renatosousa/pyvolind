import pandas as pd
import quandl as ql
import MetaTrader5 as mt5
import time
import yfinance as yf

class FinancialData:
    def __init__(self, asset):
        print("Initializing...")
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()

        print("Initialized successfully.")
        self.asset = asset

    def get_price(self):
        print("Entering get_price loop...")
        while True:
            print("Getting price...")
            asset_info = mt5.symbol_info_tick(self.asset)
            if asset_info is None:
                print("symbol_info_tick() failed, error code =",mt5.last_error())
                quit()

            print("Current price of", self.asset, "is", asset_info.last, "and the volume is", asset_info.volume)
            time.sleep(1)

    def get_volume(self):
        # TODO: Implement logic to retrieve the volume of the asset
        pass

    def get_returns(self):
        # TODO: Implement logic to calculate the returns of the asset
        pass
    
if __name__ == "__main__":
    data = FinancialData("VALE3")
    data.get_price()