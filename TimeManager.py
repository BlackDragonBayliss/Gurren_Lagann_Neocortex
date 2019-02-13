import calendar, time, datetime

class TimeManager:
    def __init__(self):
        pass

    def getCurrentSecond(self):
        ts = time.time()
        self.currentTime = time.localtime(ts)
        return self.currentTime.tm_sec

    def getCurrentMinute(self):
        ts = time.time()
        self.currentTime = time.localtime(ts)
        return self.currentTime.tm_min

    def getCurrentHour(self):
        ts = time.time()
        self.currentTime = time.localtime(ts)
        return self.currentTime.tm_hour

    def getCurrentEpochTime(self):
        epoch_time = calendar.timegm(time.gmtime())
        return epoch_time

    def getCurrentDateObjectList(self):
        date = datetime.datetime.now()
        # print(x.year)
        # print(x.month)
        # print(x.day)
        dateObjectList = [date.year, date.month, date.day]
        return dateObjectList

    def convertEpochToTime(self, epochInput):
        timeResult = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(epochInput))
        return timeResult

    def convertTimeToEpoch(self, dateTime):
        pattern = '%d.%m.%Y %H:%M:%S'
        epoch = int(time.mktime(time.strptime(dateTime, pattern)))
        return epoch


    def isStockWithinTradingTimeBound(self, stock):
        if(int(stock["hour_created"]) >= 14):
            return False
        return True

