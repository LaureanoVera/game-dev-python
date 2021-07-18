import pygame
import sys
pygame.init()

# --- COLORS
dark = (23, 29, 50)
blue = (20, 170, 250)

# --- CONFIG
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('The GAME?')
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

# --- GAME VARS
points = 0

# 

# --- GAME LOOP
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      sys.exit()

  # --- MOUSE
  mouse = pygame.mouse.get_pos()
  x = mouse[0]
  y = mouse[1]

  # --- BG COLOR
  screen.fill(dark)

  # --- PLAYER
  pygame.draw.circle(screen, blue, (x, y), 20)

  # --- UPDATE
  pygame.display.flip()
  clock.tick(50)