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

# --- GAME LOOP
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      sys.exit()

  # --- BG COLOR
  screen.fill(dark)

  # --- UPDATE
  pygame.display.flip()
  clock.tick(50)