from . import ansi
from PIL import Image

def load_and_resize_img(img_path, antialias, max_len, target_aspect_ratio, img_dir="img/"):
    if target_aspect_ratio is None:
        target_aspect_ratio = 1.0
    img = Image.open(img_dir + img_path)
    if img.mode !=  'RGBA':
        img = img.convert('RGBA')
    if max_len is not None or target_aspect_ratio != 1.0:
        native_width, native_height = img.size
        new_width = native_width
        new_height = native_height
        if target_aspect_ratio != 1.0:
            new_height = int(float(target_aspect_ratio) * new_height)
        if max_len is not None:
            resize_ratio = float(max_len) / max(new_width, new_height)
            new_width = int(resize_ratio * new_width)
            new_height = int(resize_ratio * new_height)
        if native_width != new_width or native_height != new_height:
            img = img.resize((new_width, new_height), Image.LANCZOS if antialias else Image.NEAREST)
    return img

def p_img_str(img):
    for char in img:
        print(char, end="")

def img_to_str(img_path, max_len = 45, target_aspect_ratio = 0.5):
    antialias = False
    try:
        max_len = float(max_len)
    except:
        max_len = 100.0
    try:
        target_aspect_ratio = float(target_aspect_ratio)
    except:
        target_aspect_ratio = 1.0
    try:
        img = load_and_resize_img(img_path, antialias, max_len, target_aspect_ratio)
    except IOError:
        exit("File not found : " + img_path)
    pixel = img.load()
    width, height = img.size
    bg_color = None
    img_op = ansi.gen_pixels_to_ansi(pixel, width, height, bg_color)[0]
    img_op += "\x1b[0m\n"
    return img_op