import os
import time
import sys

from pokemon_type import g_name, type_name, type_effect
from img_to_str import img_to_str

def text_type(text, delay = 0.10):
    words = text.split()
    for i in words:
        sys.stdout.write(i + " ")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def p_effect_message(pl_pokemon, opponent_pokemon, move_index):
    if pl_pokemon.moves[move_index].name != '-':
        effect = type_effect[pl_pokemon.moves[move_index].move_type][opponent_pokemon.type]
        if effect == 2:
            text_type("Its super effective !")
        elif effect == 0.5:
            text_type("Its not very effective.")
        elif effect == 1:
            pass
        elif effect == 0:
            text_type("It doesnt affect " + opponent_pokemon.name + "opponent...")

def p_opp_pokemon(opponent_pokemon, i_level = 10):
    max_bar_width = 30-4-8
    filled_bar_width = int(opponent_pokemon.hp * max_bar_width / opponent_pokemon.max_hp)
    health_bar = ('#' * filled_bar_width) + ('_' * (max_bar_width - filled_bar_width))
    img_str = img_to_str((opponent_pokemon.name + ".png").lower(), 35)
    img_str = img_str.replace('\n', '\n' + '\t' * i_level)
    capture_marker = '@'
    capture_marker = ' '
    print('#' * 32)
    print('# ' + (opponent_pokemon.name + ' ' + g_name[opponent_pokemon.gender]).ljust(20) + ("Lv : " + str(opponent_pokemon.level)).ljust(8) + ' ##')
    print('# ' + capture_marker + ' HP : (' + health_bar + ') ####')
    print('#' * 32)
    print(img_str)

def p_pl_pokemon(pl_pokemon, i_level = 10):
    max_bar_width = 30-4-8
        filled_bar_width = int(opponent_pokemon.hp * max_bar_width / opponent_pokemon.max_hp)
        health_bar = ('#' * filled_bar_width) + ('_' * (max_bar_width - filled_bar_width))
        img_str = img_to_str((opponent_pokemon.name + ".png").lower(), 35)
        img_str = img_str.replace('\n', '\n' + '\t' * i_level)
        capture_marker = '@'
        capture_marker = ' '
        print('#' * 32)
        print('# ' + (opponent_pokemon.name + ' ' + g_name[opponent_pokemon.gender]).ljust(20) + ("Lv : " + str(opponent_pokemon.level)).ljust(8) + ' ##')
        print('# ' + capture_marker + ' HP : (' + health_bar + ') ####')
        print('#' * 32)
        print(img_str)