from . import ansi
from PIL import Image

def load_and_resize_img(img_path, antialias, max_len, target_aspect_ratio):
    if target_aspect_ratio is None:
        target_aspect_ratio = 1.0
    img = Image.open(img_path)
    if img.mode !=  'RGBA':
        img = img.convert('RGBA')
    if max_len is not None or target_aspect_ratio != 1.0:
        native_width, native_height = img.size
        new_width = native_width
        new_width = native_width