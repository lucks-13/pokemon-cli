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
        self

        
