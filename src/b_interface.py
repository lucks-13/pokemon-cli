import os
import time
import sys
import random

from pokemon_type import g_name, type_name, type_effect
from img_to_str import img_to_str
from key_input import get_key

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
    print('#' * 37)
    print(img_str)

def p_pl_pokemon(pl_pokemon, i_level = 10):
    max_bar_width = 30-4-8
    filled_bar_width = int(pl_pokemon.hp * max_bar_width / pl_pokemon.max_hp)
    health_bar = ('#' * filled_bar_width) + ('_' * (max_bar_width - filled_bar_width))
    img_str = img_to_str((pl_pokemon.name + "_t.png").lower(), 35)
    status_box = ('\n ' + ('#' * 32) + '\n ## ' + (pl_pokemon.name + ' ' + g_name[pl_pokemon.gender]).ljust(8) + ' #' + '\n #### HP : (' + health_bar + ') #' + '\n' + ('#' * 37))
    print(img_str)
    print(status_box.replace('\n', '\n' + '\t' * i_level))

def b_menu(width = 70):
    print('#' * width)
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print('#' + " 0) Fight".center(int(width / 2 - 2)) + '#' + " 1) Bag".center(int(width / 2 - 1)) + '#')
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print('#' * width)
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print('#' + " 2) Switch Pokemon".center(int(width / 2 - 2)) + '#' + " 3) Run".center(int(width / 2 - 1)) + '#')
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print('#' * width)
    print('Your Choice : ', end="")
    choice = get_key()
    try:
        choice = int(choice)
    except Exception:
        choice = -1
    return choice

def move_selection_menu(pl_pokemon, width = 70):
    pl = pl_pokemon
    print('#' * width)
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print('#' + (' 0) ' + pl.moves[0].name).ljust(int(width / 2 - 2)) + '#' + (" 1) " + pl.moves[1].name).ljust(int(width / 2 - 1)) + '#')
    print('#' + (" " + type_name[pl.moves[0].move_type].ljust(12) + " PP : " + str(pl.moves[0].pp) + "/" + str(pl.moves[0].pp_max)).ljust(int(width / 2 - 2)) + '#' + (" " + type_name[pl.moves[1].move_type].ljust(12) + " PP : " + str(pl.moves[1].pp) + '/' + str(pl.moves[1].pp_max)).ljust(int(width / 2 - 1)) + '#')
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print("#" * width)
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print('#' + (" 2) " + pl.moves[2].name).ljust(int(width / 2 - 2)) + '#' + (" 3) " + pl.moves[3].name).ljust(int(width / 2 - 1)) + '#')
    print('#' + (" " + type_name[pl.moves[2].move_type].ljust(12) + " PP : " + str(pl.moves[2].pp) + '/' + str(pl.moves[2].pp_max)).ljust(int(width / 2 - 2)) + '#' + (" " + type_name[pl.moves[3].move_type].ljust(12) + " PP : " + str(pl.moves[3].pp) + '/' + str(pl.moves[3].pp_max)).ljust(int(width / 2 - 1)) + '#')
    print('#' + (' ' * int(width / 2 - 2)) + '#' + (' ' * int(width / 2 - 1)) + '#')
    print("#" * width)
    print('Your Choice : ', end="")
    choice = get_key()
    try:
        choice = int(choice)
    except Exception:
        choice = -1
    return choice

def a_sel_menu(pl_pokemon, opponent_pokemon):
    pl = pl_pokemon
    opponent = opponent_pokemon
    sel_atk = -1
    atk_id = '-'
    while atk_id == '-':
        b_display(pl, opponent_pokemon)
        try:
            sel_atk = move_selection_menu(pl)
        except Exception:
            sel_atk = -1
        if sel_atk in [0, 1, 2, 3]:
            atk_id = pl.attack(opponent, sel_atk)
    text_type(pl.name + " used " + atk_id + " against Pokemon " + opponent.name + " opponent.")
    time.sleep(0.25)
    p_effect_message(pe, pr, sel_atk)
    get_key()

def b_display(pl_pokemon, opponent_pokemon):
    os.system('clear')
    p_opp_pokemon(opponent_pokemon)
    p_pl_pokemon(pl_pokemon)

def pokemon_fainted(pl_pokemon):
    return pl_pokemon.hp <= 0

def r_b_algo(pl_pokemon, opponent_pokemon, wild_pokemon = True):
    pl = pl_pokemon
    opponent = opponent_pokemon
    sel_menu = 0
    max = 0
    opponent_move_index = 0
    pokemon_fainted = False
    escape_attempts = 0
    while not pokemon_fainted:
        while True:
            b_display(pl, opponent)
            print("what should it do " + pl.name + "?")
            sel_menu = b_menu()
            if sel_menu in [0, 1, 2, 3]:
                break
        if sel_menu == 0:
            while True:
                b_display(pl, opponent)
                print("what should it do " + pl.name + "?")
                max = move_selection_menu(pl)
                if max not in [0, 1, 2, 3]:
                    break
                moves_with_pp = [0, 1, 2, 3]
                for i in range(0, 4):
                    if pl.moves[i].pp == 0:
                        moves_with_pp.remove(i)
                retry = False
                if len(moves_with_pp) == 0:
                    max = -1
                else:
                    if pl.moves[max].pp <= 0:
                        text_type("No PP left for this move !")
                        retry = True
                        get_key()
                if pl.speed > opponent.speed:
                    first = pl
                    second = opponent
                elif pl.speed < opponent.speed:
                    first = opponent
                    second = pl
                else:
                    luck = random.randint(0, 1):
                    if luck == 0:
                        first = pl
                        second = opponent
                    else:
                        first = opponent
                        second = pl
                if not retry:
                    if first == pl:
                        atk_id = pl.attack(opponent, max)
                        escape_attemps = 0
                        text_type(pl.name + " used " + atk_id + ".")
                        get_key()
                        p_effect_message(pl, opponent, max)
                        if opponent.hp <= 0:
                            return 0
                        atk_id = opponent.attack_1(pl)
                        text_type("Pokemon " + opponent.name + " opponent used " + atk_id + ".")
                        get_key()
                        p_effect_message(pl, opponent, max)
                    else:
                        atk_id = opponent.attack_1(pl)
                        if opponent.hp <= 0:
                            return 0
                        if pl.hp <= 0:
                            return -1
                break
        if sel_menu == 1:
            text_type("Bag is not implemented yet.")
            get_key()
        if sel_menu == 2:
            text_type("This is your last Pokemon!")
            get_key()
        if sel_menu == 3:
            if wild_pokemon:
                A = pl.speed
                B = opponent.speed
                C = escape_attemps
                if B == 0:
                    B = 1
                F = ((A * 128) / B + 30 * C) % 256
                escape_success = random.randint(0, 256) < F
                if escape_success:
                    text_type("You escaped without any problems...")
                    get_key()
                    pokemon_fainted = True
                else:
                    text_type("You cannot escape from the battle !")
                    escape_attemps += 1
                    get_key()
            else:
                text_type("You cannot escape from a battle against a trainer !")
                get_key()


def p_trainer(pl_trainer, i_level = 0):
    img_str = img_to_str((g_name[pl_trainer.gender] + '.png').lower())
    img_str = img_str.replace('\n', '\n' + '\t' * i_level)
    print(img_str)

def p_trainer_bs(pl_trainer, i_level = 0):
    img_str = img_to_str((g_name[pl_trainer.gender] + '.png').lower())
    img_str = img_str.replace('\n', '\n' + '\t' * i_level)
    print(img_str)

def get_pokemon_t_marker(t_pokemon):
    pokemon_marker = '@'
    if t_pokemon.name == '-':
        pokemon_marker = 'O'
    elif t_pokemon.hp <= 0:
        pokemon_marker = 'X'
    return str(pokemon_marker)

def trainer_t_box(pl_trainer, orientation = 0, i_level = 0):
    trainer = pl_trainer
    t_marker = ""
    for i in range(0, len(trainer.team)):
        t_marker += get_pokemon_t_marker(trainer.team[i]) + ' '
    e_t_marker = ""
    for i in range(0, 6 - len(trainer.team)):
        e_t_marker += 'O '
    t_marker = e_t_marker + t_marker
    if orientation == 0:
        status_box = ('\n# ' + t_marker.center(30) + '\n' + ('#' * 32))
    else:
        "".join(reversed(t_marker))
        status_box = ('\n' + t_marker.center(31) + '#\n' + ('#' * 32))
    status_box = status_box.replace('\n', '\n' + '\t' * i_level)
    status_box = status_box.replace('@', '\x1b[31m@\x1b[0m')
    status_box = status_box.replace('O', '\x1b[31m@\x1b[0m')
    status_box = status_box.replace('X', '\x1b[31m@\x1b[0m')
    return status_box

def b_wild_pokemon(pl_trainer, opponent_pokemon):
    os.system('clear')
    p_opp_pokemon(opponent_pokemon)
    p_trainer_bs(pl_trainer)
    text_type('\nA Wild Pokemon has appeared !')
    get_key()
    os.system('clear')
    p_opp_pokemon(opponent_pokemon)
    p_trainer_bs(pl_trainer)

    pl_active_pokemon = pl_trainer.get_firs


    selected_pokemon_index = -1
    for i in range(0, len(pl_trainer.team)):
        if pl_trainer.team[i].name != '-' and pl_trainer.team[i].hp > 0:
            selected_pokemon_index = i
            break
    
    
    if selected_pokemon_index == -1:
        print("The trainer has no healthy Pokemon")
    pl_active_pokemon = pl_trainer.team[selected_pokemon_index]
    text_type('\nGo ' + pl_active_pokemon.name + '!')
    input()

def b_trainer(pl_trainer, opponent_trainer):
    trainer = pl_trainer
    opponent = opponent_trainer
    os.system('clear')
    print(trainer_t_box(opponent))
    p_trainer(opponent, 10)
    p_trainer_bs(trainer)
    print(trainer_t_box(trainer,1, 10))
    text_type("\nCool Trainer " + opponent.name + 'Wants to battle !')
    input()
    os.system('clear')
    print(trainer_t_box(opponent))
    p_trainer(opponent, 10)
    p_trainer_bs(trainer)
    print(trainer_t_box(trainer, 1, 10))
    selected_pokemon_index = -1
    for i in range(0, len(trainer.team)):
        if trainer.team[i].name != '-' and trainer.team[i].hp > 0:
            selected_pokemon_index = i
            break
    if selected_pokemon_index == -1:
        print("The Trainer has no Healthy Pokemon")
    pl_active_pokemon = trainer.team[selected_pokemon_index]
    selected_pokemon_index = -1
    for i in range(0, len(opponent.team)):
        if opponent.team[i].name != '-' and opponent.team[i].hp > 0:
            selected_pokemon_index = i
            break
    if selected_pokemon_index == -1:
        print("The Trainer has no Healthy Pokemon")
    opponent_active_pokemon = opponent.team[selected_pokemon_index]
    text_type("\nGo " + pl_active_pokemon.name + "!")
    input()
    os.system('clear')
    print(trainer_t_box(opponent))
    p_trainer(opponent, 10)
    p_pl_pokemon(pl_active_pokemon)
    text_type("\nOpponent trainer " + opponent.name + " sent out " + opponent_active_pokemon.name + "!")
    input()
    os.system('clear')
    p_pl_pokemon(opponent_active_pokemon)
    p_pl_pokemon(pl_active_pokemon)

