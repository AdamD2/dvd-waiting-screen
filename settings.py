class Settings():
    """A class to store all of the settings."""

    def __init__(self):
        """Initialize all of the settings for the screen and logo."""
        # Screen settings
        self.screenWidth = 1366
        self.screenHeight = 768
        self.bgColor = (0, 0, 0)

        # Movement settings
        self.imageSpeed = 0.5
        self.yScalar = 1
        self.xScalar = 8
