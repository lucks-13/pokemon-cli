from pokemon_type import *

class Move:
    def display_line(self, display_width):
        return [
            self.name,
            "-" * display_width,
            "Type : " + type_name[self.move_type],
            "Category : "+ category_name[self.category] 
        ]