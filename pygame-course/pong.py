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
# PLAYER ONE
one_x_coor = 50
one_y_coor = (300 - (player_height / 2))
one_speed = 0
# PLAYER TWO
two_x_coor = (750 - player_width)
two_y_coor = (300 - (player_height / 2))
two_speed = 0
# BALL
ball_size = 20
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

# GAME LOOP
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            # PLAYER ONE
            if event.key == pygame.K_w:
                one_speed = -3
            if event.key == pygame.K_s:
                one_speed = 3
            # PLAYER TWO
            if event.key == pygame.K_UP:
                two_speed = -3
            if event.key == pygame.K_DOWN:
                two_speed = 3

        if event.type == pygame.KEYUP:
            # PLAYER ONE
            if event.key == pygame.K_w:
                one_speed = 0
            if event.key == pygame.K_s:
                one_speed = 0
            # PLAYER TWO
            if event.key == pygame.K_UP:
                two_speed = 0
            if event.key == pygame.K_DOWN:
                two_speed = 0
        
    # MOVE
    one_y_coor += one_speed
    two_y_coor += two_speed

    if one_y_coor > (size[1] - player_height) or one_y_coor < 0:
      one_speed = 0

    if two_y_coor > (size[1] - player_height) or two_y_coor < 0:
      two_speed = 0

    # BG COLOR
    screen.fill(black)

    # DRAW ZONE
    player_one = pygame.draw.rect(screen, white, (one_x_coor, one_y_coor, player_width, player_height))
    player_two = pygame.draw.rect(screen, white, (two_x_coor, two_y_coor, player_width, player_height))
    ball = pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))
    
    # UPDATE
    pygame.display.flip()
    clock.tick(60)

pygame.quit()