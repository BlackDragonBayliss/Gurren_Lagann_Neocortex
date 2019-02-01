import asyncio
from threading import Thread
import json
import requests

from NodeRequester import NodeRequester


class DataFilterManager:
    def __init__(self):

        self.nodeRequester = NodeRequester()
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
        self.isStockStoreValue = 0

    def createStockDataSet(self):
        jsonResponse = self.nodeRequester.getAllRecordSets("02/01/2019")
        self.triFilterNodeRequestProcess(jsonResponse)

    def triFilterNodeRequestProcess(self, jsonResponse):
        stockList = []
        dayList = []
        for key, value in jsonResponse.items():
            dayList.append(value)

        for day_set in dayList[0]:
            for hour_set in day_set["hour_sets"]:
                for ten_minute_set in hour_set["ten_minute_sets"]:
                    for five_minute_set in ten_minute_set["five_minute_sets"]:
                        for stock in five_minute_set["stock_sets"]:
                            stockList.append(stock)

        # print(len(stockList))
        print(stockList)

    def process_stock_store(self, stock):
        print("hit process_stock_store")
        if (self.is_data_bundle_initialization_required):
            print("Value of bool bundle: " + str(self.is_data_bundle_initialization_required))
            self.is_data_bundle_initialization_required = False
            self.process_data_initialization(stock)
            self.reset_data_initialization_value()
            return
        else:
            self.process_changeover_request()
            json = self.create_request_bundle(stock)
            print("else json: " + str(json))
            self.post_request_bundle(json)
            self.reset_process_changeover_request()

    def process_data_initialization(self, stock):
        self.dataBundleRecordSetInitiation = 1
        json = self.create_request_bundle(stock)
        # self.reset_data_initialization_value()
        print("bundle init json: " + str(json))
        self.post_request_bundle(json)

    def reset_data_initialization_value(self):
        print("reset data intialization")
        self.dataBundleRecordSetInitiation = 0

    def process_changeover_request(self):
        if (self.time_data_set_manager.calculate_hour_change()):
            self.isHourChangeoverValue = 1
            return
        if (self.time_data_set_manager.calculate_ten_minute_change()):
            self.isTenMinuteChangeoverValue = 1
            return
        if (self.time_data_set_manager.calculate_five_minute_change()):
            self.isFiveMinuteChangeoverValue = 1
            return
        self.isStockStoreValue = 1

    def reset_process_changeover_request(self):
        self.isHourChangeoverValue = 0
        self.isChangeoverValue = 0
        self.isHourChangeoverValue = 0
        self.isStockStoreValue = 0

    def create_request_bundle(self, stock):
        json = {
            "request_type": "data_manager_request_bundle",
            "isGetLatestHourSet": self.isGetLatestHourSet,
            "isGetLatestTenMinuteSet": self.isGetLatestTenMinuteSet,
            "isGetLatestFiveMinuteSet": self.isGetLatestFiveMinuteSet,
            "isGetLatestStock": self.isGetLatestStock,

            "dataBundleRecordSetInitiation": self.dataBundleRecordSetInitiation,
            "dataBundleDaySetInitiation": self.dataBundleDaySetInitiation,
            "isHourChangeover": self.isHourChangeoverValue,
            "isTenMinuteChangeover": self.isTenMinuteChangeoverValue,
            "isFiveMinuteChangeover": self.isFiveMinuteChangeoverValue,
            "isStockStore": self.isStockStoreValue,

            "stock_symbol": stock.get_sym(),
            "stock_last": stock.get_last(),
            "stock_pchg": stock.get_pchg(),
            "stock_bid": stock.get_bid(),
            "stock_ask": stock.get_ask()
        }
        return json
