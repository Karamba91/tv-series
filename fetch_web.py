#Fetch webpage from url using urllib2
import urllib2

def fetch_html (url=""):
    request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.google.se/",
        "Connection": "keep-alive"
    }
    response = urllib2.Request(url, headers=request_headers)
    html = urllib2.urlopen(response)
    html_code = html.read()
    html.close()
    return html_code
