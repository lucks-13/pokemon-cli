from numpy import random
from pokemon_type import *
from moves_db import *
from pokemon_data import *
import json

class Trainer:
    def __str__(self):
        text_id = str(self.trainer_id)
        text_gender = str(dict_gender[])