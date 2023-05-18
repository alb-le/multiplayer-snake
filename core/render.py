import sys
import time

import pygame

from core import config


class Render:

    def __init__(self):
        # Checks for errors encountered
        check_errors = pygame.init()
        # pygame.init() example output -> (6, 0)
        # second number in tuple gives number of errors
        if check_errors[1] > 0:
            print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
            sys.exit(-1)
        else:
            print('[+] Game successfully initialised')

        # Initialise game window
        pygame.display.set_caption('Jogo das Cobrinhas')
        self.game_window = pygame.display.set_mode((config.frame_size_x, config.frame_size_y))

    def game_over(self, score: int):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, config.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (config.frame_size_x/2, config.frame_size_y/4)
        self.game_window.fill(config.black)
        self.game_window.blit(game_over_surface, game_over_rect)
        self.show_score(score, 0, config.red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def show_score(self, score: int, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (config.frame_size_x / 10, 15)
        else:
            score_rect.midtop = (config.frame_size_x / 2, config.frame_size_y / 1.25)
        self.game_window.blit(score_surface, score_rect)
        # pygame.display.flip()

    def draw_snakes(self, snake_body):
        self.game_window.fill(config.black)
        for pos in snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(self.game_window, config.green, pygame.Rect(pos[0], pos[1], 10, 10))

    def draw_food(self, food):
        # Snake food
        pygame.draw.rect(self.game_window, config.white, pygame.Rect(food[0], food[1], 10, 10))