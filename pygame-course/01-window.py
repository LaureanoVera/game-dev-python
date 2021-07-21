import pygame, sys
from pygame.locals import *
pygame.init()

# SETTINGS
clock = pygame.time.Clock()
SIZE = (800, 500)
pygame.display.set_caption('Pygame Window')
screen = pygame.display.set_mode(SIZE, 0,32)

# GAME LOOP
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.quit()

  # UPDATE
  pygame.display.update()
  clock.tick(60)