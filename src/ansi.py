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