import pygame
import random
from projectiles import Fireball
from settings import screen, SCREEN_HEIGHT, GREEN, RED
from assets import load_images

pygame.init()

images = load_images()

# Zomboss class
class Zomboss(pygame.sprite.Sprite):
    def __init__(self, x, y, image, health, fireball_group, peaship_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.change = 5
        self.health_full = health
        self.health_left = health
        self.last_fired = pygame.time.get_ticks()
        self.fireball_group = fireball_group
        self.peaship_group = peaship_group

    def update(self):
        # Current time
        current_time = pygame.time.get_ticks()

        # Fireball cooldown
        cooldown = random.randrange(300, 1500)

        self.rect.y += self.change
        if self.rect.top < -150:
            self.change *= -1

        elif self.rect.bottom > SCREEN_HEIGHT + 50:
            self.change *= -1

        # Draw health
        pygame.draw.rect(screen, RED, (705, 650, 250, 30))
        if self.health_left > 0:
            pygame.draw.rect(screen, GREEN, (705, 650, int(250 * (self.health_left / self.health_full)), 30))

        # Shooting at the player
        if current_time - self.last_fired > cooldown:
            fireball_main = Fireball(self.rect.left, self.rect.centery + 50, images["ball"], self.peaship_group)
            self.fireball_group.add(fireball_main)

            if current_time - self.last_fired > cooldown and self.health_left < 125:
                fireball_lower = Fireball(self.rect.left, self.rect.centery + 150, images["ball"], self.peaship_group)
                self.fireball_group.add(fireball_lower)

            if current_time - self.last_fired > cooldown and self.health_left < 50:
                fireball_upper = Fireball(self.rect.left, self.rect.centery - 50, images["ball"], self.peaship_group)
                self.fireball_group.add(fireball_upper)

            self.last_fired = current_time