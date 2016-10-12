import asyncio


def make_url(url,data):
    return "".join([url, "/", data["type"], "/", data["id"]])
