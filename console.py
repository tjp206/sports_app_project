import pdb
from models.game import Game
import repositories.game_repo as game_repo

from models.team import Team
import repositories.team_repo as team_repo

from models.player import Player
import repositories.player_repo as player_repo

# game_repo.delete_all()
# player_repo.delete_all()
# team_repo.delete_all()

game_1 = Game("Exhibition")
print('Exhibiton')
game_repo.save(game_1)

game_2 = Game("Super Bowl")
print('Super Bowl')
game_repo.save(game_2)

team_1 = Team('New England Patriots', 'Jon Gruden', 2, 0)
print('New England Patriots', 'Bill Belichick', 2, 0)
team_repo.save(team_1)

team_2 = Team('Seattle Seahawks', 'Pete Carroll', 2, 0)
print('Seattle Seahawks', 'Pete Carroll', 2, 0)
team_repo.save(team_2)

player_1 = Player('Russell Wilson', 'QB', 99, team_2)
print('Russell Wilson', 'QB', 99)
player_repo.save(player_1)

player_2 = Player('Cam Newton', 'QB', 95, team_1)
print('Cam Newton', 'QB', 95)
player_repo.save(player_2)



pdb.set_trace()