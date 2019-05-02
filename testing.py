# from DataDisplayer import DataDisplayer
#
# dataDisplayer = DataDisplayer()
#
# dataDisplayer.testCase3()

# from DataFilterManager import DataFilterManager
#
# dfm = DataFilterManager()
# dfm.createStockDataSet()

# from GenerationDataMatrixFactory import GenerationDataMatrixFactory
# from DynamicTimeMarkationManager import DynamicTimeMarkationManager
#
# gdmf = GenerationDataMatrixFactory()
# dataMatrix = gdmf.createGenerationDataMatrix("bayliss", 300, [7.5,10.5], 1, 0.5, [0,0,0])
#
# dtmm = DynamicTimeMarkationManager()
#
# timeInterval = dtmm.determineDynamicTimeInterval(dataMatrix)
#
# print(timeInterval)

# testList = [[0],[1],[2],[]]
# index = 0
# for item in testList:
#     if(len(item) == 0):
#         testList.pop(index)
#     index += 1
#
# print(testList)

# from OperationCenter import OperationCenter
#
# operationCenter = OperationCenter()
#     # operation_center.process_main_process_loop()
# operationCenter.getNodeInformation(0)

# from datetime import datetime
#
# x = datetime.now()
#
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.strftime("%Y-%m-%d %H:%M:%S"))

# from TimeManager import TimeManager
#
# tm = TimeManager()
#
# print(tm.getCurrentDateObjectList())



from PerpetualTimer import PerpetualTimer


class Awesome:

    # self.internalIteration = 0

    def __init__(self):
        self.internalIteration = 0
        self.perpetualTimerSellBreachWatch = PerpetualTimer()

    def sweet(self):
        print("sweet: "+str(self.internalIteration))

        if(self.internalIteration == 2):
            print("cancelling")
            self.perpetualTimerSellBreachWatch.cancel()

        self.internalIteration += 1

    def createPepTimer(self):

        self.perpetualTimerSellBreachWatch.setup_timer_stock(2, 3000, self.sweet, 'getStockInformation')

awesome = Awesome()
awesome.createPepTimer()


# >>> from time import gmtime, strftime
# strftime("%Y-%m-%d %H:%M:%S", gmtime())
# '2009-01-05 22:14:39'