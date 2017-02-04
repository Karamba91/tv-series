import datetime
class Episode:
    def __init__(self, n_season, n_episode, n_name = "Episode", date = datetime.date(2000, 01, 01), downloaded=True):
        self.name = n_name
        self.season = n_season
        self.episode = n_episode
        self.broadcast_date = date
        self.downloaded = downloaded

    def get_name(self):
        return self.name

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def get_broadcastdate(self):
        return self.broadcast_date

    def is_downloaded(self):
        return self.downloaded
