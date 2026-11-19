import os
import time
import sys

from pokemon_type import g_name, type_name, type_effect
from img_to_str import img_to_str

def text_type(text, delay = 0.10):
    words = text.split()
    for i in words:
        sys.stdout.write(i + " ")
        sys.stdout.flush