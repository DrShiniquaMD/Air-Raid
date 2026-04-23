import pygame
from pygame import mixer
from settings import WHITE, BLACK, NEXT_IMG_COLOUR

pygame.init()

mixer.init()

def load_image(path, colorkey=None):
    img = pygame.image.load(path).convert()
    if colorkey is not None:
        img.set_colorkey(colorkey)
    return img

def load_images():
    return {
        # Screens
        "menu_screen": load_image("assets/air raid menu.png"),
        "instruction_screen": load_image("assets/Night_Note.jpg"),
        "death_screen": load_image("assets/lose.png"),
        "win_screen": load_image("assets/win.png"),
        "achievement": load_image("assets/achievement.jpg"),

        # UI buttons
        "start_img": load_image("assets/start.jpg", WHITE),
        "quit_img": load_image("assets/exit.jpg", WHITE),
        "end_img": load_image("assets/end.png"),
        "next_img": load_image("assets/next.png", NEXT_IMG_COLOUR),
        "back_img": load_image("assets/back.png", WHITE),
        "reset_img": load_image("assets/reset.png"),
        "menu_img": load_image("assets/main menu.png", WHITE),

        # Player / enemies
        "ship": load_image("assets/air raid.png", WHITE),
        "alt_ship": load_image("assets/threepeater.png.png"),

        # Projectiles
        "pea_projectile": load_image("assets/pea.png", BLACK),
        "ball": load_image("assets/fire-removebg-preview.png", BLACK),

        # Powerups
        "sun": load_image("assets/Sun_PvZ3.png", BLACK),
        "food": load_image("assets/Pvz2plantfood.png", BLACK),
        "taco": load_image("assets/Taco.png", BLACK),

        # Boss
        "boss": load_image("assets/zomboss.png", WHITE),

        # Extra
        "winner": load_image("assets/winner.jpg", WHITE),
    }

def load_sound():
    return {
        "fire" : mixer.Sound("assets/SFX swing.ogg"),

        "hit_zomboss" : mixer.Sound("assets/SFX shieldhit.mp3"),

        "die_sound" : mixer.Sound("assets/Voices scream.mp3"),

        "roof" : mixer.Sound("assets/Roof.mp3"),

        "boss" : mixer.Sound("assets/Zomboss.mp3"),

        "ready" : mixer.Sound("assets/READY.mp3"),

        "win" : mixer.Sound("assets/wins.mp3"),

        "hit" : mixer.Sound("assets/fire.mp3"),

        "collect" : mixer.Sound("assets/collect.mp3"),

        "food" : mixer.Sound("assets/plant food.mp3"),

        "taco" : mixer.Sound("assets/eat.mp3")
    }