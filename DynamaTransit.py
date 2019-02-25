from GoldenBearDeterminer import GoldenBearDeterminer

class DynamaTransit:

    def __init__(self):
        self.observanceObjectResultsComposite = []

    def transferObservanceObjectResults(self, observanceObjectResultsComposite):
        self.observanceObjectResultsComposite =  observanceObjectResultsComposite
        self.goldenBearDeterminer = GoldenBearDeterminer()
        # Transit Buy Register decision process(threaded locally most likey)
        # Transit GoldenBears decision process
            # Support needed for active continuous process
        goldenBearDeterminer.processGoldenBears(self.observanceObjectResultsComposite)