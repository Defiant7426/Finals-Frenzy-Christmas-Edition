import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #self.image = pygame.Surface((30, 30))}
        original_image = pygame.image.load('img/player.png')
        self.image = pygame.transform.scale(original_image, (80, 60))
        #self.image.fill((0, 0, 255))
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
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)