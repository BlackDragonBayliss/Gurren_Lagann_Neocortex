
class GoldenBearDeterminer:
    def __init__(self):
        self.range = []
        self.highPriceDelimiter = 16.00
        self.lowPriceDelimiter = 3.00

    def processGoldenBears(self, observanceObjectResults):
        self.observanceObjectResults = observanceObjectResults

    def isGoldenBear(self, stock):
        if(self.isWithinRange(stock)):
            return True
        return False

    def isWithinRange(self, price):
        if(price >= self.highPriceDelimiter):
            return False
        if (price <= self.lowPriceDelimiter):
            return False
        return True