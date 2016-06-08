import aiohttp

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
                return resp.decode()