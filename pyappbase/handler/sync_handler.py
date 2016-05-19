import requests


class SyncHandler(object):


    def ping(self,url):
        return requests.get(url)