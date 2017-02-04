import json
from datetime import date


def create_dict_from_list_episodes(list_episodes):
    ep_dict = dict()
    for episode in list_episodes:
        if episode.get_season() not in ep_dict.keys():
            ep_dict.update({episode.get_season(): dict()})
        ep_dict[episode.get_season()][episode.get_episode()] = {'title': episode.get_name(),
                                                                'broadcast_date': str(episode.get_broadcastdate()),
                                                                'downloaded': True}
    return ep_dict

def open_and_write_json_to_file(name, jstr):
    with open(name+'.json', 'w') as file_handle:
        return file_handle.write(json.dumps(jstr, indent=4, sort_keys=True))


def open_and_read_json_from_file(name):
    with open(name + '.json', 'r') as file_handle:
        return json.loads(file_handle.read())


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
