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
                "Name : " + self.name + '\n'
                "Number : " + str(self.num) + '\n'
                "Type : " + type_name[self.type] + '\n'
                "Wild : " + bool_s[(self.trainer_id == 0)] + '\n'
                "Trainer ID : " + str(self.trainer_id) + '\n'
                "Gender : " + str(g_name[self.gender]) + '\n'
                "--- Stats ---\n"
                "Level : " + str(self.level) + '\n'
                "HP : " + str(self.hp) + '\n'
                "Max HP : " + str(self.max_hp) + '\n'
                "Attack : " + str(self.attach_stat) + '\n'
                "Special Attack : " + str(self.s_attqch) + '\n'
                "Defence : " + str(self.defense) + '\n'
                "Special Defence : " + str(self.s_defense) + '\n'
                "Speed : " + str(self.speed) + '\n'
                "------------------------------------------\n"
                "--- Moves ---\n" + moves_details + '\n'
            )

        return pokemon_details

    def set_base_stats(self, max_hp, attack, defense, s_attack, s_defence, speed):
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.attack_stat = attack
        self.defense = defense
        self.s_attack = s_attack
        self.s_defense = s_defence
        self.speed = speed

        for i in range(s, self.level):
            self.level_up()

    def learn_moves(self, new_move):
        move_learned = False

        for i in range(0, 4):
            if self.moves[i].name == '-':
                self.moves[i] = new_move
                move_learned = True
                break

        if not move_learned:
            pass

    def display_line(self, display_width):
        bar_width = display_width - 2
        fill_width = int(self.hp * bar_width / self.max_hp)
        hp_bar = ('#' * fill_width) + ('_' * (bar_width - fill_width))
        if self.gender == no_gender:
            gender_label = ""
        
        else:
            gender_label = str(g_name[self.gender])

        return [
            self.name + " " + gender_label,
            "-" * display_width,
            "Level : " + str(self.level),
            "Type : " + type_name[self.types],
            "(" + hp_bar + ")",
            

        ]
        
