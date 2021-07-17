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
    for x in range(100, 700, 100):
      pygame.draw.rect(screen, BLACK, (x, 275, 50, 50))
      pygame.draw.line(screen, GREEN, (x, 0), (x, 100), 5)
    # pygame.draw.line(screen, GREEN, [0, 0], [800, 600], 3)
    # pygame.draw.rect(screen, BLUE, (x, y, tam, tam))
    # pygame.draw.circle(screen, RED, (200, 200), 20)
    # ---- Draw Zone ----

    # Update Screen
    pygame.display.flip()
