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

        # Check collisions. Check every bullet against every alien to so if they are overlapping.
        for bullet in self.bullet_list:
            for alien in self.alien_list:
                if bullet.get_rectangle().colliderect(alien.get_rectangle()):
                    self.bullet_list.remove(bullet)
                    self.alien_list.remove(alien)