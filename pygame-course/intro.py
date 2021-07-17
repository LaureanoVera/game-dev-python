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
# FPS Controller
clock = pygame.time.Clock()

# Coordinate Square
cord_y = 400
cord_x = 200

# Speed square
speed_x = 3
speed_y = 3

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Collisions
    if cord_x > 720 or cord_x < 0:
        speed_x *= -1
    if cord_y > 520 or cord_y < 0:
        speed_y *= -1


    # Animation
    cord_x += speed_x
    cord_y += speed_y
    
    # ---- Logic ----
    # ---- Logic ----
    
    # BG Color
    screen.fill(WHITE)

    # ---- Draw Zone ----
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
    # ---- Draw Zone ----

    # Update Screen
    pygame.display.flip()
    clock.tick(60)
