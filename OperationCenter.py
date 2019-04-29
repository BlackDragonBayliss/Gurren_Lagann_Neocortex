import asyncio
from threading import Thread
from NodeRequester import NodeRequester
from DataFilterManager import DataFilterManager
from DynamicTimeMarkationManager import DynamicTimeMarkationManager
from ScenarioManager import ScenarioManager
from DataDisplayer import DataDisplayer
from TimeManager import TimeManager
from DynamaTransit import DynamaTransit
from TypeConverter import TypeConverter

class OperationCenter:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.listGoldenGeese = []
        self.nodeRequester = NodeRequester()
        self.dataFilterManager = DataFilterManager()
        self.dynamicTimeMarkationManager = DynamicTimeMarkationManager()
        self.timeManager = TimeManager()
        self.dynamaTransit = DynamaTransit()
        self.typeConverter = TypeConverter()

    def process_main_process_loop(self):
        self.main_process_loop()

    def main_process_loop(self):
        self.perpetual_timer.setup_timer_stock(1, 1000000, self.main_loop, 'main_process_loop')

    def main_loop(self):
        #Handle loop, check time, if time 10:30 initiate time process.
        if (self.calculate_time_delimiter_initiate_buy_process()):
            self.initiate_buy_process()

    def calculate_time_delimiter_initiate_buy_process(self):
        print(self.time_manager.get_current_hour())
        if(self.time_manager.get_current_hour() == self.scrape_hour):
            if (self.time_manager.get_current_minute() == self.scrape_minute):
                return True
        return False

    def breachBuy(self, stringQuery):
        print(stringQuery)

        #totalsecurities

        #after purchase and wait 10 seconds, holdings string
        isHoldings = "1"
        #if positions found, continue operations - breach sell.
        if(isHoldings == "1"):
            print("")
        #else cancel operations.
        else:
            print("cancel operations")

        #get if trade was successful, wait 10 seconds



    def initiate_buy_process(self):
        #Buy trade process
        #Bird to node
        self.nodeRequester.postBuyBreachWatch()



    def goldenGooseProcess(self, data):
        listGeeseMetrics = []
        # for key, value in data.items():
        #     listGeeseMetrics.append(value)
        for gooseMetrics in data:
            listGeeseMetrics.append(gooseMetrics)

        print("list symbol values: "+str(listGeeseMetrics))

        # intake stock json, take price and pchg
        # transform json into list, of price and pchg.
        # get price and pchg of each item in list.
            #parse json of each in list

        self.dynamaTransit.goldenGooseProcessIntake(self, listGeeseMetrics)

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
            # for observanceObjectResults in observanceObjectResultsComposite[0]:
                # print(observanceObjectResults.getScenarioOutcome())

            self.dynamaTransit.transferObservanceObjectResults(observanceObjectResultsComposite)

    def setListGoldenGeese(self, listGoldenGeese):
        self.listGoldenGeese = listGoldenGeese
    def getListGoldenGeese(self):
        return self.listGoldenGeese