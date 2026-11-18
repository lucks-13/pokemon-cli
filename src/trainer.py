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
            pokemon.id_coach -