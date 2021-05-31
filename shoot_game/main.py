import pygame

import sys

import random


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gunshot.mp3")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, targets, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, x, y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


class GameState:
    def __init__(self):
        self.state = 'main_game'
    
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if event.type == pygame.MOUSEBUTTONDOWN:
                # crosshair.shoot()

        screen.blit(background, (0, 0))  
        screen.blit(ready_text, (640 - 115, 360 - 33))
        crosshairs.draw(screen)
        crosshairs.update()
        
        pygame.display.flip() 


    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        pygame.display.flip()
        screen.blit(background, (0, 0))  
        targets.draw(screen)


        
        crosshairs.draw(screen)
        crosshairs.update()


pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Screen
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load('BG.png')
ready_text = pygame.image.load('ready.png')
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair('crosshair.png')
crosshairs = pygame.sprite.Group()
crosshairs.add(crosshair)

# Target
targets = pygame.sprite.Group()
for target in range(20):
    target = Target("target.png", random.randrange(
        0, 1280), random.randrange(0, 720))
    targets.add(target)

while True:
    game_state.intro()
    clock.tick(60)
