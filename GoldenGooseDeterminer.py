from NodeRequester import NodeRequester

class GoldenGooseDeterminer:
    def __init__(self):
        self.range = []
        self.highPriceDelimiter = 0
        self.lowPriceDelimiter = 0
        self.nodeRequester = NodeRequester()

    def processGoldenGeese(self, observanceObjectResultsComposite):
        self.observanceObjectResultsComposite = observanceObjectResultsComposite
        self.refreshMetrics()
        for observanceObjectResults in observanceObjectResultsComposite:
            firstResult = observanceObjectResults[0].getMarkationSet()[0]

            print(str(self.isGoldenGoose(firstResult)))

    def refreshMetrics(self):
        response = self.nodeRequester.getGoldenGooseMetrics()
        self.highPriceDelimiter = float(response["data"]["highPriceDelimiter"])
        self.lowPriceDelimiter = float(response["data"]["lowPriceDelimiter"])

        print("Look at that highPriceDelimiter wow: "+str(self.highPriceDelimiter))
        print("Look at that lowPriceDelimiter wow: "+ str(self.lowPriceDelimiter))

    def isGoldenGoose(self, stock):
        # Support for multi-metric calculations
        if(self.isWithinRange(float(stock["bid"]))):
            return True
        return False

    def isWithinRange(self, price):
        if(price >= self.highPriceDelimiter):
            return False
        if (price <= self.lowPriceDelimiter):
            return False
        return True