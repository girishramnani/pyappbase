import aiohttp
import json
import asyncio
from pyappbase.utils import make_url


class AsyncHandler(object):

    def __init__(self, url):
        self.url = url
        self._hold = asyncio.Event()
        self._hold.set()

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


    async def get_stream(self,data,callback):
        url = make_url(self.url,data)
        url = url + "?stream=true"

        return await self._stream_on_url(url,data,callback)

    def close_stream(self):
        self._hold.clear()

    def open_stream(self):
        self._hold.set()


    async def _stream_on_url(self,url,data,callback):
        self.open_stream()
        with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                while (not response.content.at_eof()) and self._hold.is_set():
                    line = await response.content.readany() # reads all the content in the buffer
                    callback(line)
                response.close()

    async def search_stream(self,data,callback):
        self.open_stream()
        url = "{url}/{type}/_search?stream=true".format(url=self.url,type=data["type"][:])
        del(data["type"])
        with aiohttp.ClientSession() as session:
            async with session.post(url,data=json.dumps(data)) as response:
                while (not response.content.at_eof()) and self._hold.is_set():
                    line = await response.content.readany() # reads all the content in the buffer
                    callback(line)
                response.close()
