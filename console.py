import pdb
from models.game import Game
import repositories.game_repo as game_repo

from models.team import Team
import repositories.team_repo as team_repo

from models.result import Result
import repositories.result_repo as result_repo

# game_repo.delete_all()
# team_repo.delete_all()
# result_repo.delete_all()

game_1 = Game("Exhibition")
print('Exhibiton')
game_repo.save(game_1)

game_2 = Game("Super Bowl")
print('Super Bowl')
game_repo.save(game_2)

team_1 = Team('Las Vegas Raiders', 'Jon Gruden', 2, 0)
print('Las Vegas Raiders', 'Jon Gruden', 2, 0)
team_repo.save(team_1)

team_2 = Team('Seattle Seahawks', 'Pete Carroll', 2, 0)
print('Seattle Seahawks', 'Pete Carroll', 2, 0)
team_repo.save(team_2)

result_1 = Result(45, team_1, team_2, game_1)
result_repo.save(result_1)
print(result_1.__dict__)
game_team = team_repo.outcome(team_1)
print(game_team)



pdb.set_trace()