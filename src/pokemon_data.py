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
        