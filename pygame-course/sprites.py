import pygame
import sys
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# CONFIG
size = (900, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
score = 0


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame-course/Terran.png").convert()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
      self.rect.y += 1
      if self.rect.y > size[1]:
        self.rect.y = random.randint(-25, -10)
        self.rect.x = random.randint(0, (size[0]-10))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame-course/char.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]


meteor_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for i in range(30):
    meteor = Meteor()
    meteor.rect.x = random.randrange(size[0])
    meteor.rect.y = random.randrange(size[1])

    meteor_list.add(meteor)
    all_sprites.add(meteor)

player = Player()
all_sprites.add(player)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites.update()

    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)

    for meteor in meteor_hit_list:
        score += 1
        print(score)

    screen.fill(BLACK)

    all_sprites.draw(screen)

    # for meteor in all_sprites:
    #   meteor.rect.x += random.randint(0, i)
    #   meteor.rect.y += random.randint(0, i)

    pygame.display.flip()
    clock.tick(40)

pygame.quit()
