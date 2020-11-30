from MongoClientObject import MongoClientObject
from StockObject import StockObject
from Mediator import Mediator
from Wallet import Wallet
import base64
import struct
import time

Uri = "mongodb+srv://dbUser:dbUserPassword123@cluster0-tefh6.azure.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass%20Community&retryWrites=true&ssl=true"
Client = MongoClientObject(Uri, "StockManager", "Test for Tobi 4")
#MicrosoftStock = StockObject("MSFT")
AppleStock = StockObject("AAPL")
Mediator = Mediator(Client)
Wallet = Wallet(10000)

#Mediator.subscribeStock(MicrosoftStock)
Mediator.subscribeStock(AppleStock)
Mediator.subscribeWallet(Wallet)

Mediator.start()

while (True):
    Wallet.buy(AppleStock, 1)
    time.sleep(2)
