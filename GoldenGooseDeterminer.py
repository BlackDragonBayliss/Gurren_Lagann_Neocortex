
class GoldenGooseDeterminer:
    def __init__(self):
        self.range = []
        self.highAskDelimiter = 0
        self.lowAskDelimiter = 0

    def processGoldenGeese(self, observanceObjectResultsComposite):
        self.observanceObjectResultsComposite = observanceObjectResultsComposite
        self.refreshMetrics()
        for observanceObjectResults in observanceObjectResultsComposite:
            self.isGoldenGoose(observanceObjectResults.getFullRangeSet()[0])

    def refreshMetrics(self):
        response = self.nodeRequester.getGoldenGooseMetrics()
        self.highAskDelimiter = response["highAskDelimiter"]
        self.lowAskDelimiter = response["lowAskDelimiter"]

    def isGoldenGoose(self, stock):
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