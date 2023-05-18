"""
Snake Eater
Made with PyGame
"""

import pygame
import random
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
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    snake.change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    snake.change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    snake.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    snake.change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if snake.change_to == 'UP' and snake.direction != 'DOWN':
            snake.direction = 'UP'
        if snake.change_to == 'DOWN' and snake.direction != 'UP':
            snake.direction = 'DOWN'
        if snake.change_to == 'LEFT' and snake.direction != 'RIGHT':
            snake.direction = 'LEFT'
        if snake.change_to == 'RIGHT' and snake.direction != 'LEFT':
            snake.direction = 'RIGHT'

        # Moving the snake
        if snake.direction == 'UP':
            snake.position[1] -= 10
        if snake.direction == 'DOWN':
            snake.position[1] += 10
        if snake.direction == 'LEFT':
            snake.position[0] -= 10
        if snake.direction == 'RIGHT':
            snake.position[0] += 10

        # Snake body growing mechanism
        snake.body.insert(0, list(snake.position))
        if snake.position[0] == food.position[0] and snake.position[1] == food.position[1]:
            snake.score += 1
            food.spawn = False
        else:
            snake.body.pop()

        # Spawning food on the screen
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
