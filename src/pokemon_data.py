from numpy import random
from pokemon_type import *
from moves_db import *
import json

legendary_pokemon = {
    'arceus', 'articuno', 'azelf', 'celebi', 'cresselia', 'darkai', 'deoxys', 'dialga', 'entei', 'giratina', 'groudon', 'heatran', 'ho-oh', 'jirachi', 'kyogre', 'latias', 'latios', 'lugia', 'manaphy', 'mesprit', 'mew', 'mewtwo', 'moltres', 'palkia', 'phione', 'raikou', 'rayquaza', 'regice', 'regigigas', 'regirock', 'registeel', 'shaymin', 'suicune', 'uxie', 'zapdos'
    }


pokemon_db = {
    0 : 'Missing-No',
    1 : 'Balbasaur',
    2 : 'Kyogre',
    3 : 'Groudon'
}

pokemon_t_by_id {
    0 : normal,
    1 : grass,
    2 : water,
    3 : land
}

class Pokemon:
    def attack_1(self, opponent):
        available_moves = [0, 1, 2, 3]
        for i in range(0, 4):
            if self.moves[i].pp == 0:
                available_moves.remove(i)

        if len(available_moves) == 0:
            self.attack(opponent, -1)
            return 'tackle_a'
        
        else:
            sel_move = available_moves[random.randint(0, len(available_moves))]
            self.attack(opponent, sel_move)
            return str(self.moves[sel_move].name).lower().replace(" ", "_")

    def restore_move_pp(self, move_index, restore_pp=100):
        if(self.moves[move_index].pp + restore_pp) > self.moves[move_index].pp_max:
            self.moves[move_index].pp = self.moves[move_index].pp_max
        
        else:
            self.moves[move_index].pp += restore_pp

    def set_moves(self, move_list):
        if len(move_list) <= 4:
            self.moves = move_list

    def __str__(self):
        pokemon_details = ""
        moves_details = ""

        if len(self.moves) != 0:
            moves_details = list_to_string(self.moves, 8, len(self.moves), 24)

            pokemon_details = (
                ""
            )