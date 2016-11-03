import re,fetch_web,datetime
from Episode_HTMLParser import Episode_HTMLParser
from Episode import Episode

def list_episodes():
    text_file = open("HTML.txt","r")
    r = text_file.read()
    text_file.close()
    return r
    #return fetch_web.fetch_html()

def decode_html(html):
    debug_i=0  # Debug index
    parser = Episode_HTMLParser()
    parser.feed(html)
    for i in parser.data:
        # To indicate which iteration loop fails
        # debug_i = debug_inc(debug_i)
        # Remove uneccesary information from string. Split at beginning of info.
        pure = re.split("(\d+\..+)",i)
        if len(pure) > 2:
            finish_flag = 0
            pure = pure[1]
            # Identifying information from string.
            m = re.match("(?P<total_episode>^\d+)(\.)(\s+)(?P<season>\d+)(\-)(?P<episode>\d+)(\s+)(?P<date>[\d\s\w]+)",pure)
            episode_dict = m.groupdict()
        elif finish_flag == 0:
            finish_flag = 1
            name = pure[0]
            new_episode = Episode(name,episode_dict['season'],episode_dict['episode'])
            print "Episode", new_episode.get_episode(),"in season", \
            new_episode.get_episode(), "is named", new_episode.get_name()

def debug_inc(index):
    index += 1
    print index
    return index 

def interpret_date(dateStr):
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    monthDict=dict(zip(months,range(1,13)))
    dd = dateStr.split()
    day = dd[0]
    month = monthDict[dd[1]]
    if len(dd[2]) == 2:
        year = "20" + dd[2]
    elif len(dd[2]) == 4:
        year = dd[2]
    return datetime.date(year,month,day)





decode_html(list_episodes())
# <pre>Test snippet</pre>