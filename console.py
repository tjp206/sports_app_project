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

team_1 = Team('New England Patriots', 'Bill Belichick', 2, 1)
print('New England Patriots', 'Bill Belichick', 2, 1)
team_repo.save(team_1)

team_2 = Team('Seattle Seahawks', 'Pete Carroll', 3, 0)
print('Seattle Seahawks', 'Pete Carroll', 3, 0)
team_repo.save(team_2)

team_3 = Team('Dallas Cowboys', 'Mike McCarthy', 1, 2)
print('Dallas Cowboys', 'Mike McCarthy', 1, 2)
team_repo.save(team_3)

team_4 = Team('NY Giants', 'Joe Judge', 0, 3)
print('NY Giants', 'Joe Judge', 0, 3)
team_repo.save(team_4)

player_1 = Player('Russell Wilson', 'QB', 99, team_2)
print('Russell Wilson', 'QB', 99)
player_repo.save(player_1)

player_2 = Player('Cam Newton', 'QB', 92, team_1)
print('Cam Newton', 'QB', 92)
player_repo.save(player_2)

player_3 = Player('Dak Prescott', 'QB', 87, team_3)
print('Dak Prescott', 'QB', 87)
player_repo.save(player_3)

player_4 = Player('Saquon Barkley', 'RB', 88, team_4)
print('Saquon Barkley', 'RB', 88)
player_repo.save(player_4)

game_1 = Game('Play Off', team_3, team_4)
print('Play Off')
game_repo.save(game_1)

game_2 = Game('Super Bowl', team_2, team_1)
print('Super Bowl')
game_repo.save(game_2)

print(game_1.winner(team_1, team_2).name)
print(game_1.winner(team_1, team_2).name)
print(game_1.winner(team_1, team_2).name)


pdb.set_trace()