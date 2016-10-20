import re,fetch_web,Episode
from Episode_HTMLParser import Episode_HTMLParser

def list_episodes():
    return fetch_web.fetch_html()

def decode_html(html):
    parser = Episode_HTMLParser()
    parser.feed(html)
    print parser.data

# <pre>Test snippet</pre>