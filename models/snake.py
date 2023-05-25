import random

import pygame

from core import config


class Snake:
    def __init__(self):
        random_init_position = random.randrange(10, config.frame_size_x, 10)
        self.position = [100, random_init_position]
        self.body = [[100, random_init_position], [100-10, random_init_position], [100-(2*10), random_init_position]]
        self.score = 0
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, event):
        # W -> Up; S -> Down; A -> Left; D -> Right
        if event.key == pygame.K_UP or event.key == ord('w'):
            self.change_to = 'UP'
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            self.change_to = 'DOWN'
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            self.change_to = 'LEFT'
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            self.change_to = 'RIGHT'
        # Esc -> Create event to quit the game
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def move(self, food):
        # Making sure the snake cannot move in the opposite direction instantaneously
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Moving the snake
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10

        # Snake body growing mechanism
        self.body.insert(0, list(self.position))
        if self.position[0] == food.position[0] and self.position[1] == food.position[1]:
            self.score += 1
            food.spawn = False
        else:
            self.body.pop()
