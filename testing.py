# from DataDisplayer import DataDisplayer
#
# dataDisplayer = DataDisplayer()
#
# dataDisplayer.testCase3()

# from DataFilterManager import DataFilterManager
#
# dfm = DataFilterManager()
# dfm.createStockDataSet()


from GenerationDataMatrixFactory import GenerationDataMatrixFactory

gdmf = GenerationDataMatrixFactory()
dataMatrix = gdmf.createGenerationDataMatrix("bayliss", 300, [7.5,10.5], 1, 0.5)

print(dataMatrix)