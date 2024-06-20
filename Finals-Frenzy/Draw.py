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

        self.draw_energy_bar(screen, player, 200, 20)

        level_text = font.render(f"Level: {game_state.level}", True, (0, 0, 0))
        screen.blit(level_text, (10, 90))

        pygame.display.flip()

    def draw_energy_bar(self, screen, player, energy_bar_width, energy_bar_height):
        outline_color = (255, 255, 255)
        if player.energy > 70:
            fill_color = (75, 249, 70)

        elif player.energy > 30:
            fill_color = (249, 238, 20)

        else:
            fill_color = (255, 27, 27)

        outline_rect = pygame.Rect(10, 50, energy_bar_width, energy_bar_height)
        fill_rect = pygame.Rect(10, 50, energy_bar_width * (player.energy / 100), energy_bar_height)
        pygame.draw.rect(screen, outline_color, outline_rect, 2)
        pygame.draw.rect(screen, fill_color, fill_rect)