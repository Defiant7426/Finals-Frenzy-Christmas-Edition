import pygame

class Draw:
    def __init__(self):
        pass

    def draw_game(self, screen, player, falling_objects, game_state):
        screen.fill((174, 214, 241))
        player.draw(screen)
        falling_objects.draw(screen)

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {game_state.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        energy_text = font.render(f"Energy: {player.energy}", True, (0, 0, 0))
        screen.blit(energy_text, (10, 50))

        level_text = font.render(f"Level: {game_state.level}", True, (0, 0, 0))
        screen.blit(level_text, (10, 90))

        pygame.display.flip()