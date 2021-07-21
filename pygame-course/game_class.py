import pygame
import random
pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# config
size = (800, 540)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# class


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame-course/Terran.png').convert()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame-course/char.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    def change_speed(self, x):
        self.speed_x += x

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y = 510


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame-course/laser.png').convert()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3


class Game(object):
    def __init__(self):
      self.score = 0
      self.meteor_list = pygame.sprite.Group()
      self.all_sprites = pygame.sprite.Group()

      for i in range(50):
        

    def process_events(self):
        pass

    def run_logic(self):
        pass

    def display_frame(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
