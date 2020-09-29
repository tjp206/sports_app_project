from random import shuffle

class Game:
    def __init__(self, name, home_team, away_team, id = None):
        self.name = name
        self.home_team = home_team
        self.away_team = away_team
        self.id = id

    def winner(self, home_team, away_team):
        teams = [home_team, away_team]
        shuffle(teams)
        return teams[0]

