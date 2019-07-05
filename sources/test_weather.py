import unittest
from user import weather


class test_weather(unittest.TestCase):
    """
    Test the weather app for functionality
    """

    def test_the_weather(self):
        try:
            hurricane = Weather()
        except Exception:
            self.assertTrue(False, "The constructor failed, something must have gone wrong.")


    def test_the_heat(self):
        hurricane = Weather()
        forcastedTemp = hurricane.main()
        self.assertLessEqual(forcastedTemp, 90,
                        ("It is going to be over 90 today! Too hot with a temp of!" + str(forcastedTemp)))
