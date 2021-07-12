import pygame
import os

width, height = 800, 600

FPS = 60

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game One')
PICTURE = pygame.image.load(os.path.join('resources', 'char.png'))

def draw_fn():
    GScreen.fill((0, 15, 0))
    GScreen.blit(PICTURE, (0, 0))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_fn()


if __name__ == '__main__':
    main()
