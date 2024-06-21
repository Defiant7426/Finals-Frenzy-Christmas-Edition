import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.button_font = pygame.font.SysFont(None, 50) # fuente de los botones
        self.info_font = pygame.font.SysFont(None, 30)
        button = pygame.image.load('img/botones/boton_play.png') # carga la imagen del boton
        self.play_button = pygame.transform.scale(button, (185, 90)) # escala la imagen del boton
        self.play_button_rect = self.play_button.get_rect(topleft=(350, 480)) # crea un rectangulo con las dimensiones del boton
        images_brand = [pygame.image.load(f'img/menu/{name}.png') for name in ['netflix', 'tiktok_pixel', 'valo', 'youtube']]
        self.images = [pygame.transform.scale(image, (58, 58)) for image in images_brand]
        self.current_image_index = 0 # indice de la imagen actual
        self.update_count = 0 # contador para actualizar la imagen
        images_franklin_pixel = pygame.image.load('img/menu/menu_franklin.png') # carga la imagen de franklin
        self.franklin_pixel = pygame.transform.scale(images_franklin_pixel, (650, 650)) # escala la imagen de franklin

        pygame.mixer.music.load('soundtrack/menu/awesomeness.wav') # carga la musica de fondo
        pygame.mixer.music.play(-1) # reproduce la musica en loop
    def draw(self):
        self.screen.fill((174, 214, 241)) # color de fondo
        self.screen.blit(self.franklin_pixel, (150, -70)) # dibuja la imagen de franklin
        self.screen.blit(self.images[self.current_image_index], (600, 95)) # dibuja la imagen actual
        self.screen.blit(self.play_button, self.play_button_rect.topleft) # dibuja el boton de play

        info_text = self.info_font.render("Ayuda a Franklin a no ir a los Sustis", True, (0, 0, 0))
        self.screen.blit(info_text, (50, 50)) # escribe el texto

    def update(self): # actualiza la imagen actual
        self.update_count += 1
        if self.update_count % 60 == 0: # cada 60 frames cambia de imagen
            self.current_image_index = (self.current_image_index + 1) % len(self.images) # ciclo entre las imagenes
    def handle_event(self, event):
        if event.type == pygame.QUIT: # si se cierra la ventana
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN: # si se hace click
            if self.play_button_rect.collidepoint(event.pos): # si se hace click en el boton de play
                pygame.mixer.music.stop() # detiene la musica
                return 'play'