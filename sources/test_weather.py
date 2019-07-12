import unittest
from weather import Weather


class test_weather(unittest.TestCase):
    """
    Test the weather app for functionality
    """

    def test_the_weather(self):
        try:
            hurricane = Weather()
        except Exception:
            self.assertTrue(False, "The constructor failed, "
                                   "something must have gone wrong.")


    def test_the_heat(self):
        hurricane = Weather()
        forcastedTemp = hurricane.main()
        print(forcastedTemp)
        self.assertLessEqual(forcastedTemp, 90,
                        ("It is going to be over 90 today! "
                         "Too hot with a high of: " + str(forcastedTemp)))

    def test_the_cold(self):
        blizzard = Weather()
        forecastedTemp = blizzard.main()
        self.assertLessEqual(forecastedTemp, 32,
                             ("No chance of a blizzard today! "
                              "Too hot with a high of: " + str(forecastedTemp)))