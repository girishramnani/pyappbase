import aiohttp
import json
import asyncio
from pyappbase.utils import make_url


class AsyncHandler(object):

    def __init__(self, url):
        self.url = url

    async def ping(self):
        with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                resp = await response.read()
                return json.loads(resp.decode())


    async def get(self,data):
        with aiohttp.ClientSession() as session:
            async with session.get(make_url(self.url,data)) as response:
                resp = await response.read()
                return json.loads(resp.decode())



    async def index(self,data,bulk=False):
        compat_object = data["body"]
        url = make_url(self.url,data,bulk)
        with aiohttp.ClientSession() as session:
            async with session.post(url,data=json.dumps(compat_object)) as response:
                resp = await response.read()
                return json.loads(resp.decode())


    async def update(self,data):
            compat_object = data["body"]
            url = make_url(self.url,data)+"/_update"
            with aiohttp.ClientSession() as session:
                async with session.post(url,data=json.dumps(compat_object)) as response:
                    resp = await response.read()
                    return json.loads(resp.decode())

    async def delete(self,data,bulk=False):
        url = make_url(self.url,data,bulk)

        with aiohttp.ClientSession() as session:
            async with session.delete(url) as response:
                resp = await response.read()
                return json.loads(resp.decode())


    async def get_stream(self,data,callback):
        url = make_url(self.url,data)
        url = url + "?stream=true"

        return await self._stream_on_url(url,data,callback)



    async def _stream_on_url(self,url,data,callback):
        with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                while (not response.content.at_eof()) :
                    line = await response.content.readany() # reads all the content in the buffer
                    callback(json.loads(line.decode()))
                response.close()

    async def search_stream(self,data,callback):
        url = "{url}/{type}/_search?stream=true".format(url=self.url,type=data["type"][:])
        del(data["type"])
        with aiohttp.ClientSession() as session:
            async with session.post(url,data=json.dumps(data)) as response:
                while (not response.content.at_eof()) :
                    line = await response.content.readany() # reads all the content in the buffer

                    callback(json.loads(line.decode()))
                response.close()
