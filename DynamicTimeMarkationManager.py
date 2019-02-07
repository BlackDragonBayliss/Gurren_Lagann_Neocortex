
class DynamicTimeMarkationManager:
    def __init__(self):
        self.boughtBidPrice = 0

    def determineDynamicTimeInterval(self, stockList):
        timeIntervalMatrix = []
        hourTimeDifferential = 0
        minuteTimeDifferential = 0
        secondTimeDifferential = 0
        stock1 = stockList[0]
        stock2 = stockList[1]

        timeMatrix1 = stock1[4] # Format [8,30,0]
        timeMatrix2 = stock2[4]

        hourTimeDifferential = timeMatrix2[0] - timeMatrix1[0]
        minuteTimeDifferential = timeMatrix2[1] - timeMatrix1[1]
        secondTimeDifferential = timeMatrix2[2] - timeMatrix1[2]

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
        #First entry start point
        intervalMatrix = self.determineDynamicTimeInterval(stockList)
        #Obtain matrix interval
        # Locate each stock price at interval.
        # We have time in [hour,minute,second]
        index = 0
        initialStock = stockList[0]
        initialStockTime = []

        # initialStockTime.append(initialStock.hour_created)
        # initialStockTime.append(initialStock.minute_created)
        # initialStockTime.append(initialStock.second_created)

        # nextHour = initialStockTime[0]

        nextMinute = initialStock.minute_created + intervalMatrix[1]


        # nextMinute
        # nextTimeIntervalToFind = initialMinute +

        for stock in stockList:
            if(index == 0):
                initialStockTime.append(stock.hour_created)
                initialStockTime.append(stock.minute_created)
                initialStockTime.append(stock.second_created)

            if():
                pass




        markationList = []
        return markationList