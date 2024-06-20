# Finals Frenzy: Christmas Edition

Alumnos: 

- De la Cruz Valdiviezo, Pedro Luis David
- Azaña Vega, Luis Angel

# Descripción del juego

El juego trata sobre un estudiante universitario llamado Franklin que está inscrito en el ciclo de primavera. Lamentablemente, la universidad empezó las clases unas semanas tarde, por lo que los exámenes finales son una semana antes de Navidad. Si el estudiante no aprueba estos exámenes, tendrá que ir a los exámenes sustitutorios que justo caen en la semana de Navidad y así no podrá disfrutar con sus amigos y familiares. Para que el estudiante pueda pasar los exámenes, debe superar una serie de retos. Concretamente, en este juego, los estudiantes deben recoger los objetos que caen del cielo. Los objetos pueden ser de soporte o trampas donde pierdes vida.

# Caracteristicas del juego

1. Personaje principal:
    - Franklin: Es un típico estudiante de UNI que siempre está luchando por mantener el equilibrio entre sus estudios y su vida social. Es inteligente pero se confía o falta en los primeros exámenes, por lo que todo el peso recae en los últimos exámenes pues solo trabaja bajo presión.
2. Objetos de estudio.:
    - Libros: Este objeto ayudan a aumentar la puntuación y asi tener mas probabilidades de pasar esos tediosos examenes
    - CharGPT
3. Objetos de soporte:
    - Café: Este suministro te da energía por lo que despues de consumirlo el estudiante recibe una cierta velocidad
    - Energizante:
4. Objetos de trampa:
    - Tiktok: Otro obstáculo distractor que, cuando Franklin interactúa con él, disminuye su tiempo de estudio y vida.
    - Valorant: Este juego es una trampa que consume gran parte del tiempo de estudio de Franklin, reduciendo su vida.
    - Almohada: Este ítem puede hacer que Franklin se duerma, lo que lo inmoviliza por un tiempo.
5. Sistema de puntuación:
    - Cada libro recogido suma puntos en la cuenta total de Franklin
    - Cada café recogido otorga un impulso de energía, permitiendo a Franklin recoger libros más rápidamente por un período de tiempo limitado.
    - Cada trampa recogida le resta puntos o lo inmoviliza durante un tiempo pequeño.
6. Niveles del juego:
    
    Franklin tiene para estudiar unas cuantas horas para el examen, en total son 5 exámenes por lo que solo hay 5 niveles
    
7. Flujo del Juego:
    
    En cada examen, Franklin tiene unas cuantas horas limitadas para estudiar todo el curso. Cada vez que Franklin acumula puntos, el puntaje crece (empieza con 0 y el máximo es 20). Si el puntaje llega a 20, el juego termina, pues es el máximo puntaje que puede tener en un examen. La nota mínima para aprobar crece cada vez que el nivel es mayor; en el primer examen, la nota mínima es 10 y en el último es 17.
    
8. Final del juego:
    
    El juego termina cuando Franklin ha recogido suficientes libros para pasar sus exámenes en el tiempo establecido o cuando su energía se agota por completo.
    

## Elementos del juego

1. Menú de inicio:
    
    Nos da contexto de la situación de Franklin y podemos empezar a jugar
    
2. Barra de energia:
    
    Esta barra representa la energía de Franklin, que disminuye cada vez que se encuentra con una trampa. Si la energía llega a cero, el juego termina.
    
3. Score:
    
    Este muestra la puntuación actual de Franklin. Cada vez que recoge un libro, su puntuación aumenta. Sin embargo, si se encuentra con una trampa, su puntuación disminuirá.
    

## Tecnologías usadas en el proyecto.

En este proyecto usaremos python usando principalmente la biblioteca pygame con el IDE Pycharm.

# Empezamos a escribir el código

Vamos a crear primero un juego simple pero funcional, y luego poco a poco agregaremos funcionalidades de manera que tengamos el juego completo.

1. Creamos la clase `FallingObject`
    
    ```java
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
    ```
    
    Explicación:
    
    Primero, importamos el módulo pygame. Luego, creamos nuestra clase `FallingObject` que hereda de `pygame.sprite.Sprite`. En el método `__init__`, inicializamos nuestro objeto con su posición (x, y) y su tipo (obj_type). De acuerdo al tipo de objeto, se crea la imagen correspondiente con `create_image()`. Los objetos de apoyo (support) son verdes y los objetos trampa (trap) son rojos. Finalmente, actualizamos la posicion del objeto en la que esta cayendo.
    
2. Creamos la clase `GameState`:
    
    ```java
    class GameState:
        def __init__(self):
            self.score = 0
            self.level = 1
            self.exam_score = [10, 12, 14, 16, 18]
            self.exam_index = 0
            self.running = True
    
        def update(self, player, collisions):
            for collision in collisions:
                if collision.obj_type == 'support':
                    self.score += 0.5
                else:
                    player.energy -= 15
    
            if self.score >= self.exam_score[self.exam_index]:
                self.level_up()
                self.score = 0
                player.energy = 100
    
            if player.energy <= 0:
                print("Franklin ira a susti :(")
                self.running = False
    
        def level_up(self):
            self.level += 1
            self.exam_index += 1
            if self.exam_index >= len(self.exam_score):
                print("Franklin paso el semestre :D sin ir a susti!")
                self.running = False
    ```
    
    Explicación:
    
    La clase `GameState` se encarga de mantener un registro del puntaje, el nivel y el estado del juego. En el método `update`, se actualiza el puntaje y la energía del jugador en base a las colisiones con los objetos que caen. Si el jugador alcanza la puntuación necesaria para pasar el examen, se aumenta el nivel y la energía del jugador se restablece a 100. Si la energía del jugador llega a 0, el juego termina. Además, el método `level_up` se encarga de aumentar el nivel y el índice del examen. Cuando el índice del examen alcanza la longitud de `exam_score`, el juego termina con una victoria.
    
3. Creamos la clase `Draw`:
    
    ```java
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
    ```
    
    Explicación:
    
    Esta función `draw_game` se encarga de dibujar todos los elementos del juego en la pantalla. En primer lugar, se llena la pantalla con el color del juego y luego se dibujan el jugador y los objetos que caen. A continuación, se crean y se dibujan en la pantalla los textos del puntaje, la energía y el nivel utilizando la fuente predeterminada de pygame. Finalmente, se actualiza la pantalla con `pygame.display.flip()`.
    
4. Creamos la clase `Player`:
    
    ```java
    import pygame
    
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((30, 30))
            self.image.fill((0, 0, 255))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 5
            self.energy = 100
    
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
    
        def draw(self, screen):
            screen.blit(self.image, self.rect)
    ```
    
    Explicación:
    
    En la clase `Player`, establecemos a Franklin, el personaje principal del juego, como un objeto azul que el jugador puede mover a izquierda y derecha utilizando las teclas correspondientes. La clase también incluye una variable de energía, que se reduce a medida que Franklin interactúa con objetos trampa. En el método `update`, se actualiza la posición de Franklin en función de las teclas presionadas. El método `draw` se utiliza para dibujar a Franklin en la pantalla.
    

Salida del juego:

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled.png)

# Pequeños arreglos al juego

Podemos hacer pequeños ajustes al juego. Por ejemplo, en lugar de mostrar la energía como un número, podemos representarla como una barra. Esto se puede hacer de la siguiente manera en la clase Draw:

```java
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
```

Explicación:

En la clase `Draw`, hemos añadido el método `draw_energy_bar` para dibujar la barra de energía en la pantalla. Este método toma como argumentos la pantalla, el jugador, el ancho y la altura de la barra de energía. Dependiendo del nivel de energía del jugador, la barra se llena con un color diferente: verde si la energía es mayor al 70%, amarillo si es mayor al 30% y rojo en otro caso. Después, se dibujan los rectángulos de contorno y de relleno en la pantalla.

Salida:

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%201.png)

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%202.png)

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%203.png)

Ahora vamos a crear el Menu del juego, para ello vamos a crear la clase Menu:

```java
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
```

Explicación:

La clase `Menu` crea e implementa el menú del juego. En el método `__init__`, se establecen la pantalla, la fuente de los botones, la fuente de la información y los rectángulos de los botones de jugar y salir. En el método `draw`, se dibujan los botones y la información en la pantalla. Finalmente, en el método `handle_event`, se manejan los eventos de pulsar los botones de jugar y salir. Si se pulsa el botón de jugar, se retorna 'play', y si se pulsa el botón de salir, se retorna 'quit'.

Luego actualizamos nuestra clase main:

```java
import random
import pygame

from FallingObject import FallingObject
from GameState import GameState
from Player import Player
from Draw import Draw
from Menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    player = Player(400, 500)
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

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
```

Explicación:

En la función `main`, primero se inicializa pygame y se crea la pantalla y el reloj del juego. Luego se crean las instancias de las clases `Player`, `GameState`, `Draw` y `Menu`, y se crea un grupo para los objetos que caen. En el primer bucle while, se controla el menú del juego: se manejan los eventos de pulsar los botones de jugar y salir, y se actualiza la pantalla. En el segundo bucle while, se maneja el juego en sí: se actualizan el jugador y los objetos que caen, se manejan las colisiones, se crean nuevos objetos que caen y se dibuja el juego en la pantalla. Finalmente, se cierra pygame cuando se termina el juego.