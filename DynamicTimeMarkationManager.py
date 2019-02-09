from datetime import datetime, timedelta

class DynamicTimeMarkationManager:
    def __init__(self):
        self.boughtBidPrice = 0
        self.stockRangeComposite = []
        self.stockRangeContainer = []
        self.isStockRangeContainerChangeOver = True

    def determineDynamicTimeInterval(self, stockList):
        timeIntervalMatrix = []
        hourTimeDifferential = 0
        minuteTimeDifferential = 0
        secondTimeDifferential = 0
        stock1 = stockList[(len(stockList)-2)]
        stock2 = stockList[(len(stockList)-1)]
        # print(stock1)
        # print(stock2)
        hourTimeDifferential = int(stock2["hour_created"]) - int(stock1["hour_created"])
        minuteTimeDifferential = int(stock2["minute_created"]) - int(stock1["minute_created"])
        secondTimeDifferential = int(stock2["second_created"]) - int(stock1["second_created"])
        #
        if(hourTimeDifferential != 0):
            timeIntervalMatrix.append(hourTimeDifferential)
        else:
            timeIntervalMatrix.append(0)

        if (minuteTimeDifferential != 0):
            timeIntervalMatrix.append(minuteTimeDifferential)
        else:
            timeIntervalMatrix.append(0)

        if (secondTimeDifferential != 0):
            timeIntervalMatrix.append(secondTimeDifferential)
        else:
            timeIntervalMatrix.append(0)
        return timeIntervalMatrix

    def calculateDefiniteMarkationList(self, stockList):
        #Definite set entries
        intervalMatrix = self.determineDynamicTimeInterval(stockList)
        markationList = []
        return markationList
    def calculateLooseMarkationList(self, stockList):
        # intervalMatrix = self.determineDynamicTimeInterval(stockList)
        index = 0
        initialStock = stockList[(len(stockList)-1)]
        stockRangeComposite = []
        stockRangeContainer = []

        stockRangeComposite.append(stockRangeContainer)
        initialStockDateTime = datetime(2012, 9, 16, int(initialStock["hour_created"]), int(initialStock["minute_created"]), int(initialStock["second_created"]))
        nextStockDateTime = initialStockDateTime + timedelta(minutes=30)
        print("diety minute: "+str(nextStockDateTime.minute))
        # for stock in stockList:
        for stock in stockList[::-1]:
            createdStockDateTime = datetime(2012, 9, 16, int(stock["hour_created"]), int(stock["minute_created"]), int(stock["second_created"]))
            print(createdStockDateTime.minute)

            if (createdStockDateTime.minute == nextStockDateTime.minute and self.isStockRangeContainerChangeOver):
                print("success at: "+str(createdStockDateTime.minute))
                self.isStockRangeContainerChangeOver = False
                nextStockDateTime += timedelta(minutes=30)
                print("nextStockDateTime set to: "+ str(nextStockDateTime.minute))
                stockRangeContainer = []
                stockRangeComposite.append(stockRangeContainer)

            if (createdStockDateTime.minute != nextStockDateTime.minute):
                self.isStockRangeContainerChangeOver = True
            stockRangeContainer.append(stock)
            index += 1
        # print(len(stockList))
        # print(initialStock)
        # print(len(stockRangeComposite))
        # print(stockRangeComposite[3])
        return stockRangeComposite