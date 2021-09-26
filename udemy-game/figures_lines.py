# IMPORTS
import pygame
import sys
from pygame.locals import *

# INIT
pygame.init()

# SCREEN CONFIG
SIZE = (400, 300)
screen = pygame.display.set_mode(SIZE)

# SCREEN STYLES
pygame.display.set_caption('Game Title')
bg_color = (1, 150, 70)
line_color = (182, 153, 5)

# GAME LOOP
while True:
  screen.fill(bg_color)
  pygame.draw.line(screen, line_color, (20, 30), (140, 100), 10)
  for event in pygame.event.get():
    if event.type == QUIT:
      # QUIT GAME
      pygame.quit()
      sys.exit()
    pygame.display.update()