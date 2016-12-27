#Fetch webpage from url using urllib2
import urllib2

def fetch_html (url=""):
    response = urllib2.urlopen(url)
    html = response.read()
    return html