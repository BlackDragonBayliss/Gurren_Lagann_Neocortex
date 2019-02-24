
class GoldenBearDeterminer:
    def __init__(self):
        self.range = []
        self.highPriceDelimiter = 16.00
        self.lowPriceDelimiter = 3.00

    def processGoldenBears(self, observanceObjectResultsComposite):
        self.observanceObjectResultsComposite = observanceObjectResultsComposite
        self.refreshMetrics()

        for observanceObjectResults in observanceObjectResultsComposite:
            pass

    def refreshMetrics(self):
        response = self.nodeRequester.getGoldenBearMetrics()

    def isGoldenBear(self, stock):
        # Support for multi-metric calculations
        # Support for far-fetch-mechanism
        if(self.isWithinRange(stock)):
            return True
        return False

    def isWithinRange(self, price):
        if(price >= self.highPriceDelimiter):
            return False
        if (price <= self.lowPriceDelimiter):
            return False
        return True