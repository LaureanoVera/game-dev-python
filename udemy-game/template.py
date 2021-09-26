import pygame
import sys
from pygame.locals import *

pygame.init()

# SCREEN CONFIG
SIZE = (400, 300)
screen = pygame.display.set_mode(SIZE)

# SCREEN STYLES
pygame.display.set_caption('Game Title')
bg_color = (1, 150, 70)

# GAME LOOP
while True:
  screen.fill(bg_color)
  for event in pygame.event.get():
    if event.type == QUIT:
      # QUIT GAME
      pygame.quit()
      sys.exit()
    pygame.display.update()