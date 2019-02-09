

class ObservanceObject:

    def __init__(self):
        self.boughtBidPrice = 0
        self.askSellPrice = 0
        self.winOrLose = 0
        self.isHighDelimiterMet = 0
        self.isLowDelimiterMet = 0
        self.buyStartTime = 0
        self.markationSet = None
        self.scenarioOutcome = None

    def setMarkationSet(self, markationSet):
        self.markationSet = markationSet
    def getMarkationSet(self):
        return self.markationSet

    def setHighDelimiter(self, delimiter):
        self.highDelimiter = delimiter
    def getHighDelimiter(self, delimiter):
        self.highDelimiter = delimiter

    def setLowDelimiter(self, delimiter):
        self.lowDelimiter = delimiter
    def getLowDelimiter(self, delimiter):
        self.lowDelimiter = delimiter

    def setIsHighDelimiterMet(self, case):
        self.isHighDelimiterMet = case
    def setIsLowDelimiterMet(self, case):
        self.isLowDelimiterMet = case

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