import asyncio
from threading import Thread
from NodeRequester import NodeRequester
from DataFilterManager import DataFilterManager
from DynamicTimeMarkationManager import DynamicTimeMarkationManager
from ScenarioManager import ScenarioManager

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
        scenarioManager = ScenarioManager()
        response = self.nodeRequester.getAllRecordSets("02/08/2019")
        dayList = self.dataFilterManager.createListOfDaylists(response)
        observanceObjectResultsComposite = []
        stockEntryTotalitiesList = []
        print(len(dayList[0]))
        for day in dayList[0]:
            # print(day[2])
            # print(day)
            stockEntryTotalitiesList.append(self.dataFilterManager.generateStockEntryTotalities(day))
        print(len(stockEntryTotalitiesList))
        for stockEntryTotalities in stockEntryTotalitiesList:
            markationList = self.dynamicTimeMarkationManager.calculateLooseMarkationList(stockEntryTotalities)
            observanceObjectResults = scenarioManager.calculateMarkationResults(markationList)
            observanceObjectResultsComposite.append(observanceObjectResults)
        print(len(observanceObjectResultsComposite))

        for observanceObject in observanceObjectResultsComposite[0]:
            # print(observanceObject.getBoughtBidPrice())
            print(observanceObject.getScenarioOutcome())



