import asyncio
import time
import unittest
from test_sync import setup
from pyappbase import Appbase


async def hello_world(d, data):
    while d[0]:
        await asyncio.sleep(0.1)
        data.append("Hello")


class AsnycTests(unittest.TestCase):


    def tearDownClass(cls):
        data = {
            "type": "Books",
            "id": "X2",
        }
        sync_appbase = setup(Appbase)

        sync_appbase.index({
            "type": "Books",
            "id": "X2",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Network Routing",
                "price": 5295
            }
        })


    def setUp(self):
        self.data = {
            "type": "Books",
            "id": "X2",
        }
        self.appbase = setup(Appbase)
        self.appbase._set_async()
        self.sync_appbase = setup(Appbase)

        print(self.sync_appbase.index({
            "type": "Books",
            "id": "X2",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Network Routing",
                "price": 5295
            }
        }))


    def test_async_two_methods(self):
        """

        simple asynchronously running ping with an async hello_world coroutine
        :return:
        """

        # some thing multable
        wait = [True]
        data = []
        asyncio.get_event_loop().create_task(hello_world(wait, data))
        results = asyncio.get_event_loop().run_until_complete(self.appbase.ping())
        wait[0] = False

        async def temp():
            await asyncio.sleep(1)

        asyncio.get_event_loop().run_until_complete(temp())
        print(results)
        self.assertNotEquals(len(data), 0)

    def test_async_get(self):

        async def get_data():
            return await self.appbase.get(self.data)

        results = asyncio.get_event_loop().run_until_complete(get_data())
        self.assertEqual(results["_source"]["name"], "A Fake Book on Network Routing")

    def test_async_index(self):

        async def index_data():
            return await self.appbase.index({
            "type": "Books",
            "id": "X2",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Distributed Compute",
                "price": 5295
            }
        })
        async def get_data():
            return await self.appbase.get(self.data)

        index = asyncio.get_event_loop().run_until_complete(index_data())

        result = asyncio.get_event_loop().run_until_complete(get_data())
        self.assertEqual(result["_source"]["name"], "A Fake Book on Distributed Compute")
