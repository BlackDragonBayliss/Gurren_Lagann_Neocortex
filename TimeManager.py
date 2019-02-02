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

    def convertEpochToTime(self, epochInput):
        # timeResult = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(epoch))
        timeResult = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(epochInput))
        return timeResult

    def convertTimeToEpoch(self, dateTime):
        # date_time = '29.08.2011 11:05:02'
        # pattern = '%d-%m-%Y %H:%M:%S'
        # pattern = '%H:%M:%S'
        # epochResult = time.mktime(time.strptime(timeInput, pattern));#int(time.mktime(time.strptime(timeInput, pattern)))
        # return epochResult

        pattern = '%d.%m.%Y %H:%M:%S'
        epoch = int(time.mktime(time.strptime(dateTime, pattern)))
        return epoch

        # epochResult = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
        # return epochResult
