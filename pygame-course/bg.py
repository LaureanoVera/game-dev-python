import pygame, sys
pygame.init()

# CONFIG
size = (624, 279)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False

bg = pygame.image.load('pygame-course/bg.jpg').convert()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill([0,0,0])
  screen.blit(bg, [0, 0])

  pygame.display.flip()
  clock.tick(40)