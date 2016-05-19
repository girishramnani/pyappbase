import requests


class SyncHandler(object):
    """
    SyncHandler is the synchronous request manager for the api. This approach is taken for future addition of
    twisted for compatibility with python2.7
    """

    def __init__(self, url):
        self.url = url

    def ping(self, url):
        return requests.get(url)

    def get(self, data):
        return requests.get(url="".join([self.url, "/", data["type"], "/", data["id"]])).json()
