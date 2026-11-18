import os
import sys
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
        ['#', "W - Move Inter ", '*'],
        ['#', "W - Move Forward ", '*'],
        ['*', '###################', '*']
        ]