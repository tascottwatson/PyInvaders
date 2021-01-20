def __init__(self):
        # You have to let the pygame library initialise itself
        pygame.init()

        # Using clock allows us fix a particular frame rate later on
        self.clock = pygame.time.Clock()

        # Set up the window that the game will run in
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_WIDTH))
        pygame.display.set_caption("Space Invaders!")

        # Load the background image, scale it to fill the entire window, and copy it to the screen.
        # (screen is the image that we actually see in the window. blit is a function that draws an image onto
        # another image.
        self.background = pygame.image.load('back.png').convert()
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_WIDTH))
        self.screen.blit(self.background, (0, 0))

        # Create a player object (see Player definition later on)
        self.player = Player()

        # Create a list to contain any aliens we create and add one new Alien object to the list.
        self.alien_list = []
        self.alien_list.append(Alien(100, 100, 5))

        # Create a list for any bullets that we create later, but don't actually a bullet yet.
        self.bullet_list = []