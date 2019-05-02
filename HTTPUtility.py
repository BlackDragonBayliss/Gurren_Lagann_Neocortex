
import aiohttp
import asyncio
from threading import Thread
class HTTPUtility:
    def __init__(self,):
        self.name = ''

    async def fetch(self,session, url, data):
        async with session.post(url, data=data) as response:
            return await response.text()

    async def async_breach_sell(self, symbol):
        async with aiohttp.ClientSession() as session:
            jsonRequest = {
                "request_type": "breachWatch",
                "breachSell": 1,
                "stock_symbol": symbol
            }
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned



# TSP Gather process
    async def async_get_stock_query(self, symbol):
        async with aiohttp.ClientSession() as session:
            jsonRequest = {
                "request_type": "breachWatch",
                "isGetLatestStock": 1,
                "stock_symbol": symbol
            }
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_stock_top_phase1(self, data, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.lookup_top_stocks_phase2(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_stock_top_phase2(self, topStockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.lookup_top_stocks_phase3(topStockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned




#Query
    async def async_post_stock_query_phase1(self, stockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_stock_query_phase1(stockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_query_stock(self, symbol):
        async with aiohttp.ClientSession() as session:
            jsonRequest = self.request_factory.async_query_stock(symbol)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned
    # async def async_post_stock_query_phase1(self, stockComposite, requestFactory):
    #     async with aiohttp.ClientSession() as session:
    #         jsonRequest = requestFactory.async_post_stock_query_phase1(stockComposite)
    #         url = 'http://localhost:3000/api/brokerage'
    #         responseReturned = await self.fetch(session, url, jsonRequest)
    #         return responseReturned




#Account
    async def async_post_account_information_phase2(self, account_information, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_account_information_phase2(account_information)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_account_information_phase3(self, stockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_account_information_phase3(stockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned


#Buy
    async def async_post_market_buy_phase1(self, data, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_buy_phase1(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_buy_phase2(self, stock, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_buy_phase2(stock)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_buy_phase3(self, stock, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_buy_phase3(stock)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)


#Sell
    async def async_post_market_sell_phase1(self, data, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_sell_phase1(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_sell_phase2(self, DM_Action, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_sell_phase2(DM_Action)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_sell_phase3(self, stockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_sell_phase3(stockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
