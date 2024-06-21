import random
import pygame

from FallingObject import FallingObject
from GameState import GameState
from Player import Player
from Draw import Draw
from Menu import Menu
from Screen import *

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    player = Player(400, 550)
    game_state = GameState()
    dg = Draw()
    falling_objects = pygame.sprite.Group()

    menu = Menu(screen)
    running = True
    while running:
        for event in pygame.event.get():
            action = menu.handle_event(event)
            if action == 'quit':
                pygame.quit()
                return
            if action == 'play':
                running = False
                break
        menu.update() # actualiza la imagen que se muestra
        menu.draw()
        pygame.display.flip()
        clock.tick(60)

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

        if game_state.level_completed:
            win_screen = WinScreen(screen)
            running = True
            while running:
                for event in pygame.event.get():
                    action = win_screen.handle_event(event)
                    if action == 'quit':
                        pygame.quit()
                        return
                    if action == 'next_level':
                        running = False
                        falling_objects.empty()
                        break
                win_screen.draw()
                pygame.display.flip()

        if game_state.win:
            win = Win(screen)
            running = True
            while running:
                for event in pygame.event.get():
                    action = win.handle_event(event)
                    if action == 'quit':
                        pygame.quit()
                        return
                win.draw()
                pygame.display.flip()

        if not game_state.running and not game_state.win:
            game_over = GameOver(screen)
            running = True
            while running:
                for event in pygame.event.get():
                    action = game_over.handle_event(event)
                    if action == 'quit':
                        pygame.quit()
                        return
                    if action == 'retry':
                        running = False
                        game_state = GameState()
                        falling_objects.empty()
                        player = Player(400, 500)
                        break
                game_over.draw()
                pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()