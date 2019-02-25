from NodeRequester import NodeRequester

class DynamaMetricsStoreManager:
    def __init__(self):
        self.nodeRequester = NodeRequester

    def storeMetrics(self):
        pass

    def createCustomStore(self):
        pass

    def retrieveStore(self,registrationID):
        pass

    def retrieveGoldenBearMetrics(self):
        self.nodeRequester.getGoldenGooseMetrics()