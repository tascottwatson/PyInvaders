def update_display(self):
        """
        This function gets called every frame do draw everything to the screen.
        """
        # Start by re-drawing the background. This will wipe out anything that was previously drawn
        self.screen.blit(self.background, (0, 0))

        # Call the function that will draw the player. We pass the screen as a parameter so the player object knows
        # where to draw itself
        self.player.draw(self.screen)

        # Run through the entire list of aliens drawing each of them
        for alien in self.alien_list:
            alien.draw(self.screen)

        # Do the same for any bullets
        for bullet in self.bullet_list:
            bullet.draw(self.screen)
        pygame.display.flip()