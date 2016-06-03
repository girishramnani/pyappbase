import asyncio
from functools import wraps

from pyappbase.handler import AsyncHandler


def conditional_coroutine(func):
    @wraps
    def wrapper(*args,**kwargs):

        try:
            self = args[0]
            is_instance = isinstance(self,AsyncHandler)
        except IndexError:
            raise IndexError("the function wrapped is not a method")

        if is_instance:
            return  asyncio.coroutine(func)
        return func



def map_object(data):
    """

    maps the input object for update and other operations having payload
    of type {
                type : ---
                id : ---
                body : new-content
            }
          To
            {
                type : ---
                id : ---
                body : { doc : new-content }
            }
    which is accepted by the appbase server


    :param data:
    :return:
    """

    body = data["body"]

    data["body"] = {
        "doc": body
    }

    return data


def make_url(url,data):
    return "".join([url, "/", data["type"], "/", data["id"]])
