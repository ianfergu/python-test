import sys
import urllib2

# jenkins exposes the workspace directory through env.
sys.path.append(['WORKSPACE'])



class Weather:
    def __init__(self):
        self.temp = 0
        self.myurl = ""

    def highOf(self):
        try:
            url = urllib2.urlopen("https://forecast.weather.gov/product.php?site=CRH&product=SFT&issuedby=RAH")
            mybytes = url.read()

            mystr = mybytes.decode("utf8")
            url.close()
            index = mystr.find("RALEIGH-DURHAM")
            mystr = mystr[index:]
            index = mystr.find("/")

            self.temp = int(mystr[index+1: index+3])

        except Exception:
            print("there was an error")

    def main(self):
        self.highOf()
        return self.temp



