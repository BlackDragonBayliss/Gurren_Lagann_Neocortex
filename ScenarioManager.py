from ObservanceObject import ObservanceObject

class ScenarioManager:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def createScenario(self):
        pass


    def determineWinOrLose(self, calculatedMarkationResults):
        for markationResult in calculatedMarkationResults:
            pass
    def organizeScenarioParameters(self, askList, bidList):
        self.generateObservanceObject()

    def generateObservanceObject(self):
        observanceObject = ObservanceObject()
