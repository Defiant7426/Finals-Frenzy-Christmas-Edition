import pygame

class WinScreen:
    def __init__(self, screen):
        self.screen = screen
        self.win_font = pygame.font.SysFont(None, 50)
        self.button_font = pygame.font.SysFont(None, 30)
        self.next_level_button = pygame.Rect(350, 350, 170, 50)

    def draw(self):
        self.screen.fill((174, 214, 241))

        win_text = self.win_font.render("¡Ganaste!", True, (0, 0, 0))
        self.screen.blit(win_text, (350, 250))

        pygame.draw.rect(self.screen, (0,255,0), self.next_level_button)
        next_level_text = self.button_font.render("Siguiente nivel", True, (0, 0, 0))
        self.screen.blit(next_level_text, (self.next_level_button.x + 10, self.next_level_button.y + 10))

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.next_level_button.collidepoint(event.pos):
                return 'next_level'

class Win:
    def __init__(self, screen):
        self.screen = screen
        self.win_font = pygame.font.SysFont(None, 37)

    def draw(self):
        self.screen.fill((174, 214, 241))

        win_text = self.win_font.render("¡Franklin Logro pasar el semestre!", True, (0, 0, 0))
        self.screen.blit(win_text, (200, 250))


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return 'quit'

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.game_over_font = pygame.font.SysFont(None, 50)
        self.button_font = pygame.font.SysFont(None, 30)
        self.retry_button = pygame.Rect(350, 350, 130, 50)

    def draw(self):
        self.screen.fill((174, 214, 241))

        game_over_text = self.game_over_font.render("¡Perdiste!", True, (0, 0, 0))
        self.screen.blit(game_over_text, (350, 250))

        pygame.draw.rect(self.screen, (255,0,0), self.retry_button)
        retry_text = self.button_font.render("Reintentar", True, (0, 0, 0))
        self.screen.blit(retry_text, (self.retry_button.x + 10, self.retry_button.y + 10))

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.retry_button.collidepoint(event.pos):
                return 'retry'