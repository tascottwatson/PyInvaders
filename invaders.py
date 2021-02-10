import pygame
import time
import random
transparent = (0, 0, 0, 0)

class Game:
    """
    Responsible for handling the main loop and storing various key variables
    """
    def __init__(self):
        # You have to let the pygame library initialise itself
        pygame.init()
        self.running = True
        self.hit = False
        # Using clock allows us fix a particular frame rate later on
        self.clock = pygame.time.Clock()
        self.alien_spawn_timer = time.time()
        self.alien_spawn_interval = 0.5
        self.bullet_spawn_timer = time.time()
        self.bullet_spawn_interval = 0.5
        self.powerup_spawn_timer = time.time()
        self.powerup_spawn_interval = 10

        # Set up the window that the game will run in
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_WIDTH))
        pygame.display.set_caption("Space Invaders!")

        self.score = 0

        self.myFont = pygame.font.SysFont('monospace', 100)
        self.label = self.myFont.render(str(self.score), 1, (255, 255, 255))

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

        # Create a list for any bullets that we create later, but don't actually a bullet yet.
        self.bullet_list = []

        self.powerup_list = []

        self.max_powerup_number = 1

    def update_display(self):
        """
        This function gets called every frame do draw everything to the screen.
        """

        # Start by re-drawing the background. This will wipe out anything that was previously drawn
        self.screen.blit(self.background, (0, 0))

        # Call the function that will draw the player. We pass the screen as a parameter so the player object knows
        # where to draw itself
        self.player.draw(self.screen)

        if len(str(self.score)) == 1:
            x_coord = 280
        elif len(str(self.score)) == 2:
            x_coord = 255
        elif len(str(self.score)) == 3:
            x_coord = 230
        self.screen.blit(self.label, (x_coord, 50))

        # Run through the entire list of aliens drawing each of them
        for alien in self.alien_list:
            alien.draw(self.screen)

        # Do the same for any bullets
        for bullet in self.bullet_list:
            bullet.draw(self.screen)

        for powerup in self.powerup_list:
            powerup.draw(self.screen)
        
        

    def update_logic(self, event_list):
        """
        This function gets called every frame to allow different objects to move or update themselves.
        event_list is a list of events such as buttons being pressed or the mouse moving.
        """

        # We call the update functions for the player, every alien and every bullet in the game.
        self.player.update(event_list)
        for alien in self.alien_list:
            alien.update(event_list)
        for bullet in self.bullet_list:
            bullet.update(event_list)
        for powerup in self.powerup_list:
            powerup.update(event_list)


        # Check collisions. Check every bullet against every alien to so if they are overlapping.
        for bullet in self.bullet_list:
            for alien in self.alien_list:
                if bullet.get_rectangle().colliderect(alien.get_rectangle()):
                    self.bullet_list.remove(bullet)
                    self.alien_list.remove(alien)
                    self.score += 1
                    self.label = self.myFont.render(str(self.score), 1, (255, 255, 255))

        for powerup in self.powerup_list:
            if self.player.get_rectangle().colliderect(powerup.get_rectangle()):
                if powerup.type == "speedup":
                    self.player.increment += 2
                else:
                    self.bullet_spawn_interval -= 0.15
                self.powerup_list.remove(powerup)

        for alien in self.alien_list:
            if self.player.get_rectangle().colliderect(alien.get_rectangle()):
                self.hit = True

        if time.time() - self.alien_spawn_timer > self.alien_spawn_interval:
            x_coord = random.randint(100, self.SCREEN_WIDTH-100)
            y_coord = random.randint(-20, 0)
            self.alien_list.append(Alien(self.SCREEN_WIDTH, x_coord, y_coord, 3))
            self.alien_spawn_timer += self.alien_spawn_interval

        if time.time() - self.bullet_spawn_timer > self.bullet_spawn_interval:
            self.bullet_list.append(Bullet(self.player.x+25, self.player.y))
            self.bullet_spawn_timer += self.bullet_spawn_interval

        if time.time() - self.powerup_spawn_timer > self.powerup_spawn_interval:
            if len(self.powerup_list) < self.max_powerup_number:
                x_coord = random.randint(100, self.SCREEN_WIDTH-100)
                y_coord = random.randint(100, self.SCREEN_HEIGHT-100)
                type = random.choice(["speedup", "strength"])
                self.powerup_list.append(PowerUp(x_coord, y_coord, type))
            self.powerup_spawn_timer += self.powerup_spawn_interval

        pygame.display.flip()

    def main_loop(self):
        """
        This is the main loop. Once the game starts it just keeps repeating until the game ends.
        """
        self.score = 0
        self.player.x = 250
        self.player.y = 500
        self.alien_list = []
        self.bullet_list = []
        self.powerup_list = []
        self.myFont = pygame.font.SysFont('monospace', 100)
        self.label = self.myFont.render(str(self.score), 1, (255, 255, 255))
        while self.running:
            # Fix the frame rate to 60 fps. If we get here too quickly the tick function
            # halts the program until it's time to move on.
            self.clock.tick(60)

            # Get a list of any input events (mouse or keyboard) that have happened since we last checked.
            event_list = pygame.event.get()

            self.update_logic(event_list)
            self.update_display()

            # After letting the different objects update themselves deal with any other events.
            for event in event_list:
                # If the user pressed the space bar, create a new bullet

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()  # quit the game
                        quit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if self.hit == True:
                self.bg = pygame.image.load("gameover.png").convert()
                self.bg = pygame.transform.scale(self.bg, (self.SCREEN_WIDTH, self.SCREEN_WIDTH))
                self.screen.blit(self.bg, (0, 0))
                for event in pygame.event.get():
                    if event.key == pygame.K_r:
                        self.hit = False
                        self.bg.fill(transparent)
                        self.main_loop()
                
                
        
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        # If we exit the main loop, the only thing left to do is shut down pygame.
        # pygame.quit()



class Player:
    """
    Hold information about the player, such as where they are on the screen.
    Also draws the image and updates their position based on keyboard input.
    """
    def __init__(self):
        self.x = 250
        self.y = 500
        self.x_vel = 0
        self.y_vel = 0
        self.increment = 5
        self._image = pygame.image.load('UFO.png').convert_alpha()

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def update(self, event_list):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.increment

        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.increment

        if keys_pressed[pygame.K_UP]:
            self.y -= self.increment

        if keys_pressed[pygame.K_DOWN]:
            self.y += self.increment


    def get_rectangle(self):
        rect = self._image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect



class Alien:
    """
    Very similar to the Player object. The update function causes it to slowly zig zig down the screen.
    """
    def __init__(self, SCREEN_WIDTH, start_x, start_y, speed):
        self.x = start_x
        self.y = start_y
        self.speed = random.choice([-speed/2, speed/2])
        self.y_speed = speed/3
        self.left_limit = 50
        self.right_limit = SCREEN_WIDTH - 50
        self._image = pygame.image.load('Alien.png').convert_alpha()

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def update(self, event_list):
        self.x += self.speed
        if self.x < self.left_limit or self.x > self.right_limit:
            self.speed *= -1
        self.y += self.y_speed

    def get_rectangle(self):
        rect = self._image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect


class Bullet:
    """
    This is actually quite similar to Player and Alien. Once created it just moves up the screen.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 12
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

class PowerUp:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self._image = pygame.image.load(type + '.png').convert_alpha()
        self.bob = "up"
        self.bob_interval = 0.5
        self.bob_time = time.time()

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def update(self, event_list):
        if time.time() - self.bob_time > self.bob_interval:
            if self.bob == "up":
                self.y += 10
                self.bob = "down"
            else:
                self.y -= 10
                self.bob = "up"
            self.bob_time += self.bob_interval

    def get_rectangle(self):
        rect = self._image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect
# This is where the game starts. We create a game object and then call it's main_loop() function.
game = Game()
game.main_loop()
