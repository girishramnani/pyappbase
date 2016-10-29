import json

import requests

from pyappbase.utils import make_url


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
        return requests.get(self.url).json()

    def get(self, data):
        """
        takes in data having a type and id to get the data from appbase

        :param data:
        :return:
        """
        return requests.get(url=make_url(self.url,data)).json()



    def index(self,data,bulk=False):
        """
        takes in data and stores it in appbase. the data should have a body key

        :param data:
        :return:
        """
        compat_object = data["body"]
        return requests.post(url=make_url(self.url,data,bulk),data=json.dumps(compat_object)).json()

    def update(self,data):
        """
        takes in data and stores it in appbase. the data should have a body key

        :param data:
        :return:
        """
        compat_object = data["body"]
        return requests.post(url=make_url(self.url,data)+"/_update",data=json.dumps(compat_object)).json()


    def delete(self,data):
        return requests.delete(url=make_url(self.url,data)).json()


    def get_stream(self,data,callback):
        raise NotImplementedError

    def search_stream(self,data,callback):
        raise NotImplementedError

