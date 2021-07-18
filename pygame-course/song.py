import pygame
import random
pygame.init()


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
        player.rect.y = 510


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygame-course/laser.png').convert()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (900, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
score = 0

all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(35):
    meteor = Meteor()
    meteor.rect.x = random.randrange(size[0]-35)
    meteor.rect.y = random.randrange(size[1] / 1.5)

    meteor_list.add(meteor)
    all_sprites.add(meteor)

player = Player()
all_sprites.add(player)

sound = pygame.mixer.Sound('pygame-course/laser.ogg')

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.change_speed(-3)
            if event.key == pygame.K_d:
                player.change_speed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 20
                laser.rect.y = player.rect.y - 20

                sound.play()
                all_sprites.add(laser)
                laser_list.add(laser)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.change_speed(3)
            if event.key == pygame.K_d:
                player.change_speed(-3)

    all_sprites.update()

    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprites.remove(laser)
            laser_list.remove(laser)
            score += 1
            print(score)
        if laser.rect.y < -10:
            all_sprites.remove(laser)
            laser_list.remove(laser)

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
