# Name: DVD Loading Screen
# Contributors: Adam Douglas
# Date: 28-06-2016
# Purpose: Use the pygame module to emulate a DVD loading screen, where the
#          logo bounces off the walls and moves around the screen.

import pygame
import animationFunctions as af

from settings import Settings
from logo import Logo

def runLoadingScreen():
    # Initialize the window to display the screen on
    pygame.init()
    dvdSettings = Settings()
    screen = pygame.display.set_mode(
        (dvdSettings.screenWidth, dvdSettings.screenHeight))
    pygame.display.set_caption("DVD Loading Screen")

    # Set a background color
    bgColor = dvdSettings.bgColor

    # Create an instance of the image
    logo = Logo(dvdSettings, screen)

    running = True
    while running:
        af.checkEvents()
        logo.update()
        af.updateScreen(screen, dvdSettings, logo)

runLoadingScreen()
