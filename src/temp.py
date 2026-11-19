from pokemon_data import *
from .trainer import Trainer, save_game

player = Trainer("Test Trainer")
starter = Pokemon(pokemon_number=1, level=5)
player.append_on_team(starter)
save_game(player, "pokemon_cli_save.json")
print("File Saved.")