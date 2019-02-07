from datetime import datetime, timedelta

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
        index = 0
        initialStock = stockList[0]
        indexRange = []
        stockFound = None
        initialStockDateTime = datetime(2012, 9, 16, initialStock.hour_created, initialStock.minute_created, initialStock.second_created)
        nextStockDateTime = initialStockDateTime + timedelta(minutes=30)
        for stock in stockList:
            if(index == 0):
                pass
            if(stock.minute_created == nextStockDateTime.minute):
                # nextStockDateTime
                indexRange.append(index)
                stockFound = stock
            index += 1
        # Get splice
        print(indexRange)
        print(stockFound)


        markationList = []
        return markationList