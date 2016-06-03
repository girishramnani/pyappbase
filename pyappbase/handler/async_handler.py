import aiohttp


class AsyncHandler(object):


    def __init__(self,url):
        self.url = url

    async def ping(self):
        with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                resp = await response.read()
                return resp.decode()
