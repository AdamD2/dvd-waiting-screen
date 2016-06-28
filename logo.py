import pygame

class Logo():
    
    def __init__(self, dvdSettings, screen):
        """Initialize the image and set its starting position."""
        self.screen = screen
        self.dvdSettings = dvdSettings

        # Load the image and get its dimensions
        self.image = pygame.image.load('images/logo.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = self.image.screen.get_rect()

        # Start the logo in the middle of the screen
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery

        # Decimal value to store the center of the logo for complex movement
        self.center = float(self.rect.centerx)

        # Movement flags, where up and right are positive
        self.movingUp = True
        self.movingRight = True

    def update(self):
        """Update the logo's position."""
        # Flip the movement flags if the ship reaches the top of the screen
        if self.rect.top == 0:
            movingUp = False
        elif self.rect.bottom == self.screenRect.height:
            movingUp = True

        if self.rect.left == 0:
            movingRight = True
        elif self.rect.right == self.screenRect.right:
            movingRight = False 

        # Update the center value.
        if self.movingUp:
            self.center += self.dvdSettings.imageSpeed * sin(30)
        elif !self.movingUp:
            self.center -= self.dvdSettings.imageSpeed * sin(30)
        
        if self.movingRight:
            self.center += self.dvdSettings.imageSpeed * cos(30)
        elif !self.movingRight:
            self.center -= self.dvdSettings.imageSpeed * cos(30)

    def blitme(self):
        """Draw the logo at its current location."""
        self.screen.blit(self.image, self.rect)
