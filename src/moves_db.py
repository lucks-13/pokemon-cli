from pokemon_type import *

class Move:
    def display_line(self, display_width):
        return [
            self.name,
            "-" * display_width,
            "Type : " + type_name[self.move_type],
            "Category : " + category_name[self.category],
            "Power : " + str(self.power),
            "Accuracy : " + str(self.accuracy),
            "PP" : str(self.pp) + "/" + str(self.pp_max),
            "-" * display_width 
        ]