import pygame
import sys
pygame.init()  # Initialize

size = (800, 500)

# Create Window
screen = pygame.display.set_mode(size)

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
