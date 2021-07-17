import pygame
import sys
pygame.init()  # Initialize pygame

# Colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)

size = (800, 600)

# Create Window
screen = pygame.display.set_mode(size)

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # BG Color
    screen.fill(WHITE)

    # ---- Draw Zone ----
    pygame.draw.line(screen, GREEN, [0, 0], [800, 600], 3)
    pygame.draw.rect(screen, BLUE, (100, 100, 40, 40))
    pygame.draw.circle(screen, RED, (200, 200), 20)
    # ---- Draw Zone ----

    # Update Screen
    pygame.display.flip()
