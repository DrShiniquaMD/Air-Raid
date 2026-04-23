import pygame
from assets import load_sound
from settings import SCREEN_WIDTH

pygame.init()

sound = load_sound()

sound["collect"].set_volume(2)

# Pea bullet class
class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y, image, zomboss_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.zomboss_group = zomboss_group

    def update(self):
        self.rect.x += 12
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
        hits = pygame.sprite.spritecollide(self, self.zomboss_group, False)
        if hits:
            self.kill()
            sound["hit_zomboss"].play()
            hits[0].health_left -= 1


# Zomboss projectile class
class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, image, peaship_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.peaship_group = peaship_group

    def update(self):
        self.rect.x -= 8
        if self.rect.right < 0:
            self.kill()
        hits = pygame.sprite.spritecollide(self, self.peaship_group, False)
        if hits:
            self.kill()
            sound["hit"].play()
            hits[0].health_left -= 1