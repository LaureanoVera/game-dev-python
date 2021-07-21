import pygame, sys
from pygame.locals import *
pygame.init()

# SETTINGS
clock = pygame.time.Clock()
SIZE = (800, 500)
pygame.display.set_caption('Pygame Window')
screen = pygame.display.set_mode(SIZE, 0,32)

# PLAYER
player_image = pygame.image.load('pygame-course/char.png')
moving_left = False
moving_right = False
player_location = [50, (SIZE[1] - 50)]

# GAME LOOP
while True:
  screen.fill((46, 144, 155))
  screen.blit(player_image, player_location)

  if moving_left == True:
    player_location[0] -= 3
  if moving_right == True:
    player_location[0] +=3

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.quit()
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        moving_left = True
      if event.key == pygame.K_d:
        moving_right = True

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        moving_left = False
      if event.key == pygame.K_d:
        moving_right = False


  # UPDATE
  pygame.display.update()
  clock.tick(60)