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
from PerpetualTimer import PerpetualTimer
from HTTPUtility import HTTPUtility

class OperationCenter:
    __instance = None
    perpetualTimerSellBreachWatch = PerpetualTimer()
    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.__instance.name = ''
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.listGoldenGeese = []
        self.nodeRequester = NodeRequester()
        self.dataFilterManager = DataFilterManager()
        self.dynamicTimeMarkationManager = DynamicTimeMarkationManager()
        self.timeManager = TimeManager()
        self.dynamaTransit = DynamaTransit()
        self.typeConverter = TypeConverter()

        self.httpUtility = HTTPUtility()
        self.isHoldings = "0"
        self.boughtStockSymbol = "JKJKJKJK"
        self.isSellDelimiterMet = "0"
        return self.__instance


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


    def breachSellHoldings(self, holdings):
        #Verify that holdings have been sold
        listResults = self.typeConverter.parseHoldingQueryString(holdings)
        quantityOfShares = listResults[1]

        #if listResults
        if(quantityOfShares != 0):
            print("canceling perpetualTimerSellBreachWatch")
            self.perpetualTimerSellBreachWatch.cancel()


    def breachBuy(self, stringQuery):
        print(stringQuery)
        #totalsecurities
        #after purchase and wait 10 seconds, holdings string
        listResults = self.typeConverter.parseHoldingQueryString(stringQuery)
        quantityOfShares = listResults[1]

        # amountOfShares
        print("quantityOfShares: "+quantityOfShares)
        if(quantityOfShares != "0"):
            self.isHoldings = "1"

        #if positions found, continue operations - breach sell.
        if(self.isHoldings == "1"):
            print("isHoldings: true")
            #Continue operations
            self.quantityOfShares = quantityOfShares
            self.totalSecurities = listResults[0]
            print(self.quantityOfShares + " "+self.totalSecurities)

            #set monitor stocks on loop, for sell process
            #handle looped query, get latest stock from node
            self.initiateSellBreachProcess()

        #else cancel operations.
        else:
            print("cancel operations")
            #Support for reiterate chosen process

    def initiateSellBreachProcess(self):
        print("begin sell process")
        self.perpetualTimerSellBreachWatch.setup_timer_stock(1, 3000, self.getStockInformation, 'getStockInformation')

    def getStockInformation(self):
        print("getting stock")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(self.httpUtility.async_get_stock_query("VICI"))

        #Handle test information vici stats, parse stats into variables
        print(response)

        listResults = self.typeConverter.parseBreachStockQueryString(response)
        # print(listResults[0] + " " + listResults[1] + " " + listResults[2] + " " + listResults[3] + " " + listResults[4])

        #test boughtPrice
        boughtPrice =  29.72
        self.checkDelimiterMet(listResults,boughtPrice)

    def checkDelimiterMet(self, listResults, delimiter):
        #Current bought
        #listResults = [pchg, pcls, last, bid, ask]
        #delimiter met do sell
        if(listResults[2] == delimiter and self.isSellDelimiterMet == "0"):
            print("DELIMITER MET")
            #Sell post
            self.isSellDelimiterMet = "1"
            self.sellPost(self.boughtStockSymbol)


    def sellPost(self,symbol):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(self.httpUtility.async_breach_sell(symbol))


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


    # def test1(self):
    #     # print("hit")
    #     self.perpetualTimerSellBreachWatch.setup_timer_stock(1, 3000, self.testSign, 'getStockInformation')
    #
    # def testSign(self):
    #     print("testSign")
    #     print(self.perpetualTimerSellBreachWatch.isInitiated)
    #
    # def test2(self):
    #     self.perpetualTimerSellBreachWatch.cancel()