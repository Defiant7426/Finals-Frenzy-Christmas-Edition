import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        franklin_d = pygame.image.load('img/player/franklin_derecha.png')
        franklin_i = pygame.image.load('img/player/franklin_izquierda.png')
        self.image_caminando_derecha = pygame.transform.scale(franklin_d, (50, 90))
        self.image_caminando_izquierda = pygame.transform.scale(franklin_i, (50, 90))
        self.image = self.image_caminando_derecha
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (x, y)
        self.speed = 6
        self.energy = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.image_caminando_izquierda
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.image_caminando_derecha

    def draw(self, screen):
        screen.blit(self.image, self.rect)