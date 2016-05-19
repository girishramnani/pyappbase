import unittest

from os.path import join, dirname
from dotenv import load_dotenv
import os

from pyappbase import Appbase


class SyncTest(unittest.TestCase):


    def setUp(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.appbase = Appbase(os.environ.get("USERNAME",""),os.environ.get("PASSWORD",""),os.environ.get("APPNAME",""))
        self.appbase.setAsync(False)


    def test_environ(self):
        self.

    def test_index(self):
        pass

    def test_get(self):
        pass


    def test_update(self):
        pass

    def test_delete(self):
        pass

    def test_bulk(self):
        pass

    def test_search(self):
        pass

    def get_stream(self):
        pass

    def search_stream(self):
        pass

    def search_stream_to_url(self):
        pass