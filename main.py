import fetch_web
from UpdateEpisodeDB import open_and_read_json_from_file, open_and_write_json_to_file,create_dict_from_list_episodes, create_download_dict
from FindEpisode import get_magnet
from DecodeHTML import decode_html

info_url = 'http://epguides.com/bigbangtheory/'

#list_episodes = decode_html(fetch_web.fetch_html(info_url))
with open('thebigbangtheory.txt', 'r') as f:
    list_episodes = decode_html(f.read())

ep_dict = create_dict_from_list_episodes(list_episodes)

open_and_write_json_to_file('Data/Big Bang Theory', ep_dict)

open_and_write_json_to_file('Data/Big Bang Theory DOWNLOAD', create_download_dict(ep_dict))

#magnet_link_url = 'https://eztv.ag/search/?q1=&q2=23&search=Search' #The Big Bang Theory @ eztv

#print get_magnet(list_episodes[0], magnet_link_url)

#(Store_json.store_in_file(x, data_file) for x in list_episodes)