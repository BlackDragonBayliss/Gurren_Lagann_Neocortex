
from threading import Thread,Event,current_thread
from threading import Timer as _Timer

import aiohttp
import asyncio
import json

class PerpetualTimer():

   def __init__(self):
      self.currentCount = 0

   def setup_timer_stock(self, delay, countToEnd, functionToInvoke, name):
        self.delay = delay
        self.countToEnd = countToEnd
        self.functionToInvoke = functionToInvoke
        self.stopped = Event();
        self.name = name;
        self.thread =  Thread(target=self.__run, args=(),name=self.name)
        #
        self.thread.start()

   def setup_timer_timer_loop(self, delay, countToEnd, functionToInvoke, list_objects, name):
       self.delay = delay
       self.countToEnd = countToEnd
       self.functionToInvoke = functionToInvoke
       self.stopped = Event();
       self.name = name;
       self.list_objects();
       self.thread = Thread(target=self.__run, args=(list_objects), name=self.name)
       #
       self.thread.start()

   def __run(self):
       while not self.stopped.wait(self.delay):
           self.functionToInvoke()

   def cancel(self):
      # self.thread.cancel()
      print("quiting pep timer: "+self.name)
      self.stopped.set()