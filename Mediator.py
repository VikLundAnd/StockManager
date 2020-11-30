import time
from MongoClientObject import MongoClientObject
from StockObject import StockObject
from Wallet import Wallet
import threading
import datetime

class Mediator(object):
    def __init__(self, MongoClient: MongoClientObject):
        self.client = MongoClient
        self.stockChildren: list[StockObject] = []
        self.wallets: list[Wallet] = []
        self.running = False



    def start(self):
        self.running = True
        runThread = threading.Thread(target=self.run)
        runThread.start()

    def run(self):
        while (self.running):
            self.insert()
            time.sleep(1)


    def subscribeStock(self, stock : StockObject):
        self.stockChildren.append(stock)

    def subscribeWallet(self, wallet : Wallet):
        self.wallets.append(wallet)

    def insert(self):
        dataEntry = {
            'time': datetime.datetime.utcnow(),
            'stocks': [self.stockMap(stock) for stock in self.stockChildren]
        }

        for idx, wallet in enumerate(self.wallets):
            dataEntry["wallet_" + str(idx)] = wallet.getTotal()

        self.client.insert(dataEntry)

    def stockMap(self, stock: StockObject):
        return {'name': stock.stockTicker, 'quantity': stock.quantity, 'total': stock.total}
