"""
Snake Eater
Made with PyGame
"""

import pygame
import sys

from core import config, client
from core.render import Render
from models.food import food
from models.snake import Snake


def handler():
    render = Render()

    snake = Snake(config.green, 0)

    # Main logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                snake.change_direction(event)

        client.move_snake(snake)
        client.recive_positions()

        render.draw_snakes(snake.body)
        render.draw_food(food.position)

        game_over_conditions = client.check_for_game_over()
        if game_over_conditions:
            client.close_conection()
            render.game_over(snake.score)

        render.show_score(snake.score, 1, config.white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()


if __name__ == '__main__':
    handler()
