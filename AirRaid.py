import pygame
from pygame import mixer
from user import Peaship
from enemy import Zomboss
from ui import Buttons
from assets import load_images, load_sound
from settings import screen, SCREEN_WIDTH
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
NEXT_IMG_COLOUR = (76, 105, 113)

images = load_images()

sounds = load_sound()

pygame.init()

mixer.init()

# Set the width and height of the screen [width, height]

# Determine which screen the game is on
page = 0

start = False

death_sound_played = False

win_sound_played = False

pygame.display.set_caption("Air Raid")

# Scrolling background (from https://youtu.be/ARt6DLP38-Y?si=gQqnzuzMXT4oX_bf)
background = pygame.image.load("assets/air raid bg.png").convert()
background_width = background.get_width()

tiles = math.ceil(SCREEN_WIDTH / background_width) + 1

scroll = 0

# Background Music (from https://youtu.be/YQ1mixa9RAw?si=t8-uw749YIX-fu8X)
if page == 0 or page == 1:
    sounds["roof"].play()
    sounds["roof"].play(-1)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Button Instances
start_button = Buttons(360, 580, images["start_img"], 0.3)

next_button = Buttons(75, 60, images["next_img"], 0.5)

quit_button = Buttons(665, 130, images["quit_img"], 0.3)

back_button = Buttons(825, 15, images["back_img"], 0.2)

end_button = Buttons(SCREEN_WIDTH / 2 - 100, 600, images["end_img"], 0.2)

reset_button = Buttons(10, 630, images["reset_img"], 0.1)

menu_button = Buttons(790, 630, images["menu_img"], 0.3)

# Sprite Groups
peaship_group = pygame.sprite.Group()

pea_group = pygame.sprite.Group()

zomboss_group = pygame.sprite.Group()

fireball_group = pygame.sprite.Group()

heal_group = pygame.sprite.Group()

boost_group = pygame.sprite.Group()

triboost_group = pygame.sprite.Group()

groups = [peaship_group, pea_group, zomboss_group, fireball_group, heal_group, boost_group, triboost_group]

# Class Instances
peaship = Peaship(200, 356, images["ship"], 17, pea_group, heal_group, boost_group, triboost_group, zomboss_group)
peaship_group.add(peaship)

zomboss = Zomboss(835, 356, images["boss"], 150, fireball_group, peaship_group)
zomboss_group.add(zomboss)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic ---
    if page == 2:
        # Draw scrolling background
        for i in range(0, tiles):
            screen.blit(background, (i * background_width + scroll, 0))

        # Scroll the background
        scroll -= 8.5

        # Reset scroll
        if abs(scroll) > background_width:
            scroll = 0

        # Drawing sprite groups
        for group in groups:
            group.draw(screen)

        # Update peaship
        for group in groups:
            group.update()

    # Switching to win/lose screens
    if peaship.health_left <= 0:
        page = 3

    if zomboss.health_left <= 0:
        page = 4

    # --- Drawing code ---
    # Check if game has started
    if page == 0:
        screen.blit(images["menu_screen"], [0, 0])

        if next_button.draw(screen):
            page = 1

        if quit_button.draw(screen):
            done = True

        # Switching screens
    if page == 1:
        screen.blit(images["instruction_screen"], [0, 0])

        if start_button.draw(screen):
            page = 2

        if back_button.draw(screen):
            page = 0

        if page == 2:

            sounds["roof"].stop()
            sounds["boss"].play()
            sounds["boss"].play(-1, 0, 5000)
            sounds["boss"].set_volume(10)
            sounds["ready"].play()

    if page == 3:
        screen.blit(images["death_screen"], [0, 0])

        sounds["boss"].stop()
        sounds["ready"].stop()

        if not death_sound_played:
            sounds["die_sound"].play()
            death_sound_played = True

        if reset_button.draw(screen):
            peaship.health_left = peaship.health_full
            zomboss.health_left = zomboss.health_full

            peaship.rect.center = (200, 356)
            zomboss.rect.center = (835, 356)

            pea_group.empty()
            fireball_group.empty()
            heal_group.empty()
            boost_group.empty()
            triboost_group.empty()

            death_sound_played = False

            sounds["boss"].stop()
            sounds["boss"].play(-1)
            sounds["ready"].play()

            page = 2

        if end_button.draw(screen):
            done = True

    if page == 4:
        screen.blit(images["achievement"], [0, 0])
        screen.blit(images["winner"], [10, 10])

        sounds["boss"].stop()

        if not win_sound_played:
            sounds["win"].play()
            win_sound_played = True


        if reset_button.draw(screen):
            peaship.health_left = peaship.health_full
            zomboss.health_left = zomboss.health_full

            peaship.rect.center = (200, 356)
            zomboss.rect.center = (835, 356)

            pea_group.empty()
            fireball_group.empty()
            heal_group.empty()
            boost_group.empty()
            triboost_group.empty()

            sounds["boss"].stop()
            sounds["boss"].play(-1)
            sounds["ready"].play()

            sounds["win"].stop()
            win_sound_played = False

            page = 2

        if menu_button.draw(screen):
            peaship.health_left = peaship.health_full
            zomboss.health_left = zomboss.health_full

            peaship.rect.center = (200, 356)
            zomboss.rect.center = (835, 356)

            pea_group.empty()
            fireball_group.empty()
            heal_group.empty()
            boost_group.empty()
            triboost_group.empty()

            sounds["win"].stop()
            win_sound_played = False

            sounds["roof"].play()

            page = 0

        if end_button.draw(screen):
            done = True

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
