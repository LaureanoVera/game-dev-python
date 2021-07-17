import pygame
import sys
import random
pygame.init()

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Config
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Coordinates
coor_list = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    coor_list.append([x, y])

# GAME LOOP
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    # BG Color
    screen.fill(black)

    for coor in coor_list:
        pygame.draw.circle(screen, red, coor, 5)
        coor[1]+=1
        if coor[1] > 500:
            coor[1] = 0 


    # Update
    pygame.display.flip()
    clock.tick(30)
