import asyncio
from threading import Thread

class NeocortexDataRequestBundler:
    def __init__(self):
        self.sym = None
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.operation_center = None
        self.time_data_set_manager = None
        self.is_data_bundle_initialization_required = True

        self.isGetLatestHourSet = 0
        self.isGetLatestTenMinuteSet = 0
        self.isGetLatestFiveMinuteSet = 0
        self.isGetLatestStock = 0

        self.dataBundleRecordSetInitiation = 0
        self.dataBundleDaySetInitiation = 0
        self.isHourChangeoverValue = 0
        self.isTenMinuteChangeoverValue = 0
        self.isFiveMinuteChangeoverValue = 0
        self.isStockStoreValue = 1

    def process_stock_store(self, stock):
        print("hit process_stock_store")
        if (self.is_data_bundle_initialization_required):
            print("Value of bool bundle: " + str(self.is_data_bundle_initialization_required))
            self.is_data_bundle_initialization_required = False
            self.process_data_initialization(stock)
            self.reset_data_initialization_value()
            return
        else:
            json = self.create_request_bundle(stock)
            print("else json: " + str(json))
            self.post_request_bundle(json)
            self.reset_process_changeover_request()

    def process_data_initialization(self, stock):
        self.dataBundleRecordSetInitiation = 1
        json = self.create_request_bundle(stock)

        print("bundle init json: " + str(json))
        self.post_request_bundle(json)


    def createRequestBundle(self, goldenBearResults):

        json = {
            "request_type": "neocortexDataRequestBundle",
            "isRequestBundle": 1
            "dataPayload": {
            "day": date
            "isGoldenBearPresent": 0,
            "sym1": {
                "symbol": sym,
                "goldenBearStatus": {
                    "isGoldenBear": 0
                    "algorithmsUsed": "fullLength"
                }
            },
            "sym2": {
                "symbol": sym
                "goldenBearStatus": {
                    "isGoldenBear": 0
                    "algorithmsUsed": "fullLength"
                }
            }
            "sym3": {
                "symbol": sym
                "goldenBearStatus": {
                    "isGoldenBear": 0
                    "algorithmsUsed": "fullLength"
                }
            }
        }
        }
        return json

    def post_request_bundle(self, json):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(
            self.operation_center.node_manager.async_post_data_manager_request_bundle(
                json))
