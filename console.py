import pdb
from models.game import Game
import repositories.game_repo as game_repo



game_1 = Game("Super Bowl")
print('Super Bowl')
game_repo.save(game_1)






pdb.set_trace()