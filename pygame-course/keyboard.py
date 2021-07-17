import pygame
import sys
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 255, 0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_x = 10
coor_y = 10

speed_x = 0
speed_y = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

        # Keyboard Event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed_x = -3
            if event.key == pygame.K_d:
                speed_x = 3
            if event.key == pygame.K_w:
                speed_y = -3
            if event.key == pygame.K_s:
                speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed_x = 0
            if event.key == pygame.K_d:
                speed_x = 0
            if event.key == pygame.K_w:
                speed_y = 0
            if event.key == pygame.K_s:
                speed_y = 0

    screen.fill(black)
    coor_x += speed_x
    coor_y += speed_y
    pygame.draw.rect(screen, blue, (coor_x, coor_y, 100,100))
    pygame.display.flip()
    clock.tick(50)
