import unittest
from sources.run import get_url


class test_url(unittest.TestCase):
    """
    Test the weather app for functionality
    """
    def test_the_url(self):
        try:
            get_url()
        except Exception:
            self.assertTrue(False, "The url failed, the website must be down. Abort mission.")
