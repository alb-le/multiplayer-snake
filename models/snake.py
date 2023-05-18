import random

from core import config


class Snake:
    def __init__(self):
        random_init_position = random.randrange(10, config.frame_size_x, 10)
        self.position = [100, random_init_position]
        self.body = [[100, random_init_position], [100-10, random_init_position], [100-(2*10), random_init_position]]
        self.score = 0
        self.direction = 'RIGHT'
        self.change_to = self.direction
