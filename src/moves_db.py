from pokemon_type import *

class Move:
    def display_line(self, display_width):
        return [ 
            self.name, "-" * display_width,
            "Type : " + type_name[self.move_type],
            "Category : " + category_name[self.category], 
            "Power : " + str(self.power),
            "Accuracy : " + str(self.accuracy),
            "PP : "+ str(self.pp) + "/" + str(self.pp_max),
            "-" * display_width
        ]
    
    def __str__(self):
        return '\n'.join(self.display_line(24))

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

def move_to_dict(move):
    move_data = move
    return {
        'name' : move_data.name,
        'type' : move_data.move_type,
        'category' : move_data.category,
        'power' : move_data.power,
        'accuracy' : move_data.accuracy,
        'pp' : move_data.pp_max
    }

move_db = {
    '' : Move("-", no_type, no_category, 0, 0, 0),
    'tackle_a' : Move("Tackle A", normal, physical, 50, 100, 1),
    'tackle_b' : Move("Tackle B", normal, physical, 50, 100, 35),
    'feint' : Move("Feint", normal, physical, 60, 100, 20),
    'flame_thrower' : Move("Flame THrower", normal, physical, 110, 85, 5),
    'solar_beam' : Move("Solar Beam", normal, physical, 120, 100, 10),
    'earthquake' : Move("Earthquake", normal, physical, 100, 100, 10),
    'explosion' : Move("Explosion", normal, physical, 150, 100, 5),
    'blizzard' : Move("Blizzard", normal, physical, 110, 70, 5),
    'surf' : Move("Surf", normal, physical, 90, 100, 15),
    'splash' : Move("Splash", normal, physical, 150, 100, 5),
    'hydro_pump' : Move("Hydro Pump", normal, physical, 110, 80, 5),
    'thunder' : Move("Thunder", normal, physical, 110, 70, 10),
}