import asyncio
from threading import Thread
from NodeRequester import NodeRequester
from DataFilterManager import DataFilterManager
from DynamicTimeMarkationManager import DynamicTimeMarkationManager
from ScenarioManager import ScenarioManager
from DataDisplayer import DataDisplayer

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

    def getNodeInformation(self, caseCalculationType):
        scenarioManager = ScenarioManager()
        response = self.nodeRequester.getAllRecordSets("02/08/2019")
        dayList = self.dataFilterManager.createListOfDaylists(response)
        observanceObjectResultsComposite = []
        stockEntryTotalitiesList = []
        for day in dayList[0]:
            stockEntryTotalitiesList.append(self.dataFilterManager.generateStockEntryTotalities(day))
        # print(len(stockEntryTotalitiesList))

        if (caseCalculationType == 0):
            for stockEntryTotalities in stockEntryTotalitiesList:
                dataDisplayer = DataDisplayer()
                fullRangeStockList = self.dynamicTimeMarkationManager.calculateFullRangeList(stockEntryTotalities)
                dataDisplayer.testCase3(fullRangeStockList)
                break

            #     observanceObjectResult = scenarioManager.calculateFullRangeResults(fullRangeStockList)
            #     observanceObjectResultsComposite.append(observanceObjectResult)
            #
            # for observanceObjectResult in observanceObjectResultsComposite:
            #     print(observanceObjectResult.getScenarioOutcome())

        if (caseCalculationType == 1):
            for stockEntryTotalities in stockEntryTotalitiesList:
                markationStockRangeComposite = self.dynamicTimeMarkationManager.calculateLooseMarkationList(stockEntryTotalities)
                observanceObjectResults = scenarioManager.calculateMarkationResults(markationStockRangeComposite)
                observanceObjectResultsComposite.append(observanceObjectResults)

            for observanceObjectResultsList in observanceObjectResultsComposite:
                for observanceObject in observanceObjectResultsList:
                    print(observanceObject.getScenarioOutcome())

        # print(len(markationStockRangeComposite))
        # print(markationStockRangeComposite[1])
        # print(markationStockRangeComposite[0][0])
        # print(markationStockRangeComposite[16][0])

        # print(len(observanceObjectResultsComposite))





