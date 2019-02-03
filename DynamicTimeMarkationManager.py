
class DynamicTimeMarkationManager:
    def __init__(self):
        self.boughtBidPrice = 0

    def determineDynamicTimeInterval(self, listOfObjects):
        timeIntervalMatrix = []
        hourTimeDifferential = 0
        minuteTimeDifferential = 0
        secondTimeDifferential = 0
        stock1 = listOfObjects[0]
        stock2 = listOfObjects[1]

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

    def generateMarkationJSON(self):
        pass
    def calculcateMarkationJSON(self):
        pass

