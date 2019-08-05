import urllib2

def go_online():
    url = urllib2.urlopen("https://google.com")
    mybytes = url.read()
    url.close()
    return url
