from sources.weather import Weather
from urllib import request


url = request.urlopen("https://forecast.weather.gov/product.php?site=CRH&product=SFT&issuedby=RAH")
print(url)
newWeather = Weather()
temp = newWeather.main()
print(temp)