# FPS (frames per second) controller
import pygame

from core import config
from models import snake
from models.food import food


def handler():
    fps_controller = pygame.time.Clock()
    snake.move(food)
    if not food.spawn:
        food.spawn_new_food()

    # Game Over conditions
    # Getting out of bounds
    if snake.position[0] < 0 or snake.position[0] > config.frame_size_x - 10:
        snake.game_over = True
    if snake.position[1] < 0 or snake.position[1] > config.frame_size_y - 10:
        snake.game_over = True
    # Touching the snake body
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            snake.game_over = True

    # Refresh rate
    fps_controller.tick(config.difficulty)
