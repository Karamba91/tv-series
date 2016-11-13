import re,fetch_web,datetime,Store_json
from Episode_HTMLParser import Episode_HTMLParser
from Episode import Episode

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
f = open('data.txt','w')
f.write("")
f.close()
# Open file in append mode
data_file = open('data.txt', 'a')
list_episodes = decode_html(fetch_web.fetch_html())
data_file.write(list_episodes)
#(Store_json.store_in_file(x, data_file) for x in list_episodes)