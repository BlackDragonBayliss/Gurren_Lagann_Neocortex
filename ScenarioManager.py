from ObservanceObject import ObservanceObject

class ScenarioManager:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def calculateMarkationResults(self,markationList):
        markationResults = []
        for markationSet in self.markationList:
            observanceObject = ObservanceObject()
            observanceObject.setMarkationSet(markationSet)
            observanceObject.setBoughtBidPrice(markationSet[0])
            observanceObject.setHighDelimter(.02)
            observanceObject.setLowDelimter(.10)

            self.calculateWinOrLose(observanceObject)

            return markationResults.append(observanceObject)

    def calculateWinOrLose(self, observanceObject):
        markationSet = observanceObject.getMarkationSet()
        stockYieldHighPriceVector = (observanceObject.getBoughtBidPrice() * observanceObject.getHighDelimiter())
        stockYieldLowPriceVector = (observanceObject.getBoughtBidPrice() * observanceObject.getLowDelimiter())

        stockYieldHighPrice = (observanceObject.getBoughtBidPrice() + stockYieldHighPriceVector)
        stockYieldLowPrice = (observanceObject.getBoughtBidPrice() - stockYieldLowPriceVector)

        index = 0

        for stock in markationSet:
            if(stock["ask"] == stockYieldHighPrice):
                observanceObject.setScenarioOutcome([1,stock.price,index])
                observanceObject.setAskSellPrice(stock.price)

            if (stock["ask"] == stockYieldLowPrice):
                observanceObject.setScenarioOutcome([0,stock.price,index])
                observanceObject.setAskSellPrice(stock["ask"])
            index += 1


    def generateObservanceObject(self):
        observanceObject = ObservanceObject()