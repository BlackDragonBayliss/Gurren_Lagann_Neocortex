from NodeRequester import NodeRequester

class GoldenGooseDeterminer:
    def __init__(self):
        self.range = []
        self.highPriceDelimiter = 20.0
        self.lowPriceDelimiter = 2.0
        self.nodeRequester = NodeRequester()


    def refreshHardMetrics(self):
        response = self.nodeRequester.getGoldenGooseMetrics()
        self.highPriceDelimiter = float(response["data"]["highPriceDelimiter"])
        self.lowPriceDelimiter = float(response["data"]["lowPriceDelimiter"])

        print("Look at that highPriceDelimiter wow: "+str(self.highPriceDelimiter))
        print("Look at that lowPriceDelimiter wow: "+ str(self.lowPriceDelimiter))


    def processGoldenGeese(self, operationCenter, listRawGeeseMetrics):
        # self.refreshHardMetrics()
        print("listRawGeeseMetrics: "+ str(listRawGeeseMetrics))
        listFilteredGeeseMetrics = [[listRawGeeseMetrics[0],listRawGeeseMetrics[1],2.03, #listRawGeeseMetrics[2],
                                     listRawGeeseMetrics[3],listRawGeeseMetrics[4]],
                                    [listRawGeeseMetrics[5],listRawGeeseMetrics[6], 2.02,#listRawGeeseMetrics[7],
                                     listRawGeeseMetrics[8],listRawGeeseMetrics[9]],
                                    [listRawGeeseMetrics[10],listRawGeeseMetrics[11],2.01,#listRawGeeseMetrics[12],
                                     listRawGeeseMetrics[13], listRawGeeseMetrics[14]]]



        #Succesful list, initial criteria met
        listSuccessfulGeeseMetrics = []
        for filteredGeeseMetrics in listFilteredGeeseMetrics:
            if(self.isGoldenGoose(filteredGeeseMetrics)):
                listSuccessfulGeeseMetrics.append([filteredGeeseMetrics, 1])
            else:
                listSuccessfulGeeseMetrics.append([filteredGeeseMetrics, 0])



        #Priority highest DM, extend all others, fixed priority MM handle, check priority 11
        listSuccessfulGeeseMetrics = self.compareGeesePrices(listSuccessfulGeeseMetrics)

        operationCenter.setListGoldenGeese(listSuccessfulGeeseMetrics)
        print("List flying geese: " + str(operationCenter.getListGoldenGeese()))

        # Isolate if determined
        isChosenDetermined = self.calculateIsChosenDetermined(listSuccessfulGeeseMetrics)

        print("isChosenDetermined: "+ str(isChosenDetermined))
        # response = self.nodeRequester.postGoldenGooseResult(isChosenDetermined,"POP",0,"DOG",1,"MOM", 0)
        print("listSuccessfulGeeseMetrics :" + str(listSuccessfulGeeseMetrics))
        sublist1 = listSuccessfulGeeseMetrics[0]
        sublist2 = listSuccessfulGeeseMetrics[1]
        sublist3 = listSuccessfulGeeseMetrics[2]
        sublistSymbol1 = sublist1[0][0]
        sublistSymbol2 = sublist2[0][0]
        sublistSymbol3 = sublist3[0][0]
        sublistPriority1 = sublist1[1]
        sublistPriority2 = sublist2[1]
        sublistPriority3 = sublist3[1]


        print("sublist: " + str(sublistSymbol1) + str(sublistPriority1))
        # print("sublist: "+str(sublist2[0][0]))
        # print("sublist: " + str(sublist3[0][0]))


        #Frankly bayliss remember alt reality and reaching it twice as fast.
        #Remember in your alt reality they are your friend.

        # print("listSuccessfulGooseMetrics[0][1] :"+str(listSuccessfulGooseMetrics[0][1]))
        # print("listSuccessfulGooseMetrics[0][0] :"+str(listSuccessfulGooseMetrics[0][0]))
        response = self.nodeRequester.postGoldenGooseResult(isChosenDetermined, sublistSymbol1, sublistPriority1,
                                                            sublistSymbol2, sublistPriority2,
                                                            sublistSymbol3, sublistPriority3)


    def compareGeesePrices(self, listSuccessfulGeeseMetrics):
        listComparison = []
        for metric in listSuccessfulGeeseMetrics:
            metricPriority = metric[1]
            print("Compare metricPriority: "+str(metricPriority))
            if(metricPriority > 0):
                listComparison.append(metric)

        highestPriorityBid = ""
        highestPriorityIndex = 0
        metrixIndex = 0
        for metric in listComparison:
            print(metric)
            bid = metric[0][2]
            print("metric bid: "+str(bid))
            if(highestPriorityBid == ""):
                print("Init highestPriorityBid")
                highestPriorityBid = bid
                highestPriorityIndex = metrixIndex
            if (highestPriorityBid < bid):
                print("bidHigher former bid: "+ str(highestPriorityBid) +"bidHigher current greater bid: "+str(bid))
                highestPriorityBid = bid
                highestPriorityIndex = metrixIndex
            metrixIndex += 1

        #get highest priority metric find in list, update priority by 1
        highestPriorityMetric = listComparison[highestPriorityIndex]

        #update original list
        updateIndex = 0
        for metric in listSuccessfulGeeseMetrics:
            currentSymbol = metric[0][0]
            currentBid = metric[0][2]
            print("messed currentBid: "+str(currentBid))

            if(currentSymbol == highestPriorityMetric[0][0]):
                listSuccessfulGeeseMetrics[updateIndex][1] = (listSuccessfulGeeseMetrics[updateIndex][1] + 1)
                priorityUpdated = listSuccessfulGeeseMetrics[updateIndex][1]
                print("Symbol: "+str(listSuccessfulGeeseMetrics[updateIndex][0][0])
                      + " bid: "+str(listSuccessfulGeeseMetrics[updateIndex][0][2]))
                print("priorityUpdated: "+str(priorityUpdated))

            updateIndex += 1
        return listSuccessfulGeeseMetrics

    def calculateIsChosenDetermined(self,listGooseMetrics):
        #if list is not empy, return true

        for gooseMetrics in listGooseMetrics:
            if(gooseMetrics[1] == 1):
                print("goose: "+str(gooseMetrics[1]))
                return 1
        return 0

    def isGoldenGoose(self, filteredGeeseMetrics):
        # Support for multi-metric calculations
        if(self.isWithinRange(float(filteredGeeseMetrics[2]))):
            print("GG returning true: "+ str(filteredGeeseMetrics[2]))
            return True
        return False

    def isWithinRange(self, price):
        if(price >= self.highPriceDelimiter):
            return False
        if (price <= self.lowPriceDelimiter):
            return False
        return True