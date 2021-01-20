"""
    Hold information about the player, such as where they are on the screen.
    Also draws the image and updates their position based on keyboard input.
    """
    def __init__(self):
        self.x = 100
        self.y = 500
        self.x_vel = 0
        self.y_vel = 0
        self._image = pygame.image.load('UFO.png').convert_alpha()

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_vel -= 10
                if event.key == pygame.K_RIGHT:
                    self.x_vel += 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.x_vel += 10
                if event.key == pygame.K_RIGHT:
                    self.x_vel -= 10
        self.x += self.x_vel
        self.y += self.y_vel