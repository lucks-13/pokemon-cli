import os
import platform
# import fabulous.color import blink, plain
import copy
import menu
from numpy import random
from colored import fg, bg, attr

map = {#  0   1   2   3   4   5   6   7   8   9   10  11
    0 : ['#',' ',' ',' ','#','x','x','#',' ',' ',' ','#'],
    1 : ['#','#','#','#','#',' ',' ','#','#','#','#','#'],
    2 : ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    3 : ['#',' ',' ',' ','*',' ',' ',' ',' ',' ',' ','#'],
    4 : ['#','-','-','-','*','-','-','-',' ',' ',' ','#'],    
    5 : ['*',' ',' ',' ','*','w','w','w','w','w','w','*'],
    6 : ['*',' ',' ',' ','*','w','w','w','w','w','w','*'],
    7 : ['*','-','-','-','*','w','w','w','w','w','w','*'],
    8 : ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
    9 : ['*',' ',' ',' ',' ',' ',' ',' ','w','w','w','*'],
    10 : ['*','#','-','-','-','#','#','#','w','w','w','*'],
    11 : ['#',' ',' ',' ',' ',' ',' ',' ','w','w','w','#'],
    12 : ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    13 : ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    14 : ['#',' ','-','-',' ','-','-','-','-','-','-','#'],
    15 : ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    16 : ['#',' ',' ',' ',' ',' ',' ','w','w','w',' ','#'],
    17 : ['#','*','*','*','*','*','*','w','w','w','-','#'],
    18 : ['#',' ',' ',' ',' ',' ',' ','w','w','w',' ','#'],
    19 : ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
    20 : ['#','-',' ',' ','i','-','-','-','-','-','-','#'],
    21 : ['*',' ','w','w','w',' ',' ',' ','w','w','w','*'],
    22 : ['*','w','w','w',' ',' ',' ','w','w','w',' ','*'],
    23 : ['*','#','#','#','#','w','w','#','#','#','#','*'],
    24 : ['*',' ',' ',' ','#','w','w','#',' ',' ',' ','*'],
    25 : ['*',' ',' ',' ','#','x','x','#',' ',' ',' ','*'],
}

b_cell = {
    'wall' : '#',
    'tree' : '*',
    'close' : 'x',
    'jump' : '-',
    'post' : 'i',
    'player' : '@'
}

elements = {
    'empty' : ' ',
    'herb' : 'w',
    **b_cell
}

l_step = elements['empty']
p_x = 22
p_y = 6
map[p_x][p_y] = elements['player']

def clean_scr():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def p_map(map):
    for i in range(len(map)):
        print(" ".join(map[i]))

def map_color(map):
    c_map = copy.deepcopy(map)
    for i in range(len(map)):
        for col in  range(len(map[0])):
            if map[i][col] == elements['wall']:
                c_map[i][col] = fg('white') + map[i][col] + attr(0)

            elif map[i][col] == elements['tree']:
                c_map[i][col] = fg('light_green') + map[i][col] + attr(0)

            elif map[i][col] == elements['herb']:
                c_map[i][col] = fg('dark_green') + map[i][col] + attr(0)

            elif map[i][col] == elements['jump']:
                c_map[i][col] = fg('light_grey') + map[i][col] + attr(0)

            elif map[i][col] == elements['close']:
                c_map[i][col] = fg('red') + map[i][col] + attr(0)

            elif map[i][col] == elements['post']:
                c_map[i][col] = fg('yellow') + map[i][col] + attr(0)

            elif map[i][col] == elements['player']:
                c_map[i][col] = fg('blue') + map[i][col] + attr(0)

    return c_map

def update_map(map):
    clean_scr()
    p_map(map_color(map))

def next_move(map):
    global p_x
    global p_y
    global l_step
    l_battle = False
    while True:
        key_pressed = input()
        player_move = False
        if key_pressed == 'w':
            if map[p_x -1][p_y] in (elements['empty'], elements['herb']):
                map[p_x][p_y] = l_step
                l_step = map[p_x -1][p_y]
                p_x = p_x -1
                map[p_x][p_y] = elements['player']
                player_move = True

        elif key_pressed == 's':
            if map[p_x +1][p_y] in (elements['empty'], elements['herb']):
                map[p_x][p_y] = l_step
                l_step = map[p_x +1][p_y]
                p_x = p_x +1
                map[p_x][p_y] = elements['player']
                player_move = True

        elif map[p_x +1][p_y] is elements['jump']:
            map[p_x][p_y] = l_step
            l_step = map[p_x +2][p_y]
            p_x = p_x +2
            map[p_x][p_y] = elements['player']
            player_move = True

        elif key_pressed == 'a':
            if map[p_x][p_y -1] in (elements['empty'], elements['herb']):
                map[p_x][p_y] = l_step
                l_step = map[p_x][p_y -1]
                p_y = p_y -1
                map[p_x][p_y] = elements['player']
                player_move = True

        elif key_pressed == 'd':
                if map[p_x][p_y +1] in (elements['empty'], elements['herb']):
                    map[p_x][p_y] = l_step
                    l_step = map[p_x][p_y +1]
                    p_y = p_y +1
                    map[p_x][p_y] = elements['player']
                    player_move = True

        elif key_pressed == 'e':
            c_cell = map[p_x -1][p_y]
            if c_cell is elements['post']:
                print("Trainer Tips !", end="")
                input()
                print("To Enter the Menu, Press M", end="")
                input()

            elif c_cell is elements['herb']:
                print("This is a patch of tall Grass", end="")
                input()
                print("Wild Pokemon might appear !", end="")
                input()

            elif c_cell is elements['wall']:
                print("There is a Wall Ahead", end="")
                input()

            elif c_cell is elements['jump']:
                print("I can Jump this from other side", end="")
                input()

            elif c_cell is elements['tree']:
                print("Its a Tree", end="")

            elif c_cell is elements['close']:
                print("The Path is blocked", end="")
                input()
            
            update_map(map)

        elif key_pressed == 'm':
            menu.next_move()
        
        update_map(map)
        if player_move and l_step is elements['herb']:
            prob = random.randint(0,10)

            if prob < 2:
                if l_battle is True:
                    l_battle = False

                else:
                    print("A Wild Pokemon appeared")
                    input()
                    l_battle = True
        