from sources.weather import Weather
import urllib2


def get_url():
    url = urllib2.urlopen("https://forecast.weather.gov/product.php?site=CRH&product=SFT&issuedby=RAH")
    print(url)
