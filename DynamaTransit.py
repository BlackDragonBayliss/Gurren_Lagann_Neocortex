from GoldenBearDeterminer import GoldenBearDeterminer


class DynamaTransit:

    def __init__(self):
        self.observanceObjectResults = []

    def transferObservanceObjectResults(self, observanceObjectResults):
        self.observanceObjectResults =  observanceObjectResults
        self.goldenBearDeterminer = GoldenBearDeterminer()
        # Transit Buy Register decision process(threaded locally most likey)
        # Transit GoldenBears decision process
            # Support needed for active continuous process
        goldenBearDeterminer.processGoldenBears(self.observanceObjectResults)