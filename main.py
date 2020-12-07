from MongoClientObject import MongoClientObject
from StockObject import StockObject
from Mediator import Mediator
from Wallet import Wallet
import base64
import struct


Uri = "mongodb+srv://dbUser:dbUserPassword123@cluster0-tefh6.azure.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass%20Community&retryWrites=true&ssl=true"
Client = MongoClientObject(Uri, "StockManager", "Test for Viktor")
MicrosoftStock = StockObject("MSFT")
AppleStock = StockObject("ROKU")
Mediator = Mediator(Client)
Wallet = Wallet(5000)

Mediator.subscribeStock(MicrosoftStock)
Mediator.subscribeStock(AppleStock)
Mediator.subscribeWallet(Wallet)

Mediator.start()

while (True):
    Wallet.buy(AppleStock, 1)
