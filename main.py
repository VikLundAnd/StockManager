import yfinance as yf
import sys
import matplotlib.pyplot as plot
from MongoClientObject import MongoClientObject
from StockObject import StockObject
from Mediator import Mediator


Uri = "mongodb+srv://dbUser:dbUserPassword123@cluster0-tefh6.azure.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass%20Community&retryWrites=true&ssl=true"
m = MongoClientObject(Uri, "dbName", "First try")
Stock = StockObject("MSFT")
Mediator = Mediator(m)

Mediator.subscribe(Stock)

Mediator.start()

while (True):
    Stock.buy(1)
