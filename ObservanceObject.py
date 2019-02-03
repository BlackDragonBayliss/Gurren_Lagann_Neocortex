

class ObservanceObject:

    def __init__(self):
        self.boughtBidPrice = 0
        self.askSellPrice = 0
        self.winOrLose = 0
        self.isHighDelimiterMet = 0
        self.isLowDelimiterMet = 0
        self.buyStartTime = 0

    def setBoughtBidPrice(self, case):
        self.boughtBidPrice = case

    def setAskSellPrice(self, case):
        self.askSellPrice = case

    def determineWinOrLose(self, case):
        self.winOrLose = case

    def setIsHighDelimiterMet(self, case):
        self.isHighDelimiterMet = case

    def setIsLowDelimiterMet(self, case):
        self.isLowDelimiterMet = case

    def setBuyStartTime(self, case):
        self.buyStartTime = case