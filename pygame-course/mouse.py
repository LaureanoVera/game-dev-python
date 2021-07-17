import pygame
import sys
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 255, 0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.fill(black)

    pygame.draw.rect(screen, blue, ((x - 50), (y - 50), 100,100))
    pygame.display.flip()
    clock.tick(50)
