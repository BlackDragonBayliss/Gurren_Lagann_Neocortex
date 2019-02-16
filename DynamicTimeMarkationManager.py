from datetime import datetime, timedelta
from TimeManager import TimeManager

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


    def calculateFullRangeList(self, stockList):
        timeManager = TimeManager()
        # intervalMatrix = self.determineDynamicTimeInterval(stockList)
        index = 0
        # initialStock = stockList[(len(stockList)-1)]
        # stockRangeComposite = []
        stockRangeContainer = []
        # stockRangeComposite.append(stockRangeContainer)

        # initialStockDateTime = datetime(2012, 9, 16, int(initialStock["hour_created"]), int(initialStock["minute_created"]), int(initialStock["second_created"]))
        # nextStockDateTime = initialStockDateTime + timedelta(minutes=30)

        for stock in stockList[::-1]:
            # createdStockDateTime = datetime(2012, 9, 16, int(stock["hour_created"]), int(stock["minute_created"]), int(stock["second_created"]))

            if(timeManager.isStockWithinTradingTimeBound(stock) == False):
                break
            #
            # if (createdStockDateTime.minute == nextStockDateTime.minute and self.isStockRangeContainerChangeOver):
            #     self.isStockRangeContainerChangeOver = False
            #     stockRangeContainer = []
            #     stockRangeComposite.append(stockRangeContainer)

            # if (createdStockDateTime.minute != nextStockDateTime.minute and self.isStockRangeContainerChangeOver == False):
            #     nextStockDateTime += timedelta(minutes=30)
            #     self.isStockRangeContainerChangeOver = True

            stockRangeContainer.append(stock)
            index += 1
        return stockRangeContainer

    def calculateLooseMarkationList(self, stockList):
        timeManager = TimeManager()
        # intervalMatrix = self.determineDynamicTimeInterval(stockList)
        index = 0
        initialStock = stockList[(len(stockList)-1)]
        stockRangeComposite = []
        stockRangeContainer = []
        stockRangeComposite.append(stockRangeContainer)

        initialStockDateTime = datetime(2012, 9, 16, int(initialStock["hour_created"]), int(initialStock["minute_created"]), int(initialStock["second_created"]))
        nextStockDateTime = initialStockDateTime + timedelta(minutes=30)

        for stock in stockList[::-1]:
            createdStockDateTime = datetime(2012, 9, 16, int(stock["hour_created"]), int(stock["minute_created"]), int(stock["second_created"]))

            if(timeManager.isStockWithinTradingTimeBound(stock) == False):
                break

            if (createdStockDateTime.minute == nextStockDateTime.minute and self.isStockRangeContainerChangeOver):
                self.isStockRangeContainerChangeOver = False
                stockRangeContainer = []
                stockRangeComposite.append(stockRangeContainer)

            if (createdStockDateTime.minute != nextStockDateTime.minute and self.isStockRangeContainerChangeOver == False):
                nextStockDateTime += timedelta(minutes=30)
                self.isStockRangeContainerChangeOver = True

            stockRangeContainer.append(stock)
            index += 1

        # print(len(stockList))
        # print(initialStock)
        # print(len(stockRangeComposite))
        # print(stockRangeComposite[3])
        # stockRangeComposite = self.clearEmptyStockRangeContainerFromComposite(stockRangeComposite)

        return stockRangeComposite

    def calculateDefiniteMarkationList(self, stockList):
        #Definite set entries

        #If time is x
        timeManager = TimeManager()
        index = 0
        initialStock = stockList[(len(stockList) - 1)]
        stockRangeComposite = []
        stockRangeContainer = []
        stockRangeComposite.append(stockRangeContainer)

        initialStockDateTime = datetime(2012, 9, 16, int(initialStock["hour_created"]),
                                        int(initialStock["minute_created"]), int(initialStock["second_created"]))
        nextStockDateTime = initialStockDateTime + timedelta(minutes=30)

        for stock in stockList[::-1]:
            createdStockDateTime = datetime(2012, 9, 16, int(stock["hour_created"]), int(stock["minute_created"]),
                                            int(stock["second_created"]))

            if (timeManager.isStockWithinTradingTimeBound(stock) == False):
                break

            if (createdStockDateTime.minute == nextStockDateTime.minute and self.isStockRangeContainerChangeOver):
                self.isStockRangeContainerChangeOver = False
                stockRangeContainer = []
                stockRangeComposite.append(stockRangeContainer)

            if (
                    createdStockDateTime.minute != nextStockDateTime.minute and self.isStockRangeContainerChangeOver == False):
                nextStockDateTime += timedelta(minutes=30)
                self.isStockRangeContainerChangeOver = True

            stockRangeContainer.append(stock)
            index += 1
        markationList = []
        return markationList



    def clearEmptyStockRangeContainerFromComposite(self, stockRangeComposite):
        index = 0
        for stockRangeContainer in stockRangeComposite:
            if(len(stockRangeContainer) == 0):
                stockRangeComposite.pop(index)
            index += 1
        return stockRangeComposite

