import re, fetch_web, datetime
from Episode_HTMLParser import Episode_HTMLParser
from Episode import Episode
from FindEpisode import get_magnet

def decode_html(html):
    episode_list=[]
    parser = Episode_HTMLParser()
    parser.feed(html)
    for i in parser.data:
        # Remove uneccesary information from string. Split at beginning of info at "#number dot".
        pure = re.split("(\d+\..+)",i)
        if len(pure) > 2:
            finish_flag = 0
            pure = pure[1]
            # Identifying information from string.
            m = re.match(
                "(?P<total_episode>^\d+)(\.)(\s+)(?P<season>\d+)(\-)(?P<episode>\d+)(\s+)(?P<date>[\d\s\w]+)",pure)
            episode_dict = m.groupdict()
        elif finish_flag == 0:
            finish_flag = 1
            name = pure[0]
            episode_list.append(Episode(name, episode_dict['season'], episode_dict['episode'],
                                        interpret_date(episode_dict['date'])))
    return episode_list

def interpret_date(dateStr):
    months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthDict = dict(zip(months, range(1, 13)))
    dd = dateStr.split()
    day = dd[0]
    month = monthDict[dd[1]]
    if len(dd[2]) == 2:
        year = "20" + dd[2]
    elif len(dd[2]) == 4:
        year = dd[2]
    return datetime.date(int(year), int(month), int(day))


# Initialization of file, clean sheet.
f = open('data.txt', 'w')
f.write("")
f.close()
# Open file in append mode
data_file = open('data.txt', 'a')

info_url = 'http://epguides.com/bigbangtheory/'

list_episodes = decode_html(fetch_web.fetch_html(info_url))

#print [i.get_name() for i in list_episodes]

magnet_link_url = 'https://eztv.ag/search/?q1=&q2=23&search=Search' #The Big Bang Theory @ eztv

#print "S" + list_episodes[-1].get_season() + 'E' + list_episodes[1].get_episode()

print get_magnet(list_episodes[0], magnet_link_url)

#(Store_json.store_in_file(x, data_file) for x in list_episodes)