import asyncio
from threading import Thread
from NodeRequester import NodeRequester
from DataFilterManager import DataFilterManager
from DynamicTimeMarkationManager import DynamicTimeMarkationManager
from ScenarioManager import ScenarioManager
from DataDisplayer import DataDisplayer
from TimeManager import TimeManager
from DynamaTransit import DynamaTransit

class OperationCenter:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.nodeRequester = NodeRequester()
        self.dataFilterManager = DataFilterManager()
        self.dynamicTimeMarkationManager = DynamicTimeMarkationManager()
        self.timeManager = TimeManager()
        self.dynamaTransit = DynamaTransit()

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
        # response = self.nodeRequester.getAllRecordSets("02/08/2019")
        response = self.nodeRequester.getAllRecordSets("02/21/2019")
        dayList = self.dataFilterManager.createListOfDaylists(response)
        observanceObjectResultsComposite = []
        stockEntryTotalitiesList = []
        for day in dayList[0]:
            stockEntryTotalitiesList.append(self.dataFilterManager.generateStockEntryTotalities(day))
        # print(len(stockEntryTotalitiesList))

        if (caseCalculationType == 0):
            for stockEntryTotalities in stockEntryTotalitiesList:
                fullRangeStockList = self.dynamicTimeMarkationManager.calculateFullRangeList(stockEntryTotalities)
                observanceObjectResult = scenarioManager.calculateFullRangeResults(fullRangeStockList)
                observanceObjectResultsComposite.append(observanceObjectResult)

            for observanceObjectResult in observanceObjectResultsComposite:
                print(observanceObjectResult.getScenarioOutcome())

        if (caseCalculationType == 1):
            for stockEntryTotalities in stockEntryTotalitiesList:
                markationStockRangeComposite = self.dynamicTimeMarkationManager.calculateLooseMarkationList(stockEntryTotalities)
                observanceObjectResults = scenarioManager.calculateMarkationResults(markationStockRangeComposite)
                observanceObjectResultsComposite.append(observanceObjectResults)

            for observanceObjectResultsList in observanceObjectResultsComposite:
                for observanceObject in observanceObjectResultsList:
                    print(observanceObject.getScenarioOutcome())

        if (caseCalculationType == 2):
            currentTestIndex = 0
            for stockEntryTotalities in stockEntryTotalitiesList:
                if (currentTestIndex == 0):
                    print("Internal Index: "+ str(currentTestIndex))
                    fullRangeStockList = self.dynamicTimeMarkationManager.calculateFullRangeList(stockEntryTotalities)
                    # print("first index: "+str(fullRangeStockList[0]))
                    # print("last index: "+ str(fullRangeStockList[(len(fullRangeStockList)-1)]))


                    chronDict = scenarioManager.stockChronologicalLocationIdentifier(fullRangeStockList)
                    stockRangeContainerTenMinuteSetComposite = self.dynamicTimeMarkationManager.calculateFullRangeMarkationList(fullRangeStockList, chronDict, self.timeManager)
                    for tenMinuteSet in stockRangeContainerTenMinuteSetComposite:
                        print(tenMinuteSet[0]["symbol"])
                    currentTestIndex += 1

                observanceObjectResults = scenarioManager.calculateFullRangeMarkationResults(stockRangeContainerTenMinuteSetComposite)
                observanceObjectResultsComposite.append(observanceObjectResults)
                # print(observanceObjectResultsComposite)
            for observanceObjectResults in observanceObjectResultsComposite[0]:
                print(observanceObjectResults.getScenarioOutcome())

            dynamaTransit.transferObservanceObjectResults(observanceObjectResults)

