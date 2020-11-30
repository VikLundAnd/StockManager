import time
from MongoClientObject import MongoClientObject
import threading
import requests


class StockObject(object):
    def __init__(self, stockTicker):
        self.quantity = 0
        self.total = 0
        self.stockTicker = stockTicker

        mainLoopThread = threading.Thread(target=self.loop)
        mainLoopThread.start()

    def buy(self, quantity):
        self.quantity = self.quantity + quantity
        return -self.getPrice(quantity, self.getAssetPrice())

    def sell(self, quantity):
        self.quantity = self.quantity - quantity
        return self.getPrice(quantity, self.getAssetPrice())

    def loop(self):
        while (True):
            self.update()
            time.sleep(1)

    def update(self):
        self.total = self.getPrice(self.quantity, self.getAssetPrice())

    def getPrice(self, quantity, assetPrice):
        return quantity * assetPrice

    def getAssetPrice(self):
        url = "https://query1.finance.yahoo.com/v8/finance/chart/" + self.stockTicker
        response = requests.get(url)
        print(response.json()['chart']['result'][0]['meta']['regularMarketPrice'])
        return response.json()['chart']['result'][0]['meta']['regularMarketPrice']
