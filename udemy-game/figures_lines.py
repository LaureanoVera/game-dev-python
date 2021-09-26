# IMPORTS
import pygame
import sys
from pygame.locals import *

# INIT
pygame.init()

# SCREEN CONFIG
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)

# SCREEN STYLES
pygame.display.set_caption('Game Title')
bg_color = (33, 29, 44)
line_color = (0, 255, 255)
circle_color = (1, 150, 70)
figure_color = (255, 0, 255)

# GAME LOOP
while True:
  screen.fill(bg_color)
  # LINES
  pygame.draw.line(screen, line_color, (60, 30), (140, 100), 5)
  pygame.draw.line(screen, line_color, (80, 190), (140, 100), 5)
  pygame.draw.line(screen, line_color, (10, 70), (140, 100), 5)
  # CIRCLES
  pygame.draw.circle(screen, circle_color, (400, 280), 60, 10)
  pygame.draw.circle(screen, circle_color, (120, 530), 40, 5)
  # FIGURES
  pygame.draw.rect(screen, figure_color, (170, 170, 180, 180))
  pygame.draw.polygon(screen, figure_color, ((30, 50), (60, 90), (200, 130), (130, 170)))
  for event in pygame.event.get():
    if event.type == QUIT:
      # QUIT GAME
      pygame.quit()
      sys.exit()
    pygame.display.update()