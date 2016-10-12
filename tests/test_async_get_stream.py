import asyncio
import time
import unittest
from test_sync import setup
from pyappbase import Appbase

## this test is more of a demo of actually how the async get stream works

async def hello_world():
    while True:
        await asyncio.sleep(0.1)
        print("hello world")


class AsnycStreamTests(unittest.TestCase):

    def setUp(self):
        self.data = {
            "type": "Books",
            "id": "X2",
        }
        self.appbase = setup(Appbase)
        self.appbase.set_async()
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


    def test_stream(self):

        loop = asyncio.get_event_loop()
        loop.create_task(self.appbase.get_stream({
                "type":"Books",
                "id":"1"
            },lambda word: print(word)))

        loop.run_until_complete(hello_world())