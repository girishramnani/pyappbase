import requests




class SyncHandler(object):

    def __init__(self,url):
        self.url = url

    def ping(self,url):
        return requests.get(url)


    def get(self,data):
        return requests.get(url="".join([self.url,"/",data["type"],"/",data["id"]])).json()