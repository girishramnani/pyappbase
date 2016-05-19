import requests


class SyncHandler(object):
    """
    SyncHandler is the synchronous request manager for the api. This approach is taken for future addition of
    twisted for compatibility with python2.7
    """

    def __init__(self, url):
        self.url = url

    def ping(self):
        """
        checks if the connection is working or not
        :return: returns a dict of type { "status" : int , "message" : string }
        """
        return requests.get(self.url)

    def get(self, data):
        """
        takes in data having a type and id to get the data from appbase

        :param data:
        :return:
        """
        return requests.get(url="".join([self.url, "/", data["type"], "/", data["id"]])).json()
