from .handler import AsyncHandler, SyncHandler


class WrongCredentialError(Exception):
    """
    Is used by appbase for the users to recover from wrong credentials  ( will be used soon ).
    """

    def __init__(self):
        super().__init__("Wrong credentials")


class Appbase(object):
    """
    The main class which handles the auth and also provides abstraction over selection of different handlers.

    :param username : the user key of the appbase account ( preferably with R/W rights),
            password : secret key of the account
            appname : the app name (should be unique to all the other appnames )
    """

    def __init__(self, username, password, appname):
        self.username = username
        self.password = password
        self.appname = appname

        self.URL = "https://{user}:{passwd}@scalr.api.appbase.io/{app}".format(user=username, passwd=password,
                                                                               app=appname)

        self.set_async()

    def ping(self):
        """
        checks if the connection is working or not
        :return: returns a dict of type { "status" : int , "message" : string }
        """
        response = self.req_handler.ping()
        return response.json()

    def set_async(self, boolean=True):
        """
        sets if the handlers should be async or synchronous. Defaults to async.
        :param boolean:
        :return:
        """
        if boolean:
            self.req_handler = AsyncHandler(self.URL)

        else:
            self.req_handler = SyncHandler(self.URL)

    def get(self, data):
        return self.req_handler.get(data)
