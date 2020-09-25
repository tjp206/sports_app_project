import pdb
from models.game import Game
from models.result import Result
from models.team import Team
import repositories.games_repo as games_repo
import repositories.results_repo as results_repo
import repositories.teams_repo as teams_repo


game_1 = Game("Super Bowl")
print('Super Bowl')
games_repo.save(game_1)






pdb.set_trace()