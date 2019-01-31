import asyncio
from threading import Thread

class AlgorithmFactory:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def createAlgorithm(self, case):
        pass