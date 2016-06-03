import asyncio

from pyappbase.handler import AsyncHandler


def conditional_coroutine(func):

    def wrapper(*args,**kwargs):

        try:
            self = args[0]

            for attribute in self.__dict__:
                if isinstance(getattr(self, attribute), AsyncHandler):
                    return asyncio.coroutine(func)

        except IndexError:
            raise IndexError("the function wrapped is not a method")

        return func

    return wrapper



def make_url(url,data):
    return "".join([url, "/", data["type"], "/", data["id"]])
