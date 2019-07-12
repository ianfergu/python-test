import unittest
from sources.webtest import go_online


class test_webtest(unittest.TestCase):
    """
    Test the weather app for functionality
    """
    def test_webl(self):
        result = ""
        result = go_online()
        self.assertNotEqual(result, "")