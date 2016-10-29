import asyncio


def make_url(url,data,bulk=False):
    if bulk:
        return "".join([url,"/",data["type"],"/","_bulk"])
    return "".join([url, "/", data["type"], "/", data["id"]])
