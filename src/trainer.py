from numpy import random
from .pokemon_type import *
from .moves_db import *
from .pokemon_data import *
import json

class Trainer:
    def __str__(self):
        text_id = str(self.trainer_id)
        text_gender = str(g_name[self.gender])
        text_team = ""
        if len(self.team) == 0:
            text_team = "There are no Pokemon in the Team \n"
        else:
            text_team = list_to_string(self.team, 7, len(self.team), 24)
        return (
            "Name : " + self.name + '\n'
            "Gender : " + text_gender + '\n'
            "ID : " + text_id + '\n'
            "Map : " + str(self.map_1) + '\n'
            "X : " + str(self.x) + '\n'
            "--- Team ---\n" + text_team
        )
    
    def append_on_team(self, pokemon):
        exit_bool = False
        if pokemon.trainer_id == 0:
            pokemon.trainer_id = self.trainer_id
        if len(self.team) <= 5:
            self.team.append(pokemon)
            exit_bool = True
        return exit_bool

    def __init__(self, name, gender=male, t_id = random.randint(1, 2^32), pokemon_team = []):
        self.name = name
        self.gender = gender
        self.trainer_id = t_id
        self.team = pokemon_team
        self.map_1 = "route1"
        self.x = 22
        self.y = 6

def save_game(trainer, file_path = "pokemon_cli_save.json"):
    team_data = []
    for i in range(0, len(trainer.team)):
        team_data.append(pokemon_to_dict(trainer.team[i]))
    save_data = {
        'name' : trainer.name,
        'gender' : trainer.gender,
        'id' : trainer.trainer_id,
        'map_1' : trainer.map_1,
        'p_x' : trainer.x,
        'p_y' : trainer.y,
        'team' : team_data
    }

    with open(file_path, 'w') as out_file:
        json.dump(save_data, out_file)

def load_game(file_path="pokemon_cli_save.json"):
    with open(file_path) as json_file:
        save_data = json.load(json_file)
    team = []
    for pokemon_data in save_data['team']:
        team.append(dict_to_pokemon(pokemon_data))
    trainer = Trainer(save_data['name'], save_data['gender'], save_data['id'], team)
    trainer.map_1 = save_data['map_1']
    trainer.x = save_data['p_x']
    trainer.y = save_data['p_y']
    return trainer