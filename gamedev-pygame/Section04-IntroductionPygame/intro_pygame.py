import pygame

width, height = 800, 600

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game One')

def main():
  run = True

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    GScreen.fill((0, 15, 0))
    pygame.display.update()

if __name__ == '__main__':
  main()