from NodeRequester import NodeRequester

class GoldenGooseDeterminer:
    def __init__(self):
        self.range = []
        self.highPriceDelimiter = 20.0
        self.lowPriceDelimiter = 2.0
        self.nodeRequester = NodeRequester()


    def refreshHardMetrics(self):
        response = self.nodeRequester.getGoldenGooseMetrics()
        self.highPriceDelimiter = float(response["data"]["highPriceDelimiter"])
        self.lowPriceDelimiter = float(response["data"]["lowPriceDelimiter"])

        print("Look at that highPriceDelimiter wow: "+str(self.highPriceDelimiter))
        print("Look at that lowPriceDelimiter wow: "+ str(self.lowPriceDelimiter))


    def processGoldenGeese(self, operationCenter, listRawGeeseMetrics):
        # self.refreshHardMetrics()

        # listFilteredGeeseMetrics = [[listRawGeeseMetrics[0],listRawGeeseMetrics[1],listRawGeeseMetrics[2],listRawGeeseMetrics[3],listRawGeeseMetrics[4]],
        #                             [listRawGeeseMetrics[5],listRawGeeseMetrics[6],listRawGeeseMetrics[7],listRawGeeseMetrics[8],listRawGeeseMetrics[9]],
        #                             [listRawGeeseMetrics[10],listRawGeeseMetrics[11],listRawGeeseMetrics[12],listRawGeeseMetrics[13], listRawGeeseMetrics[14]]]

        # print(len(listFilteredGeeseMetrics))
        listFilteredGeeseMetrics = [['HUYA', '26.710', '2.01', '0.000', '0.00'], ['BAY', '26.710', '19.01', '0.000', '0.00'], ['BAY1', '26.710', '1.01', '0.000', '0.00']]
        #First order metrics,
        listSuccessfulGooseMetrics = []
        for filteredGeeseMetrics in listFilteredGeeseMetrics:
            # print(filteredGeeseMetrics)
            if(self.isGoldenGoose(filteredGeeseMetrics)):
                listSuccessfulGooseMetrics.append(filteredGeeseMetrics)

        # print(listSuccessfulGooseMetrics)
        operationCenter.setListGoldenGeese(listSuccessfulGooseMetrics)
        print("List flying geese: "+str(operationCenter.getListGoldenGeese()))

        isChosenDetermined = self.calculateIsChosen(listSuccessfulGooseMetrics)
        # matchSuccessList if item is more worthy, decide, match raise priority.

        #Match
        #Raise priority




        print("isChosenDetermined: "+ str(isChosenDetermined))
        response = self.nodeRequester.postGoldenGooseResult(isChosenDetermined,"POP",0,"DOG",0,"MOM", 0)


    # def isGoldenGoose(self, stock):
    #     # Support for multi-metric calculations
    #     if(self.isWithinRange(float(stock["bid"]))):
    #         return True
    #     return False

    def calculateIsChosen(self,listSuccessfulGooseMetrics):
        #if list is not empy, return true
        if(len(listSuccessfulGooseMetrics) == 0):
            print(len(listSuccessfulGooseMetrics))
            return 0
        else:
            print(len(listSuccessfulGooseMetrics))
            return 1

    def isGoldenGoose(self, filteredGeeseMetrics):
        # Support for multi-metric calculations
        if(self.isWithinRange(float(filteredGeeseMetrics[2]))):
            print("GG returning true: "+ str(filteredGeeseMetrics[2]))
            return True
        return False

    def isWithinRange(self, price):
        if(price >= self.highPriceDelimiter):
            return False
        if (price <= self.lowPriceDelimiter):
            return False
        return True