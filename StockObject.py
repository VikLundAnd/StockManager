import time
from MongoClientObject import MongoClientObject
import threading
import requests
import websockets
import asyncio
import base64
import struct


class StockObject(object):
    def __init__(self, stockTicker):
        self.quantity = 0
        self.total = 0
        self.stockTicker = stockTicker
        self.assetPrice: float = 0
        self.running = False

        self.uri = "wss://streamer.finance.yahoo.com/"

        mainLoopThread = threading.Thread(target=self.between_callback)
        mainLoopThread.start()
        while(not self.running):
            pass

    def buy(self, quantity: int) -> float:
        self.quantity = self.quantity + quantity
        price = self.getPrice(quantity, self.assetPrice)
        self.total = self.getPrice(self.quantity,self.assetPrice)
        return -price

    def sell(self, quantity: int):
        self.quantity = self.quantity - quantity
        price = self.getPrice(quantity, self.assetPrice)
        self.total = self.getPrice(self.quantity,self.assetPrice)
        return price

    async def loop(self):
        async with websockets.connect(self.uri) as websocket:
            await websocket.send('{"subscribe":["' + self.stockTicker + '"]}')
            await self.update(websocket)
            self.running = True
            while (self.running):
                await self.update(websocket)
                time.sleep(1)

    async def update(self, websocket):
        self.assetPrice = await self.getAssetPrice(websocket)
        self.total = self.getPrice(self.quantity, self.assetPrice)

    def getPrice(self, quantity: int, assetPrice):
        return quantity * assetPrice

    async def getAssetPrice(self, websocket):
        received = await websocket.recv()
        decoded = base64.b64decode(received)
        bytes = decoded[7:11]
        data = struct.unpack('f', bytes)[0]
        return data

    def between_callback(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(self.loop())
        loop.close()
