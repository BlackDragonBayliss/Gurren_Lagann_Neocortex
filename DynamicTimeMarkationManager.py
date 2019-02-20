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


    def calculateFullRangeMarkationList(self, stockList, chronDict, timeManager):
        #[stock,index]
        beginWatchListResult = chronDict["chronBeginWatch"]
        endWatchListResult = chronDict["chronEndWatch"]

        desiredTimeInterval = 10
        # timeManager = timerManager
        index = 0
        initialStock = beginWatchListResult[0]
        # print("begin watch sanity: " + str(initialStock))

        stockRangeComposite = []
        stockRangeContainer = []
        stockRangeComposite.append(stockRangeContainer)

        beginIterationStockDateTime = datetime(2012, 9, 16, int(initialStock["hour_created"]),
                                        int(initialStock["minute_created"]), int(initialStock["second_created"]))
        # print(initialStockDateTime.minute)
        # nextStockDateTime = beginIterationStockDateTime + timedelta(minutes=desiredTimeInterval)

        tenMinuteSetComposite = []
        tenMinuteSet = []
        # entryComposite.append(tenMinuteSet)
        # print(str(stockList[0]["minute_created"]) + " hour: "+ str(stockList[0]["hour_created"]))
        #
        # lastIndexMinute = str(stockList[(len(stockList)-1)]["minute_created"])
        # print(lastIndexMinute)
        # lastIndexHour = str(stockList[(len(stockList) - 1)]["hour_created"])
        # print(lastIndexHour)
        # print(str(stockList[len(stockList-1)]["minute_created"]) +
        #       " hour: " + str(stockList[len(stockList-1)]["hour_created"]))


        # for tenMinuteSet in tenMinuteSetComposite:
        for stock in stockList:
            createdStockDateTime = datetime(2012, 9, 16, int(stock["hour_created"]), int(stock["minute_created"]),
                                            int(stock["second_created"]))
            # print("createdStockDateTime.minute: "+str(createdStockDateTime.minute) +
            # " beginIterationStockDateTime.minute: "+ str(beginIterationStockDateTime.minute)+
            # " self.isStockRangeContainerChangeOver: " +str(self.isStockRangeContainerChangeOver))

            if(createdStockDateTime.minute == beginIterationStockDateTime.minute and self.isStockRangeContainerChangeOver):
                print("adding entryList")
                tenMinuteSetComposite.append([createdStockDateTime])
                self.isStockRangeContainerChangeOver = False

            if (createdStockDateTime.minute != beginIterationStockDateTime.minute and self.isStockRangeContainerChangeOver == False):
                print("self.isStockRangeContainerChangeOver "+str(self.isStockRangeContainerChangeOver))
                # nextStockDateTime += timedelta(minutes=desiredTimeInterval)
                print("beginIterationStockDateTime "+ str(beginIterationStockDateTime))
                beginIterationStockDateTime = beginIterationStockDateTime + timedelta(minutes=desiredTimeInterval)
                # print("internal minute mile: "+ str(beginIterationStockDateTime))
                self.isStockRangeContainerChangeOver = True





            # if(len(tenMinuteSetComposite) >=50):
            #     print("breaking")
            #     break


        print(len(tenMinuteSetComposite))
        # halfEntryCompositeLength = int(len(entryComposite) / 2)
        # # print(halfEntryCompositeLength)
        # newEntryComposite = entryComposite[0:halfEntryCompositeLength]
        # print(len(newEntryComposite))
        # print(newEntryComposite)



        # for entryList in newEntryComposite:
            # print("Second for: " + str(entryList[0].minute))

        # print(newEntryComposite)
        # for entryList in entryComposite:
            # print("Second for: "+str(entryList[0].minute)

        # for stock in stockList:
        #     createdStockDateTime = datetime(2012, 9, 16, int(stock["hour_created"]), int(stock["minute_created"]),
        #                                     int(stock["second_created"]))
        # # Catch if stock is ever out of trading hours
        #     if (timeManager.isStockWithinTradingTimeBound(stock) == False):
        #         break
        # #
        #     if (createdStockDateTime.minute == nextStockDateTime.minute and self.isStockRangeContainerChangeOver):
        #         self.isStockRangeContainerChangeOver = False
        #         stockRangeContainer = []
        #         stockRangeComposite.append(stockRangeContainer)
        # #
        #     if (createdStockDateTime.minute != nextStockDateTime.minute and self.isStockRangeContainerChangeOver == False):
        #         nextStockDateTime += timedelta(minutes=desiredTimeInterval)
        #         self.isStockRangeContainerChangeOver = True
        #
        #     stockRangeContainer.append(stock)
        #     index += 1
        return stockRangeComposite

    def clearEmptyStockRangeContainerFromComposite(self, stockRangeComposite):
        index = 0
        for stockRangeContainer in stockRangeComposite:
            if(len(stockRangeContainer) == 0):
                stockRangeComposite.pop(index)
            index += 1
        return stockRangeComposite

