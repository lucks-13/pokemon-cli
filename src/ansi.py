from .g_utils import alpha_blend

def get_ansi_color_for_rgb(rgb):
    red_level = int(round((rgb[0] / 255.0) * 5))
    green_level = int(round((rgb[1] / 255.0) * 5))
    blue_level = int(round((rgb[2] / 255.0) * 5))
    