import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.button_font = pygame.font.SysFont(None, 50)
        self.info_font = pygame.font.SysFont(None, 30)
        self.play_button = pygame.Rect(350, 250, 130, 50)
        self.quit_button = pygame.Rect(350, 310, 130, 50)

    def draw(self):
        self.screen.fill((174, 214, 241))

        pygame.draw.rect(self.screen, (0,255,0), self.play_button)
        play_text = self.button_font.render("Jugar", True, (0, 0, 0))
        self.screen.blit(play_text, (self.play_button.x + 20, self.play_button.y + 10))

        pygame.draw.rect(self.screen, (255,0,0), self.quit_button)
        quit_text = self.button_font.render("Salir", True, (0, 0, 0))
        self.screen.blit(quit_text, (self.quit_button.x + 20, self.quit_button.y + 10))

        info_text = self.info_font.render("Presiona 'Jugar' para comenzar", True, (0, 0, 0))
        self.screen.blit(info_text, (50, 50))

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.collidepoint(event.pos):
                return 'play'
            if self.quit_button.collidepoint(event.pos):
                return 'quit'