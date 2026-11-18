from pokemon_type import *

class Move:
    def display_line(self, display_width):
        return [ self.name, "-" * display_width, "Type : " + type_name[self.move_type], "Category : " + category_name[self.category], "Power : " + str(self.power), "Accuracy : " + str(self.accuracy), "PP" : str(self.pp) + "/" + str(self.pp_max), "-" * display_width ]

    def __str__(self):
        return '\n'.join(self.display_line())

    def __init__(self, name = "-", move_type = no_type, category = no_category, power = 0, accuracy = 0, max_pp = 0):
        self.name = name
        self.move_type = move_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp_max = max_pp
        self.pp = self.pp_max

def dict_to_move(set_m):
    move_data = set_m
    
    return Move(move_data['name'], move_data['type'], move_data['category'], move_data['power'], move_data['accuracy'], move_data['pp'])

def format_move(move_data):
    move_data['name'] = str(move_data['name']).title()
    move_data['type'] = int(t_name_i[move_data['type'].lower()])
    move_data['category'] = int(c_name_i[move_data['category'].lower()])
    move_data['power'] = int(move_data['power'])
    if move_data['accuracy'] == '-':
        move_data['accuracy'] = int(100)

    else:
        move_data['accuracy'] = int(move_data['accuracy'])

    move_data['pp'] = int(move_data['pp'])

def move_to_

        
