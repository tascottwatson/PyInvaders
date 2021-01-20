def __init__(self, start_x, start_y, speed):
        self.x = start_x
        self.y = start_y
        self.speed = speed
        self.left_limit = 50
        self.right_limit = 500
        self._image = pygame.image.load('Alien.png').convert_alpha()

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def update(self, event_list):
        self.x += self.speed
        if self.x < self.left_limit or self.x > self.right_limit:
            self.speed *= -1
            self.y += 10

    def get_rectangle(self):
        rect = self._image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect