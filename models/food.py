import random
from typing import Tuple

from core import config


class Food:
    def __init__(self):
        self.position: list = [random.randrange(1, (config.frame_size_x // 10)) * 10, random.randrange(1, (config.frame_size_y // 10)) * 10]
        self.spawn: bool = True

    def spawn_new_food(self):
        self.position = [random.randrange(1, (config.frame_size_x // 10)) * 10, random.randrange(1, (config.frame_size_y // 10)) * 10]
        self.spawn = True


food = Food()
