from ObservanceObject import ObservanceObject

class ScenarioManager:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def setMarkationList(self, markationList):
        self.markationList = markationList
    def calculateMarkationResults(self):
        markationResults = []
        for markationSet in self.markationList:
            observanceObject = ObservanceObject()
            # observanceObject.a
        # markationResults.append

    def determineWinOrLose(self, calculatedMarkationResults):
        for markationResult in calculatedMarkationResults:
            pass
    def organizeScenarioParameters(self, askList, bidList):
        self.generateObservanceObject()

    def generateObservanceObject(self):
        observanceObject = ObservanceObject()