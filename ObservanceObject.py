

class ObservanceObject:

    def __init__(self):
        boughtBidPrice = 0
        askSellPrice = 0
        winOrLose = 0
        isHighDelimiterMet = 0
        isLowDelimiterMet = 0
        buyStartTime = 0

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