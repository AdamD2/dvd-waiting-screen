import pygame
import math

class Logo():
    
    def __init__(self, dvdSettings, screen):
        """Initialize the image and set its starting position."""
        self.screen = screen
        self.dvdSettings = dvdSettings

        # Load the image and get its dimensions
        self.image = pygame.image.load('images/logo.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # Start the logo in the middle of the screen
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery

        # Decimal value to store the center of the logo for complex movement
        self.verticalCenter = float(self.rect.centery)
        self.horizontalCenter = float(self.rect.centerx)

        # Movement flags, where up and right are positive
        self.movingUp = True
        self.movingRight = True

    def update(self):
        """Update the logo's position."""
        # Flip the movement flags if the ship reaches the edge of the screen
        if self.rect.top < 0:
            self.movingUp = False
        elif self.rect.bottom == self.screenRect.height:
            self.movingUp = True

        if self.rect.left < 0:
            self.movingRight = True
        elif self.rect.right == self.screenRect.right:
            self.movingRight = False 

        # Update the center value.
        if self.movingUp:
            self.verticalCenter += self.dvdSettings.imageSpeed * math.sin(30) * 1
        elif not self.movingUp:
            self.verticalCenter -= self.dvdSettings.imageSpeed * math.sin(30) * 1
        
        if self.movingRight:
            self.horizontalCenter += self.dvdSettings.imageSpeed * math.cos(30) * 8
        elif not self.movingRight:
            self.horizontalCenter -= self.dvdSettings.imageSpeed * math.cos(30) * 8

        # Update rect object from self.center
        self.rect.centerx = self.horizontalCenter
        self.rect.centery = self.verticalCenter

    def blitme(self):
        """Draw the logo at its current location."""
        self.screen.blit(self.image, self.rect)
