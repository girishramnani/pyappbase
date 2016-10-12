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

    def setUp(self):
        self.data = {
            "type": "Books",
            "id": "X2",
        }
        self.appbase = setup(Appbase)
        self.appbase._set_async()
        self.sync_appbase = setup(Appbase)

        self.sync_appbase.update({
            "type": "Books",
            "id": "X2",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Network Routing",
                "price": 5295
            }
        })

    def test_async_sync_ping_comparison(self):
        """
        This test runs the sync and async methods 'call_counts' times and checks if the async is faster than
        sync or not
        :return:
        """
        # number of simultaneous calls
        call_counts = 4


        t = time.time()
        for i in range(call_counts):
            print(self.sync_appbase.ping())
        sync_difference = time.time() - t
        print()
        print("Syncronous method took ", sync_difference, "s")

        async def get_data():
            return await self.appbase.ping()

        t = time.time()
        loop = asyncio.get_event_loop()

        async def get_data_gathered():
            answer = await asyncio.gather(*[get_data() for _ in range(call_counts)], loop=loop)
            return answer

        print("".join(loop.run_until_complete(get_data_gathered())))
        async_difference = time.time() - t
        print("Asnycronous method took ", async_difference, "s")
        print()

        # the async is more fast
        self.assertGreater(sync_difference, async_difference)

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

    def test_async_update(self):

        async def update_data():
            return await self.appbase.update({
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

        update = asyncio.get_event_loop().run_until_complete(update_data())

        result = asyncio.get_event_loop().run_until_complete(get_data())
        self.assertEqual(result["_source"]["name"], "A Fake Book on Distributed Compute")
