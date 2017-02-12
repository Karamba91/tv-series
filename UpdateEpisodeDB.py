import json
import os
import sys
from datetime import date
from DecodeHTML import decode_html
import fetch_web


def add_series(tag, name, epguid_url, eztv_url):
    tv_dic = open_and_read_json_from_file('tvseries.json')
    if (tag in tv_dict.keys()) or (name in [tv_dict[tv_series] for tv_series in tv_dict.keys()]):
        print "Tv- series seems to already exist in database"
        return -1
    else:
        tv_dict.update({tag:{'Name': name, 'epguides_url': epguid_url, 'eztv_url': eztv_url}})
        return 0


def create_dict_from_list_episodes(list_episodes, first_setup=False):
    ep_dict = dict()
    for episode in list_episodes:
        if episode.get_season() not in ep_dict.keys():
            ep_dict.update({episode.get_season(): dict()})
        # If first setup
        if first_setup:
            ep_dict[episode.get_season()][episode.get_episode()] = {'title': episode.get_name(),
                                                                    'broadcast_date': str(episode.get_broadcastdate()),
                                                                    'downloaded': True}
        else:
            ep_dict[episode.get_season()][episode.get_episode()] = {'title': episode.get_name(),
                                                                    'broadcast_date': str(episode.get_broadcastdate()),
                                                                    'downloaded': False}

    return ep_dict

def open_and_write_json_to_file(name, jstr):
    with open('Data/' + name + '.json', 'w') as file_handle:
        return file_handle.write(json.dumps(jstr, indent=4, sort_keys=True))



def open_and_read_json_from_file(name):
    #try:
    with open('Data/' + name + '.json', 'r') as file_handle:
        return json.loads(file_handle.read())
    #except IOError:
    #    raise IOError("File you tried to open could not be opened")



def create_download_dict(ep_db):
    today = date.today().isoformat()
    download_dict = dict()
    for seas in ep_db.keys():
        for ep in ep_db[seas].keys():
            if (ep_db[seas][ep]['broadcast_date'] < today) and (ep_db[seas][ep]['downloaded'] is False):
                if seas in download_dict.keys():
                    if ep in download_dict[seas].keys():
                        raise ValueError('Trying to add a episode that already exists, abort to preserve list')
                    download_dict[seas].update({ep: ep_db[seas][ep]})
                else:
                    download_dict.update({seas: {ep: ep_db[seas][ep]}})
    return download_dict


def update_episode_dict(old_ep_dict, new_ep_dict):
    updated_episodes = 0
    ret_dict = old_ep_dict
    for seas in old_ep_dict.keys():
        if old_ep_dict[seas].keys() == new_ep_dict[seas].keys():
            continue
        else:
            if len(new_ep_dict[seas].keys()) < len(old_ep_dict[seas].keys()):
                raise ValueError('Newly updated season have fewer episode than previous, check this')
            diff_list = list(set(new_ep_dict[seas].keys()) - set(old_ep_dict[seas].keys()))
            for diff_episode in diff_list:
                updated_episodes += 1
                print "Updated with S" + seas + "E" + diff_episode
                ret_dict[seas].update({diff_episode: new_ep_dict[seas][diff_episode]})
    if updated_episodes < 1:
        print "No episodes updated"
    return ret_dict

if __name__ == '__main__':

    # Make sure that fuction is called with any tag
    try:
        tv_tag = sys.argv[1]
    except IndexError:
        raise IndexError('You have to call function with series tag')
    tv_dict = open_and_read_json_from_file('tvseries')

    # Check whether tag belongs to a valid
    try:
        if not os.path.exists('Data/' + tv_dict[tv_tag]['Name'] + '.json'):
            raise NotImplementedError('Could not find database for current tv series, add it manually first time')
    except KeyError:
        raise KeyError('Can\'t find tag in series list, try and add manually with function')

    series_dict_old = open_and_read_json_from_file(tv_dict[tv_tag]['Name'])
    series_list_new = decode_html(fetch_web.fetch_html(tv_dict[tv_tag]['epguides_url']))
    series_dict_new = create_dict_from_list_episodes(series_list_new)
    open_and_write_json_to_file(tv_dict[tv_tag]['Name'],
                                update_episode_dict(series_dict_old, series_dict_new))

# a = {1: {2: {4: 5}}, 3: {4: {45: 6}}, 5: {6: {66: 55}}, 7: {8: {65: 77}}}
# b = {1: {2: {4: 5}}, 3: {4: {45: 6, 345: 53}, 2: {55:5}}, 5: {6: {66: 55}}, 7: {8: {65: 77, 776: 45, 6: 45}}}
# print update_episode_dict(a, b)