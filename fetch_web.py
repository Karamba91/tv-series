#Fetch webpage from url using urllib2
import urllib2

def fetch (url=""):
    response = urllib2.urlopen('http://epguides.com/BigBangTheory/')
    html = response.read()
    print html