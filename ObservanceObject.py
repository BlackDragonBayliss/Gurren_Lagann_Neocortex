

class ObservanceObject:

    def __init__(self):
        self.fullRangeSet = None
        self.markationSet = None

        self.highDelimiter = None
        self.lowDelimiter = None
        self.isHighDelimiterMet = 0
        self.isLowDelimiterMet = 0

        self.boughtBidPrice = 0
        self.askSellPrice = 0
        self.scenarioOutcome = None

        self.winOrLose = 0
        self.buyStartTime = 0

    def setFullRangeSet(self,fullRangeSet):
        self.fullRangeSet = fullRangeSet
    def getFullRangeSet(self):
        return self.fullRangeSet

    def setMarkationSet(self, markationSet):
        self.markationSet = markationSet
    def getMarkationSet(self):
        return self.markationSet

    def setHighDelimiter(self, delimiter):
        self.highDelimiter = delimiter
    def getHighDelimiter(self):
        return self.highDelimiter

    def setLowDelimiter(self, delimiter):
        self.lowDelimiter = delimiter
    def getLowDelimiter(self, ):
        return self.lowDelimiter

    def setIsHighDelimiterMet(self, case):
        self.isHighDelimiterMet = case
    def getIsHighDelimiterMet(self):
        return self.isHighDelimiterMet

    def setIsLowDelimiterMet(self, case):
        self.isLowDelimiterMet = case
    def getIsLowDelimiterMet(self):
        return self.isLowDelimiterMet

    def setBoughtBidPrice(self, case):
        self.boughtBidPrice = case
    def getBoughtBidPrice(self):
        return self.boughtBidPrice

    def setAskSellPrice(self, case):
        self.askSellPrice = case
    def getAskSellPrice(self):
        return self.askSellPrice

    def setScenarioOutcome(self, scenarioOutcome):
        self.scenarioOutcome = scenarioOutcome
    def getScenarioOutcome(self):
        return self.scenarioOutcome

    def setBuyStartTime(self, case):
        self.buyStartTime = case