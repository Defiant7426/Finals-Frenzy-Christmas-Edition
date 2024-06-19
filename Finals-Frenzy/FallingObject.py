import pygame

class FallingObject(pygame.sprite.Sprite):
    def __init__(self, x, y, obj_type):
        super().__init__()
        self.obj_type = obj_type
        self.image = self.create_image(obj_type)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def create_image(self, obj_type):
        if obj_type == 'support':
            return self.create_support_image()
        else:
            return self.create_trap_image()

    def create_support_image(self):
        image = pygame.Surface((30, 30))
        image.fill((0, 255, 0))
        return image

    def create_trap_image(self):
        image = pygame.Surface((30, 30))
        image.fill((255, 0, 0))
        return image

    def update(self):
        self.rect.y += self.speed