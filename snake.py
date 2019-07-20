from pygame.locals import *
import pygame
import time
import random

window_width = 400
window_height = 400
grid_size = 20
num_of_cells = 400 / 20
player_x = 10
player_y = 10
food_x = 15
food_y = 15
trail = []
tail_size = 5
x_velocity = 0
y_velocity = 0
is_running = True

pygame.init()
game_display = pygame.display.set_mode((window_width, window_height))

while is_running:
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            exit()

    if (keys[K_RIGHT]):
        x_velocity = 1
        y_velocity = 0

    if (keys[K_LEFT]):
        x_velocity = -1
        y_velocity = 0

    if (keys[K_UP]):
        x_velocity = 0
        y_velocity = -1

    if (keys[K_DOWN]):
        x_velocity = 0
        y_velocity = 1

    player_x += x_velocity
    player_y += y_velocity

    if (player_x < 0):
        player_x = num_of_cells - 1
    if (player_x > num_of_cells - 1):
        player_x = 0
    if (player_y < 0):
        player_y = num_of_cells - 1
    if (player_y > num_of_cells - 1):
        player_y = 0

    game_display.fill((0, 0, 0))
    for i in range(len(trail)):
        left = trail[i]['x'] * grid_size
        top = trail[i]['y'] * grid_size
        width = height = grid_size - 2
        pygame.draw.rect(game_display, (255, 255, 255), (left, top, width, height))

        if trail[i]['x'] == player_x and trail[i]['y'] == player_y:
            tail_size = 5

    trail.append({'x': player_x, 'y': player_y})
    while (len(trail) > tail_size):
        trail.pop(0)

    if (food_x == player_x and food_y == player_y):
        tail_size += 1
        food_x = int(random.random() * num_of_cells)
        food_y = int(random.random() * num_of_cells)

    left = food_x * grid_size
    top = food_y * grid_size
    width = height = grid_size - 2
    pygame.draw.rect(game_display, (255, 0, 0), (left, top, width, height))
    pygame.display.flip()

    time.sleep(60.0 / 1000.0)
    