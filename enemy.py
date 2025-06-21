import pygame
class Enemy:
    #creates/initialize the enemy
    def __init__(self):
        self.image = pygame.image.load("Main Ship - Base - Damaged.png")
        self.rectangle = self.image.get_rect()
        #place them at the center of screen
        self.rectangle.centerx = 200
        self.rectangle.centery = 200


