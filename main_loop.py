def main_loop(self):
        """
        This is the main loop. Once the game starts it just keeps repeating until the game ends.
        """
        running = True
        while running:
            # Fix the frame rate to 60 fps. If we get here too quickly the tick function
            # halts the program until it's time to move on.
            self.clock.tick(60)

            # Get a list of any input events (mouse or keyboard) that have happened since we last checked.
            event_list = pygame.event.get()

            self.update_logic(event_list)
            self.update_display()

            # After letting the different objects update themselves deal with any other events.
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # If the user pressed the space bar, create a new bullet
                        self.bullet_list.append(Bullet(self.player.x, 500))
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # quit the game
                elif event.type == pygame.QUIT:
                    running = False

        # If we exit the main loop, the only thing left to do is shut down pygame.
        pygame.quit()