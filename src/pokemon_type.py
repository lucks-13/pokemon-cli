steel = 0
water = 1
bug = 2
dragon = 3
electric = 4
ghost = 5
fire = 6
fairy = 7
ice = 8
fight = 9
normal = 10
grass = 11
psychic = 12
rock = 13
dark = 14
land = 15
poison = 16
fly = 17
no_type = 18

type_name = {
    steel : 'Steel',
    water : 'Water',
    bug : 'Bug',
    dragon : 'Dragon',
    electric : 'Electric',
    ghost : 'Ghost',
    fire : 'Fire',
    fairy : 'Fairy',
    ice : 'Ice',
    fight : 'Fight',
    normal : 'Normal',
    grass : 'Grass',
    psychic : 'Psychic',
    rock : 'Rock',
    dark : 'Dark',
    land : 'Land',
    poison : 'Poison',
    fly : 'Fly',
    no_type : '-'
}

t_name_i = {
    'steel' : steel,
    'water' : water,
    'bug' : bug,
    'dragon' : dragon,
    'electric' : electric,
    'ghost' : ghost,
    'fire' : fire,
    'fairy' : fairy,
    'ice' : ice,
    'fight' : fight,
    'normal' : normal,
    'grass' : grass,
    'psychic' : psychic,
    'rock' : rock,
    'dark' : dark,
    'land' : land,
    'poison' : poison,
    'fly' : fly,
    '-' : no_type
}

physical = 0
special = 1
no_category = 2

category_name = {
    physical : 'Physical',
    special : 'Special',
    no_category : '-'
}

c_name_i = {
    'physical' : physical,
    'special' : special,
    '-' : no_category
}

female = 0
male = 1
girl = 2
boy = 3
no_gender = 4

g_name = {
    female : 'Female',
    male : 'Male',
    girl : 'Girl',
    boy : 'Boy',
    no_gender : '-'
}

g_name_i = {
    'female' : female,
    'male' : male,
    'girl' : girl,
    'boy' : boy,
    '-' : no_gender
}

bool_s = {
    True : 'Yes',
    False : 'No'
}

type_effect = {
    0 : [0.5, 0.5, 1, 1, 0.5, 1, 0.5, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    1 : [1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 1, 0.5, 1, 2, 1, 2, 1, 1],
    2 : [0.5, 1, 1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 2, 1, 2, 1, 0.5, 0.5],
    3 : [0.5, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    4 : [1, 2, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 2],
    5 : [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 2, 1, 0.5, 1, 1, 1],
    6 : [2, 0.5, 2, 0.5, 1, 1, 0.5, 1, 2, 1, 1, 2, 1, 0.5, 1, 1, 1, 1],
    7 : [0.5, 1, 1, 2, 1, 1, 0.5, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
    8 : [0.5, 0.5, 1, 2, 1, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 2, 1, 2],
    9 : [2, 1, 0.5, 1, 1, 0, 1, 0.5, 2, 1, 2, 1, 0.5, 2, 2, 1, 0.5, 0.5],
    10 : [0.5, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1],
    11 : [0.5, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 2, 1, 2, 0.5, 0.5],
    12 : [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1, 0, 1, 2, 1],
    13 : [0.5, 1, 2, 1, 1, 1, 2, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 2],
    14 : [1, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 0.5, 1, 1, 1],
    15 : [2, 1, 0.5, 1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 2, 0],
    16 : [0, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 1],
    17 : [0.5, 1, 2, 1,0.5, 1, 1, 1, 1, 2, 1, 2, 1, 0.5, 1, 1, 1, 1]
}

def list_to_string(items, row_count, col_count, display_width):
    f_list = ""
    for row_index in range(0, row_count):
        for col_index in range(0, int(col_count / 2)):
            if row_index == 0:
                f_list += (str(col_index) + ') ' + items[col_index].display_line(display_width)[row_index]).ljust(display_width) + '\t'
            else:
                f_list += (items[col_index].display_line(display_width)[row_index]).ljust(display_width) + '\t'
        f_list += '\n'
    f_list += '\n'
    for row_index in range(0, row_count):
        for col_index in range(int(col_count / 2), col_count):
            if row_index == 0:
                f_list += (str(col_index) + ') ' * items[col_index].display_line(display_width)[row_index]).ljust(display_width) + '\t'
            else:
                f_list += (items[col_index].display_line(display_width)[row_index]).ljust(display_width) + '\t'
        f_list += '\n'
    return f_list