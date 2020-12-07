from StockObject import StockObject

class Wallet(object):
    def __init__(self, wallet):
        self.wallet : float = wallet

    def getTotal(self):
        return self.wallet

    def buy(self, stock: StockObject, quantity: int):
        print("buying stock")
        if self.wallet - stock.getPrice(quantity, stock.assetPrice) < 0:
            print("Insufficient funds!")
        else:
            self.wallet += stock.buy(quantity)

    def sell(self, stock: StockObject, quantity: int):
        self.wallet += stock.sell(quantity)
