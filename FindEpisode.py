import urllib2, Episode
from bs4 import BeautifulSoup
__author__="Erik Henriksson"


def get_magnet(ep, url):
    magnet_link = []

    # Read content of url
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html=opener.open(url)

    pars = BeautifulSoup(html.read(),'html.parser')

    a_tags = pars.findAll("a")
    for each_tag in a_tags:
        ep_id = get_id(ep)
        if each_tag.get('title') is None:
            continue
        elif ("Magnet Link" in each_tag.get('title')) and (ep_id in each_tag.get('title')):
            magnet_link.append(each_tag.get('href'))

    if len(magnet_link)>1:
        magnet_link_final=filter(lambda x: "720p" in x, magnet_link)
        if len(magnet_link_final) == 0:
            magnet_link_final = magnet_link[0]
        elif len(magnet_link_final) >= 2:
            magnet_link_final = magnet_link_final[0]

    elif len(magnet_link) == 1:
        magnet_link_final = magnet_link[0]

    else:
        magnet_link_final = " "
    return magnet_link_final

def get_id(ep):
    season = ep.get_season()
    episode = ep.get_episode()
    if int(season) < 10:
        season = "0" + season
    if int(episode) < 10:
        episode = "0" + episode
    return "S" + season + "E" + episode
