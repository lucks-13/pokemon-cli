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
            "\t HP : " + str(self.hp) + '/' + str(self.max_hp),
            "-" * display_width
        ]

    def __init__(self, pokemon_number=0, level=5, trainer_id=0):
        if pokemon_number in pokemon_db:
            self.name = pokemon_db[pokemon_number]
            self.type = pokemon_t_by_id[pokemon_number]
        else:
            self.name = "Incomplete"
            self.type = no_type
        self.num = pokemon_number
        if level < 5:
            level  = 5
        self.level = level
        self.trainer_id = trainer_id
        self.moves = []
        for i in range(0, 4):
            self.moves.append(move_db[''])
        if self.name.lower() in legendary_pokemon:
            self.gender = no_gender
        else:
            self.gender = random.randint(0, 2)
        self.max_hp = 45
        self.hp = self.max_hp
        self.attack_stat = 49
        self.defense = 65
        self.s_attack = 49
        self.s_defense = 65
        self.speed = 45
        for i in range(5,level):
            self.level_up()

    def restore_hp(self,restore_amount = 2000):
        if(self.hp + restore_amount) > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += restore_amount

    def level_up(self):
        if self.level < 100:
            self.level += 1
            self.max_hp += 1
            self.attack_stat += 1
            self.s_attack += 1
            self.s_defense += 1
            self.speed += 1

    def attack(self, opponent, move_index):
        if move_index == -1:
            selected_move = move_db['tackle_a']
        else:
            selected_move = self.moves[move_index]
        if selected_move.move_type == self.type:
            stab_bonus = 1.5
        else:
            stab_bonus = 1
        effect_multiplier = type_effect[selected_move.move_type][opponent.type]
        random_factor = random.randint(85, 101)
        damage = 0
        if selected_move.category == physical:
            damage = int(0.01 * stab_bonus * effect_multiplier * random_factor * (((0.2 * self.level + 1) * self.attack_stat * selected_move.power) / (25 * opponent.defense) + 2))
        elif selected_move.category == special:
            damage = int(0.01 * stab_bonus * effect_multiplier * random_factor * (((0.2 * self.level + 1) * self.attack_stat * selected_move.power) / (25 * opponent.defense) + 2))
            if opponent.hp <= damage:
                opponent.hp = 0
            else:
                opponent.hp -= damage
            if selected_move.name != 'Tackle A':
                selected_move.pp -= 1

    def restore_all(self):
        self.restore_hp()
        for i in range(0, 4):
            self.restore_move_pp(i)

    def dict_to_pokemon(set_p):
        pokemon_record = set_p
        pokemon_instance = Pokemon(pokemon_record['number'], pokemon_record['level'], pokemon_record['trainer_id'])
        pokemon_instance.type = pokemon_record['type']
        pokemon_instance.gender = pokemon_record['gender']
        pokemon_instance.set_base_stats(pokemon_record['hp'], pokemon_record['attack'], pokemon_record['defense'], pokemon_record['s_attack'], pokemon_record['s_defense'], pokemon_record['speed'])
        moves = []
        for move in pokemon_record['moves']:
            moves.append(dict_to_move(move))
        pokemon_instance.moves = moves
        return pokemon_instance

    def pokemon_format(pokemon_record):
        pokemon_record['number'] = int(pokemon_record['number'])
        pokemon_record['name'] = str(pokemon_record['name']).title()
        pokemon_record['type'] = int(t_name_i[pokemon_record['type'].lower()])
        pokemon_record['hp'] = int(pokemon_record['hp'])
        pokemon_record['attack'] = int(pokemon_record['attack'])
        pokemon_record['defense'] = int(pokemon_record['defense'])
        pokemon_record['s_attack'] = int(pokemon_record['s_attack'])
        pokemon_record['s_defense'] = int(pokemon_record['s_defense'])
        pokemon_record['speed'] = int(pokemon_record['speed'])

    def pokemon_to_dict(pokemon):
        pokemon_data = pokemon
        move_data = []
        for i in range(0, len(pokemon_data.moves)):
            move_data.append(move_to_dict(pokemon_data.moves[i]))
        pokemon_record = {
            'number': pokemon_data.num,
            'name' : pokemon_data.name,
            'type' : pokemon_data.type,
            'level' : pokemon_data.level,
            'trainer_id' : pokemon_data.trainer_id,
            'gender' : pokemon_data.gender,
            'hp' : pokemon_data.max_hp,
            'attack' : pokemon_data.attack_stat,
            'defense' : pokemon_data.defense,
            's_attack' : pokemon_data.s_attack,
            's_defense' : pokemon_data.s_defense,
            'speed' : pokemon_data.speed,
            'moves' : move_data
        }
        return pokemon_record