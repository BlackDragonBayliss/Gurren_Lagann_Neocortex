
class GoldenGooseDeterminer:
    def __init__(self):
        self.range = []
        self.highAskDelimiter = 16.00
        self.lowAskDelimiter = 3.00

    def processGoldenGeese(self, observanceObjectResultsComposite):
        self.observanceObjectResultsComposite = observanceObjectResultsComposite
        self.refreshMetrics()

        for observanceObjectResults in observanceObjectResultsComposite:
            pass

    def refreshMetrics(self):
        response = self.nodeRequester.getGoldenGooseMetrics()
        self.highAskDelimiter = response["highAskDelimiter"]
        self.lowAskDelimiter = response["lowAskDelimiter"]

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