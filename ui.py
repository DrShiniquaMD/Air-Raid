import pygame

pygame.init()

# Buttons class
class Buttons:
    def __init__(self, x, y, image, size):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * size), int(height * size)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, area):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        area.blit(self.image, (self.rect.x, self.rect.y))

        return action