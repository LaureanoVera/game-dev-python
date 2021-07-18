import pygame
import sys
pygame.init()

# COLOR
black = (0, 0, 0)
white = (255, 255, 255)

# CONFIG
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# VARS
player_width = 15
player_height = 90
one_x_coor = 50
one_y_coor = (300 - (player_height / 2))
one_speed = 0
two_x_coor = (750 - player_width)
two_y_coor = (300 - (player_height / 2))
two_speed = 0

# GAME LOOP
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # BG COLOR
    screen.fill(black)

    # DRAW ZONE
    player_one = pygame.draw.rect(screen, white, (50, 300-45, player_width, player_height))
    player_two = pygame.draw.rect(screen, white, (750-player_width, 300-45, player_width, player_height))

    # UPDATE
    pygame.display.flip()
    clock.tick(60)

pygame.quit()