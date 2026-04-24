import pygame
from pygame import mixer
from assets import load_sound
from settings import SCREEN_HEIGHT

pygame.init()
mixer.init()

sounds = load_sound()

# Health class
class Health(pygame.sprite.Sprite):
    def __init__(self, x, y, image, player):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.player = player

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        if self.rect.colliderect(self.player.rect):
            self.kill()
            sounds["collect"].play()
            if self.player.health_left < self.player.health_full:
                self.player.health_left += 1

# Plant food boost
class Boost(pygame.sprite.Sprite):
    def __init__(self, x, y, image, player):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.player = player

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        if self.rect.colliderect(self.player.rect):
            self.kill()
            sounds["food"].play()
            self.player.available = False  # activates rapid fire

# Taco boost
class TriBoost(pygame.sprite.Sprite):
    def __init__(self, x, y, image, player):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.player = player

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        if self.rect.colliderect(self.player.rect):
            self.kill()
            sounds["taco"].play()
            self.player.available_alt = False  # activates triple shot
