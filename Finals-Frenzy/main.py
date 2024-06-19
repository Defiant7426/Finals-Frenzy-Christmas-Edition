import random
import pygame

from FallingObject import FallingObject
from GameState import GameState
from Player import Player
from Draw import Draw


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    player = Player(400, 500)
    game_state = GameState()
    dg = Draw()
    falling_objects = pygame.sprite.Group()

    while game_state.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.running = False

        player.update()
        falling_objects.update()

        collisions = pygame.sprite.spritecollide(player, falling_objects, True)
        game_state.update(player, collisions)

        if random.randint(1, 20) == 1:
            falling_object = FallingObject(random.randint(0, 800), 0, random.choice(['support', 'trap']))
            falling_objects.add(falling_object)

        dg.draw_game(screen, player, falling_objects, game_state)

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()