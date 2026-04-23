import pygame
import random
from projectiles import Pea
from powerups import Health, Boost, TriBoost
from settings import GREEN, RED, SCREEN_HEIGHT, screen
from assets import load_images, load_sound

pygame.init()

images = load_images()

sound = load_sound()

# Peaship class
class Peaship(pygame.sprite.Sprite):
    def __init__(self, x, y, image, health, pea_group, heal_group, boost_group, triboost_group, zomboss_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_full = health
        self.health_left = health
        self.pea_group = pea_group
        self.heal_group = heal_group
        self.boost_group = boost_group
        self.triboost_group = triboost_group
        self.zomboss_group = zomboss_group
        self.last_shot = pygame.time.get_ticks()
        self.last_healed = pygame.time.get_ticks()
        self.last_boosted = pygame.time.get_ticks()
        self.available = True
        self.available_alt = True
        self.tri = False

    def update(self):
        # Current time
        current_time = pygame.time.get_ticks()

        boost_length = 4500

        boost_cooldown = random.randrange(15000, 30000)

        triple_boost_cooldown = random.randrange(15000, 30000)

        # Cooldown for shooting
        if self.available == False and self.last_boosted + boost_length > current_time:
            cooldown = 50
        else:
            cooldown = 150
            self.available = True

        if self.available_alt == False and self.last_boosted + boost_length > current_time:
            self.tri = True

        else:
            self.tri = False

        alt_cooldown = random.randrange(5000, 20000)

        # Movement speed
        speed = 7.5

        # See if key gets pressed
        key = pygame.key.get_pressed()

        if key[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= speed
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += speed
        if key[pygame.K_d] and self.rect.right < 650:
            self.rect.x += speed

        # Draw health
        pygame.draw.rect(screen, RED, (25, 650, 250, 30))
        if self.health_left > 0:
            pygame.draw.rect(screen, GREEN, (25, 650, int(250 * (self.health_left / self.health_full)), 30))

        # Shooting the peas

        if key[pygame.K_RETURN] and current_time - self.last_shot > cooldown and self.tri == True:

            pea_top = Pea(self.rect.right, self.rect.centery - 80, images["pea_projectile"], self.zomboss_group)
            self.pea_group.add(pea_top)

            pea_bottom = Pea(self.rect.right, self.rect.centery + 40, images["pea_projectile"], self.zomboss_group)
            self.pea_group.add(pea_bottom)

            pea_middle = Pea(self.rect.right, self.rect.centery - 20, images["pea_projectile"], self.zomboss_group)
            self.pea_group.add(pea_middle)

            self.last_shot = current_time
            sound["fire"].play()

        elif key[pygame.K_RETURN] and current_time - self.last_shot > cooldown:
            pea_single = Pea(self.rect.right, self.rect.centery - 20, images["pea_projectile"], self.zomboss_group)
            self.pea_group.add(pea_single)

            self.last_shot = current_time
            sound["fire"].play()

        if current_time - self.last_healed > alt_cooldown:
            shine = Health(random.randrange(0, 650), -75, images["sun"], self)
            self.heal_group.add(shine)

            self.last_healed = current_time

        if current_time - self.last_boosted > boost_cooldown:
            leaf = Boost(random.randrange(0, 630), -75, images["food"], self)
            self.boost_group.add(leaf)

            self.last_boosted = current_time

        if current_time - self.last_boosted > triple_boost_cooldown:
            tacos = TriBoost(random.randrange(0, 630), -75, images["taco"], self)
            self.triboost_group.add(tacos)

            self.last_boosted = current_time