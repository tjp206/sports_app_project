class Team:
    def __init__(self, name, coach, wins, losses, id = None):
        self.name = name
        self.coach = coach
        self.wins = []
        self.losses = []
        self.id = id