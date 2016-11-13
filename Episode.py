import datetime
class Episode:
    def __init__(self, n_name="", n_season=0, n_episode=0, date = datetime.date(2000, 01, 01)):
        self.name = n_name
        self.season = n_season
        self.episode = n_episode
        self.broadcast_date = date

    def get_name(self):
        return self.name

    def get_season(self):
        return self.season

    def get_episode(self):
        return self.episode

    def get_brdcstdate(self):
        return self.broadcast_date
