import asyncio
from threading import Thread
from NodeRequester import NodeRequester
from DataFilterManager import DataFilterManager
from DynamicTimeMarkationManager import DynamicTimeMarkationManager

class OperationCenter:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.nodeRequester = NodeRequester()
        self.dataFilterManager = DataFilterManager()
        self.dynamicTimeMarkationManager = DynamicTimeMarkationManager()

    def process_main_process_loop(self):
        self.main_process_loop()

    def main_process_loop(self):
        self.perpetual_timer.setup_timer_stock(1, 1000000, self.main_loop, 'main_process_loop')

    def main_loop(self):
        #Update Data_Decision_Process_Action_Manager with chosen stocks
        self.event_trigger_top_stock_gather_process_phase_one()
        self.is_condition_top_stock_pull_gather = True

    def getNodeInformation(self):
        response = self.nodeRequester.getAllRecordSets()
        dayList = self.dataFilterManager.createListOfDaylists(response)
        stockEntryTotalitiesList = []
        for day in dayList:
            stockEntryTotalitiesList.append(self.dataFilterManager.generateStockEntryTotalities(day))
        print(stockEntryTotalitiesList[0])

        # self.dynamicTimeMarkationManager
        # self.calculateLooseMarkationList
