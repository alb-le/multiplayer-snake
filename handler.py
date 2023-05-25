"""
Snake Eater
Made with PyGame
"""

import pygame
import sys

from core import config
from core.render import Render
from models.food import Food
from models.snake import Snake


def main():
    render = Render()

    # FPS (frames per second) controller
    fps_controller = pygame.time.Clock()

    snake = Snake()
    food = Food()

    # Main logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                snake.change_direction(event)

        snake.move(food)
        if not food.spawn:
            food.spawn_new_food()

        render.draw_snakes(snake.body)
        render.draw_food(food.position)

        # Game Over conditions
        # Getting out of bounds
        if snake.position[0] < 0 or snake.position[0] > config.frame_size_x-10:
            render.game_over(snake.score)
        if snake.position[1] < 0 or snake.position[1] > config.frame_size_y-10:
            render.game_over(snake.score)
        # Touching the snake body
        for block in snake.body[1:]:
            if snake.position[0] == block[0] and snake.position[1] == block[1]:
                render.game_over(snake.score)

        render.show_score(snake.score, 1, config.white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(config.difficulty)


if __name__ == '__main__':
    main()
