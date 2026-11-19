from .g_utils import alpha_blend

def get_ansi_color_for_rgb(rgb):
    red_level = int(round((rgb[0] / 255.0) * 5))
    green_level = int(round((rgb[1] / 255.0) * 5))
    blue_level = int(round((rgb[2] / 255.0) * 5))
    return int((red_level * 36) + (green_level * 6) + blue_level + 16)

def get_ansi_f_code(ansi_color):
    return ['38', '5', str(ansi_color)]

def get_ansi_b_code(ansi_color):
    return ['48', '5', str(ansi_color)]

def get_ansi_b_seq(ansi_color):
    return "\x1b[" + ";".join(get_ansi_b_code(ansi_color)) + "m"

def gen_ansi_c_seq(curr_fg_color, curr_bg_color, new_fg_color, new_bg_color):
    color_codes = []
    if new_bg_color != curr_bg_color:
        if new_bg_color is None:
            color_codes.append('49')
        else:
            color_codes += get_ansi_b_code(new_bg_color)
    if new_fg_color != curr_fg_color:
        if new_fg_color is None:
            color_codes.append('39')
        else:
            color_codes += get_ansi_f_code(new_fg_color)
    if len(color_codes) > 0:
        return "\x1b[" + ";".join(color_codes) + "m"
    else:
        return ""

def gen_opt_y_move_down_to_x_sol(v_dist):
    ansi_seq = "\x1b[{0}E".format(v_dist)
    if v_dist < len(ansi_seq):
        ansi_seq = '\n' * v_dist

def gen_ansi_to_c_movement(curr_x, curr_y, target_x, target_y):
    ansi_seq = ""
    if curr_y < target_y:
        v_dist = target_y - curr_y
        if curr_x == target_x:
            if target_x != 0:
                return "\x1b[{0}B".format(v_dist)
            else:
                return gen_opt_y_move_down_to_x_sol(v_dist)
        else:
            if target_x != 0:
                ansi_seq += gen_opt_y_move_down_to_x_sol(v_dist)
                curr_x = 0
            else:
                return gen_opt_y_move_down_to_x_sol(v_dist)
    elif curr_y > target_y:
        if target_x == 0:
            return "\x1b[{0}F".format(curr_y - target_y)
        else:
            ansi_seq += "\x1b[{0}A".format(curr_y - target_y)
    if curr_x < target_x:
        ansi_seq += "\x1b[{0}C".format(target_x - curr_x)
    elif curr_x > target_x:
        ansi_seq += "\x1b[{0}D".format(curr_x - target_x)
    return ansi_seq

def gen_pixels_to_ansi(pixels, width, height, bg_rgba, current):