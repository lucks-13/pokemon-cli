import os
import sys
import copy
from termcolor import colored
import world

menu = [['*', '###################', '*'],
        ['#', ' ','Help ','#'],
        ['#', ' ','Pokedex ','#'],
        ['#', ' ','Pokemon ','#'],
        ['#', ' ','Return to the Game ','#'],
        ['#', ' ','Exit Game ','#'],
        ['*', '###################', '*']
        ]

options = {
    'help' : 1,
    'pokedex' : 2,
    'pokemon' : 3,
    'bckgame' : 4,
    'exit' : 5
}

help = [['*', '###################', '*'],
        ['#', "W - Move Forward ", '*'],
        ['#', "S - Move Backward ", '*'],
        ['#', "A - Move Left ", '*'],
        ['#', "D - Move Right ", '*'],
        ['#', "E - Interact ", '*'],
        ['#', "M - Open the Menu ", '*'],
        ['*', '###################', '*']
        ]

cursor_x = 1
cursor_y = 1
menu[cursor_x][cursor_y] = '>'

def exit_game():
    sys.exit(1)

def p_pokemon():
    print("There are no Pokemon to Display")

def p_menu(menu = menu):
    world.clean_src()
    c_menu = copy.deepcopy(menu)
    for i in c_menu:
        