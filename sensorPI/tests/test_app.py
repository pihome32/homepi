"""Main test class for app_cli"""
from src import app

class TestApp(object):

    def setup_method(self, _):
        self.app = app

    def test_function(self):
        self.app.set_name("test")
assert self.app.get_name() == "test"