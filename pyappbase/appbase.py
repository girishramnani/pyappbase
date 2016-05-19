from .handler import AsyncHandler,SyncHandler

class WrongCredentialError(Exception):
    def __init__(self):
        super().__init__("Wrong credentials")


class Appbase(object):
    def __init__(self, username, password, appname):
        self.username = username
        self.password = password
        self.appname = appname
        self.auth = (username, password)
        self.setAsync()

        self.URL = "https://{user}:{passwd}@scalr.api.appbase.io/{app}".format(user=username, passwd=password,
                                                                               app=appname)

    def ping(self):
        response = self.req_handler.ping(self.URL)
        return response.json()

    def setAsync(self, boolean=True):
        if boolean == True:
            self.req_handler = AsyncHandler()

        else:
            self.req_handler = SyncHandler()
