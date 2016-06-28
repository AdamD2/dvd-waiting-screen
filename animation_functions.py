import sys

def checkEvents():
    """Halt the program if a key is pressed."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            sys.exit()

def updateScreen(logo, dvdSettings):
    """Update the screen background and images."""
    # Fill the screen with the background color
    screen.fill(dvdSettings.bgColor)
    
    # Draw the logo
    logo.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
