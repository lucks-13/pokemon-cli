from g_utils import alpha_blend

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
    return ansi_seq

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

def gen_pixels_to_ansi(pixels, width, height, bg_rgba, current_ansi_colors = None, curr_c_pos = None, get_pixel_func = None, is_overdraw = False, x_offset = 0):
    if get_pixel_func is None:
        get_pixel_func = lambda pixels, x, y : (" ", pixels[x, y])
    if bg_rgba is not None:
        bg_ansi_color = get_ansi_color_for_rgb(bg_rgba)
        bg_ansi_seq = get_ansi_b_seq(bg_ansi_color)
    else:
        bg_ansi_color = None
        bg_ansi_seq = "\x1b[49m"
    if current_ansi_colors is not None:
        ansi_seq = ""
        pre_fg_color = current_ansi_colors['fg']
        pre_bg_color = current_ansi_colors['bg']
    else:
        ansi_seq = "\x1b[0m"
        pre_fg_color = None
        pre_bg_color = None
    if curr_c_pos is not None:
        cursor_x = curr_c_pos['x']
        cursor_y = curr_c_pos['y']
    else:
        cursor_x  = 0
        cursor_y  = 0

    for row_index in range(height):
        for col_index in range(width):
            draw_char, pixel_rgba = get_pixel_func(pixels, col_index, row_index)
            skip_pixel = False
            if draw_char is not None:
                alpha = pixel_rgba[3]
                if alpha == 0:
                    skip_pixel = True
                elif alpha != 255 and bg_rgba is not None:
                    pixel_rgba = alpha_blend(pixel_rgba, bg_rgba)
            if not skip_pixel:
                rgb = pixel_rgba[:3]
                if draw_char is None:
                    draw_char = " "
                    ansi_color = bg_ansi_color
                else:
                    ansi_color = get_ansi_color_for_rgb(rgb)
                    if not is_overdraw and (draw_char == " ") and (ansi_color == bg_ansi_color):
                        skip_pixel = True
                if not skip_pixel:
                    if len(draw_char) > 1:
                        raise ValueError("Not allowing Multi Character draw Strings")
                    offset_x = x_offset + col_index
                    if (cursor_x != offset_x) or (cursor_y != row_index):
                        ansi_seq += gen_ansi_to_c_movement(cursor_x, cursor_y, offset_x, row_index)
                        cursor_x = offset_x
                        cursor_y = row_index
                    if draw_char == " ":
                        ansi_seq += gen_ansi_c_seq(pre_fg_color, pre_bg_color, pre_fg_color, ansi_color)
                        pre_bg_color = ansi_color
                    else:
                        ansi_seq += gen_ansi_c_seq(pre_fg_color, pre_bg_color, ansi_color, bg_ansi_color)
                        pre_fg_color = ansi_color
                        pre_bg_color = bg_ansi_color
                    ansi_seq += draw_char
                    cursor_x += 1
        if (row_index + 1) != height:
            if not is_overdraw:
                if pre_bg_color != bg_ansi_color:
                    ansi_seq += bg_ansi_seq
                    pre_bg_color = bg_ansi_color
                if cursor_y != row_index:
                    ansi_seq += gen_ansi_to_c_movement(0, cursor_y, 0, row_index)
                    cursor_y = row_index
                ansi_seq += '\n'
                cursor_y += 1
                cursor_x = 0
    return ansi_seq, {
        'fg' : pre_fg_color,
        'bg' : pre_bg_color,
        'x' : cursor_x,
        'y' : cursor_y
    }