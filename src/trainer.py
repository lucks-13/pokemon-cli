from numpy import random
from pokemon_type import *
from moves_db import *
from pokemon_data import *
import json

class Trainer:
    def __str__(self):
        text_id = str(self.trainer_id)
        text_gender = str(dict_gender[self.gender])
        text_team = ""
        if len(self.team) == 0:
            text_team = "There are no Pokemon in the Team \n"

        else:
            text_team = list_to_string(self.team, 7, len(self.team), 24)

        return (
            "Name : " + self.name + '\n'
            "Gender : " + text_gender + '\n'
            "ID : " + text_id + '\n'
            "--- Team ---\n" + text_team
        )

    def append_on_team(self, pokemon):
        exit_bool = False
        if pokemon.id_coach == 0:
            pokemon.id_coach = self.trainer_id

        if len(self.team) <= 5:
            self.team.append(pokemon)
            exit_bool = True

        return exit_bool

    def __init__(self, name, gender=Male, t_id = random.randint(1, 2^32), pokemon_team = []):
        self.name = name
        self.gender = gender
        self.trainer_id = t_id
        self.team = pokemon_team

def save_game(trainer, file_path = "pokemon_cli_save.json"):
    team_data = []
    for i in range(0, len(trainer.team)):
        team_data.append(pokemon_to_set(trainer.team[i]))

    save_data = {
        'name' : trainer.name,
        'gender' : trainer.gender,
        'id' : trainer.trainer_id,
        'team' : team_data
    }

    with open(file_path, 'w') as out_file:
        json.dumps(save_data, out_file)

def load_game(file_path="")