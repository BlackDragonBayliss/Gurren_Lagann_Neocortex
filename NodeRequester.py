import asyncio
from threading import Thread

class NodeRequester:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def postRequest(self, json):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(
            self.operation_center.node_manager.async_post_data_manager_request_bundle(
                json))