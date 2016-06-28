import pygame

class Logo():
    
    def __init__(self, dvdSettings, screen):
        """Initialize the image and set its starting position."""
        self.screen = screen
        self.dvdSettings = dvdSettings

        # Load the image and get its dimensions
        self.image = pygame.image.load('images/logo.bmp')
