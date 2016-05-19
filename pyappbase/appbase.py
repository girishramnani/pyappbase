from .handler import AsyncHandler, SyncHandler


class WrongCredentialError(Exception):
    def __init__(self):
        super().__init__("Wrong credentials")


class Appbase(object):
    def __init__(self, username, password, appname):
        self.username = username
        self.password = password
        self.appname = appname

        self.URL = "https://{user}:{passwd}@scalr.api.appbase.io/{app}".format(user=username, passwd=password,
                                                                               app=appname)

        self.set_async()


    def ping(self):
        response = self.req_handler.ping(self.URL)
        return response.json()

    def set_async(self, boolean=True):
        if boolean:
            self.req_handler = AsyncHandler(self.URL)

        else:
            self.req_handler = SyncHandler(self.URL)

    def get(self, data):
        return self.req_handler.get(data)
