import time
from MongoClientObject import MongoClientObject
from StockObject import StockObject
import threading
import datetime

class Mediator(object):
    def __init__(self, MongoClient: MongoClientObject):
        self.client = MongoClient
        self.stockChildren: list[StockObject] = []
        self.running = False



    def start(self):
        self.running = True
        runThread = threading.Thread(target=self.run)
        runThread.start()

    def run(self):
        while (self.running):
            self.insert()
            time.sleep(1)


    def subscribe(self, stock : StockObject):
        self.stockChildren.append(stock)

    def insert(self):
        dataEntry = {
            'time': datetime.datetime.utcnow(),
            'data': [self.stockMap(stock) for stock in self.stockChildren]
        }

        self.client.insert(dataEntry)

    def stockMap(self, stock: StockObject):
        return {'name': stock.stockTicker, 'quantity': stock.quantity, 'total': stock.total}
