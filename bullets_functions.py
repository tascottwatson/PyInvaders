"""
    This is actually quite similar to Player and Alien. Once created it just moves up the screen.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 10
        self._image = pygame.image.load('Bullet.png').convert_alpha()

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def update(self, event_list):
        self.y -= self.velocity

    def get_rectangle(self):
        rect = self._image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect