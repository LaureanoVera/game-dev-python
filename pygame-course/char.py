import pygame, sys
pygame.init()

# CONFIG
size = (626, 278)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


pygame.mouse.set_visible(0)

bg = pygame.image.load('pygame-course/bg.jpg').convert()
char = pygame.image.load('pygame-course/char.png')
char.set_colorkey([0,0,0])

done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  mouse_pos = pygame.mouse.get_pos()
  x = mouse_pos[0]
  y = mouse_pos[1]

  screen.blit(bg, [0, 0])
  screen.blit(char, [x, y])

  pygame.display.flip()
  clock.tick(40)