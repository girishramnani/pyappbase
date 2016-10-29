import asyncio
import time
import unittest
from test_sync import setup
from pyappbase import Appbase

## this test is more of a demo of actually how the async get stream works
count =0
async def hello_world():
    global count
    count =0
    while True:
        await asyncio.sleep(0.1)
        print("hello world")
        count+=1


class AsnycStreamTests(unittest.TestCase):

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


    def test_get_stream(self):

        loop = asyncio.get_event_loop()
        loop.create_task(self.appbase.get_stream({
                "type":"Books",
                "id":"1"
            },lambda word: print(word)))

        loop.create_task(hello_world())
        loop.run_until_complete(asyncio.sleep(5))
        loop.run_until_complete(asyncio.sleep(1))
        self.assertNotEqual(count,0)


    def test_search_stream(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.appbase.search_stream({"type":"Books","query": {"match_all":{}}},lambda word: print(word)))
        loop.create_task(hello_world())
        loop.run_until_complete(asyncio.sleep(5))
        loop.stop()
        self.assertNotEqual(count,0)
