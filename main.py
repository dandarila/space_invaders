import pygame, sys
from player import Player
from alien import Alien


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 10)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)


    def alien_setup(self, rows, cols):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index
                y = row_index
                alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)
    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.aliens.draw(screen)


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            screen.fill((30, 30, 30))
            game.run()

            pygame.display.flip()
            clock.tick(60)

