import pygame

import sys

import random


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = [
            pygame.image.load('attack_1.png'),
            pygame.image.load('attack_2.png'),
            pygame.image.load('attack_3.png'),
            pygame.image.load('attack_4.png'),
            pygame.image.load('attack_5.png'),
            pygame.image.load('attack_6.png'),
            pygame.image.load('attack_7.png'),
            pygame.image.load('attack_8.png'),
            pygame.image.load('attack_9.png'),
            pygame.image.load('attack_10.png')
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.attack_animation = False
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
    
    def attack(self):
        self.attack_animation = True
    
    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
            
            self.image = self.sprites[int(self.current_sprite)]
    

pygame.init()
clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player(250, 250)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.attack()            

    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.3)

    pygame.display.flip()
    clock.tick(60)
