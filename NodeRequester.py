import asyncio
from threading import Thread

class NodeRequester:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def postRequest(self, json):
        pass