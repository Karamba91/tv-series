import re,fetch_web,Episode
from Episode_HTMLParser import Episode_HTMLParser

def list_episodes():
    text_file=open("HTML.txt","r")
    r=text_file.read()
    text_file.close()
    return r
    #return fetch_web.fetch_html()

def decode_html(html):
    debug_i=0          # Debug index
    parser = Episode_HTMLParser()
    parser.feed(html)
    print parser.data
    for i in parser.data:
        # To indicate which iteration loop fails
        debug_i = debug_inc(debug_i)
        # Remove uneccesary information from string. Split at beginning of info.
        pure=re.split("(\d+\..+)",i)[1]
        print pure
        # Identifying information from string.
        m = re.match("(?P<total_episode>^\d+)(\.)(\s+)(?P<season>\d+)(\-)(?P<episode>\d+)(\s+)(?P<date>[\d\s\w]+)",pure)
        print m.groupdict()

def debug_inc(index):
    index += 1
    print index
    return index 
# decode_html(list_episodes())
# <pre>Test snippet</pre>