from GoldenGooseDeterminer import GoldenGooseDeterminer

class DynamaTransit:

    def __init__(self):
        self.observanceObjectResultsComposite = []

    def goldenGooseProcessIntake(self, operationCenter, listOfMetrics):
        self.goldenGooseDeterminer = GoldenGooseDeterminer()
        self.goldenGooseDeterminer.processGoldenGeese(operationCenter, listOfMetrics)


    def transferObservanceObjectResults(self, data):
        self.goldenGooseDeterminer = GoldenGooseDeterminer()
        # Transit GoldenGoose decision process
            # Support needed for active continuous process
        self.goldenGooseDeterminer.processGoldenGeese(data)

