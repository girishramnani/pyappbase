import aiohttp
import json
from pyappbase.utils import make_url


class AsyncHandler(object):

    def __init__(self, url):
        self.url = url

    async def ping(self):
        with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                resp = await response.read()
                return resp.decode()


    async def get(self,data):
        with aiohttp.ClientSession() as session:
            async with session.get(make_url(self.url,data)) as response:
                resp = await response.read()
                return json.loads(resp.decode())

    async def update(self,data):
        compat_object = data["body"]
        with aiohttp.ClientSession() as session:
            async with session.post(make_url(self.url,data),data=json.dumps(compat_object)) as response:
                resp = await response.read()
                return json.loads(resp.decode())

    async def delete(self,data):
        with aiohttp.ClientSession() as session:
            async with session.delete(make_url(self.url,data)) as response:
                resp = await response.read()
                return json.loads(resp.decode())
