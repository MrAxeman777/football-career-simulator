class Career:

    def __init__(self, player):

        self.player = player
        self.club = "Youth Academy"

        self.history = []


    def add_season(self, season, club, goals, assists, trophies):

        self.history.append({

            "season": season,
            "club": club,
            "goals": goals,
            "assists": assists,
            "trophies": trophies

        })


    def transfer(self, new_club):

        self.club = new_club


    def get_history(self):

        return self.history
