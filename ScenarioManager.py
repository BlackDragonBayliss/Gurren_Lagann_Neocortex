from ObservanceObject import ObservanceObject

class ScenarioManager:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def calculateMarkationResults(self,markationList):
        markationResults = []
        # print(markationList)
        for markationSet in markationList:
            # print(markationSet)
            observanceObject = ObservanceObject()
            observanceObject.setMarkationSet(markationSet)
            observanceObject.setBoughtBidPrice(markationSet[0]["bid"])
            observanceObject.setHighDelimiter(.005)
            observanceObject.setLowDelimiter(.01)

            self.calculateWinOrLose(observanceObject)
            markationResults.append(observanceObject)
        return markationResults

    def calculateWinOrLose(self, observanceObject):
        markationSet = observanceObject.getMarkationSet()
        # print(observanceObject.getBoughtBidPrice())
        # print(observanceObject.getHighDelimiter())
        stockYieldHighPriceVector = (float(observanceObject.getBoughtBidPrice()) * float(observanceObject.getHighDelimiter()))
        stockYieldLowPriceVector = (float(observanceObject.getBoughtBidPrice()) * float(observanceObject.getLowDelimiter()))

        stockYieldHighPrice = (float(observanceObject.getBoughtBidPrice()) + stockYieldHighPriceVector)
        stockYieldLowPrice = (float(observanceObject.getBoughtBidPrice()) - stockYieldLowPriceVector)

        # print("stock purchase price: " + str(observanceObject.getBoughtBidPrice()))
        # print("stock yield high price: "+str(stockYieldHighPrice))
        # print("stock yield low price: " + str(stockYieldLowPrice))
        index = 0
        # print(markationSet)
        for stock in markationSet:
            # print(float(stock["ask"]))
            # print("high "+ str(stockYieldHighPrice))
            # print("low " + str(stockYieldLowPrice))
            if(float(stock["ask"]) >= stockYieldHighPrice):
                # print("hit ask high")
                observanceObject.setScenarioOutcome([1,stock["ask"],index])
                observanceObject.setAskSellPrice(stock["ask"])
                break
            if (float(stock["ask"]) <= stockYieldLowPrice):
                # print("hit ask low")
                observanceObject.setScenarioOutcome([0,stock["ask"],index])
                observanceObject.setAskSellPrice(stock["ask"])
                break
            if(index == (len(markationSet)-1)):
                # print("no yield found at index: " + str(index))
                pass
            index += 1


    def generateObservanceObject(self):
        observanceObject = ObservanceObject()