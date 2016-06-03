import os
import unittest
from os.path import join, dirname
from dotenv import load_dotenv
from pyappbase import Appbase


def setup(Instance):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    appbase = Instance(os.environ.get("USERNAME", ""), os.environ.get("PASSWORD", ""), os.environ.get("APPNAME", ""))
    appbase.set_async(False)
    return appbase


class SyncTest(unittest.TestCase):
    """

    Tests for synchronous handler

    """

    @classmethod
    def tearDownClass(cls):
        data = setup(Appbase).update({
            "type": "Books",
            "id": "X2",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Network Routing",
                "price": 5295
            }
        })

    def setUp(self):
        """
        injects the data from .env file to the tests.
        :return:
        """
        self.appbase = setup(Appbase)

    def test_environ(self):
        """
        tests if the enivronment variables were loaded by checking if all of the values are not ""
        :return:
        """
        self.assertEqual(all([self.appbase.appname, self.appbase.password, self.appbase.username]), True)

    def test_ping(self):
        self.appbase.ping()
        self.assertEquals(self.appbase.ping()["status"], 200)

    def test_index(self):
        pass

    def test_get(self):
        data = self.appbase.get({
            "type": "Books",
            "id": "X2",
        })
        self.assertEqual(data["_source"]["name"], "A Fake Book on Network Routing")

    def test_update(self):
        data = self.appbase.update({
            "type": "Books",
            "id": "X3",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Distributed Compute",
                "price": 5295
            }
        })

        data = self.appbase.get({
            "type": "Books",
            "id": "X3",
        })
        self.assertEqual(data["_source"]["name"], "A Fake Book on Distributed Compute")

    def test_delete(self):
        data = self.appbase.update({
            "type": "Books",
            "id": "X3",
            "body": {
                "department_id": 1,
                "department_name": "Books",
                "name": "A Fake Book on Distributed Compute",
                "price": 5295
            }
        })

        data = self.appbase.delete({
            "type": "Books",
            "id": "X3"
        })

        self.assertEqual(self.appbase.get({
            "type": "Books",
            "id": "X3",
        })["found"], False)

    def test_bulk(self):
        pass

    def test_search(self):
        pass

    def test_get_stream(self):
        pass

    def test_search_stream(self):
        pass

    def test_search_stream_to_url(self):
        pass
