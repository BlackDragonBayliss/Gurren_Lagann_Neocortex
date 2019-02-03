import random


class GenerationDataMatrixFactory:
    def __init__(self):
        self.stockGenerationDataPool = []
        self.currentTimeMatrix = [8, 30, 0]
        self.hourIncrement = 0
        self.minuteIncrement = 0
        self.secondIncrement = 0


    def createGenerationDataMatrix(self, sym, quantity, range, bidDecrement, askIncrement, timeIntervalMatrix):
        generationDataMatrix = []
        index = 0
        self.setupTimeInterval(timeIntervalMatrix)
        while (index <= quantity):
            bidPrice = (self.generateFloatsInRange(range[0], range[1]) - bidDecrement)
            askPrice = (self.generateFloatsInRange(range[0], range[1]) + askIncrement)
            self.incrementCurrentTimeMatrix()
            timeMatrix = self.getCurrentTimeMatrix()
            stockData = [sym, quantity, bidPrice, askPrice, timeMatrix]

            generationDataMatrix.append(stockData)
            index += 1
        self.resetCurrentTimeMatrix()
        return generationDataMatrix

    def setupTimeInterval(self, timeIntervalMatrix):
        self.hourIncrement = timeIntervalMatrix[0]
        self.minuteIncrement = timeIntervalMatrix[1]
        self.secondIncrement = timeIntervalMatrix[2]

    def incrementCurrentTimeMatrix(self):
        dataTimeMatrix = self.getCurrentTimeMatrix()
        updatedTimeMatrix = []
        hour = dataTimeMatrix[0] + self.hourIncrement
        minute = dataTimeMatrix[1] + self.minuteIncrement
        second = dataTimeMatrix[2] + self.secondIncrement
        if (second == 60):
            second = 0
            minute += 1
        if (minute == 60):
            minute = 0
            hour += 1
        updatedTimeMatrix.append(hour)
        updatedTimeMatrix.append(minute)
        updatedTimeMatrix.append(second)
        self.setCurrentTimeMatrix(updatedTimeMatrix)

    def resetCurrentTimeMatrix(self):
        self.currentTimeMatrix = [8, 30, 0]

    def generateFloatsInRange(self, startingFloat, endingFloat):
        return random.uniform(1.5, 1.9)

    def getCurrentTimeMatrix(self):
        return self.currentTimeMatrix
    def setCurrentTimeMatrix(self, timeMatrix):
        self.currentTimeMatrix = timeMatrix