import handler as h


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

        self.URL = "https://{user}:{passwd}@scalr.api.appbase.io/{app}".format(user=username, passw=password,
                                                                               app=appname)

    def ping(self):
        response = self.req_handler.ping(self.URL, self.auth)
        return response.json()

    def setAsync(self, boolean=True):
        if boolean == True:
            self.req_handler = h.AsyncHandler()

        else:
            self.req_handler = h.SyncHandler()
