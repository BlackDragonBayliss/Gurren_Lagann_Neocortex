from GoldenGooseDeterminer import GoldenGooseDeterminer

class DynamaTransit:

    def __init__(self):
        self.observanceObjectResultsComposite = []

    def transferObservanceObjectResults(self, observanceObjectResultsComposite):
        self.observanceObjectResultsComposite =  observanceObjectResultsComposite
        self.goldenGooseDeterminer = GoldenGooseDeterminer()
        # Transit Buy Register decision process(threaded locally most likely)
        # Transit GoldenGoose decision process
            # Support needed for active continuous process
        goldenGooseDeterminer.processGoldenGeese(self.observanceObjectResultsComposite)