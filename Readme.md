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
    - Libros: Este objeto ayudan a aumentar la puntuación y así tener mas probabilidades de pasar esos tediosos exámenes
    - ChatGPT: Este es una herramienta de inteligencia artificial que ayuda a Franklin a estudiar de manera más eficiente.
3. Objetos de soporte:
    - Café: Este suministro te da energía por lo que después de consumirlo el estudiante recibe una cierta velocidad.
    - Energizante: Este objeto proporciona a Franklin un impulso temporal de energía, lo que le permite recoger objetos a un ritmo más rápido por un tiempo limitado.
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
    
    ```python
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
    
    ```python
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
    
    ```python
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
    
    ```python
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

## Añadiendo una barra para la energía

Podemos hacer pequeños ajustes al juego. Por ejemplo, en lugar de mostrar la energía como un número, podemos representarla como una barra. Esto se puede hacer de la siguiente manera en la clase Draw:

```python
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

## Añadiendo un Menu del juego

```python
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

```python
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

El Menu del juego se veria de la siguiente manera:

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%204.png)

## Añadiendo un Menu por cada nivel

Para añadir un menu por nivel creamos la clase Win:

```python
import pygame

class WinScreen:
    def __init__(self, screen):
        self.screen = screen
        self.win_font = pygame.font.SysFont(None, 50)
        self.button_font = pygame.font.SysFont(None, 30)
        self.next_level_button = pygame.Rect(350, 350, 130, 50)

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
```

Explicación:

La clase `WinScreen` se encarga de crear y manejar la pantalla de victoria que se muestra cuando el jugador gana un nivel. En el método `__init__`, se establecen la pantalla, las fuentes de los textos y el rectángulo del botón de pasar al siguiente nivel. En el método `draw`, se dibujan en la pantalla el texto de victoria y el botón de siguiente nivel. En el método `handle_event`, se manejan los eventos de pulsar el botón de siguiente nivel y la tecla de retorno.

Ahora solo faltaría llamar a esta pantalla cada vez que el jugador logre avanzar un nivel en el método main, para lograr esto agregamos lo siguiente:

```python
    while game_state.running:
        # Resto del codigo
        if game_state.level_completed:
            win_screen = WinScreen(screen)
            running = True
            while running:
                for event in pygame.event.get():
                    action = win_screen.handle_event(event)
                    if action == 'quit':
                        pygame.quit()
                        return
                    if action == 'play':
                        break
                    if action == 'next_level':
                        running = False
                        falling_objects.empty()
                        break
                win_screen.draw()
                pygame.display.flip()
        clock.tick(60)
        # Resto del codigo
```

Explicación:

En el ciclo de juego principal, añadimos un condicional para comprobar si el jugador ha completado un nivel con `game_state.level_completed`. Si es así, se crea la pantalla de victoria y se inicia un nuevo bucle while. En este bucle, se manejan los eventos de pulsar el botón de salir y el botón de pasar al siguiente nivel. Si se pulsa este último, se vacía el grupo de objetos que caen y se sale del bucle. Por último, se dibuja la pantalla de victoria y se actualiza la pantalla del juego.

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%205.png)

Ahora cuando el usuario completo exitosamente todos los niveles vamos a mostrar solo un mensaje de que franklin logro pasar el semestre exitosamente, para ello hacemos la clase `Win` :

```python
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
```

Explicación:

La clase `Win` se encarga de crear y manejar la pantalla final que se muestra cuando el jugador ha pasado todos los niveles. En el método `__init__`, se establecen la pantalla y la fuente del texto. En el método `draw`, se dibuja en la pantalla el texto de victoria. En el método `handle_event`, se maneja el evento de salida del juego.

En nuestro bucle principal del juego agregamos estas lineas:

```python
# Resto del codigo
if not game_state.running:
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
 # Resto del codigo
```

Explicación:

En el bucle de juego principal, añadimos un condicional para comprobar si el juego ha terminado con `not game_state.running`. Si es así, se crea la pantalla de victoria final y se inicia un nuevo bucle while. En este bucle, se manejan los eventos de pulsar la tecla de salida. Por último, se dibuja la pantalla de victoria final y se actualiza la pantalla del juego.

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%206.png)

Ahora vamos a implementar la pantalla de GameOver para ello creamos la clase:

```python
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
```

Luego en nuestro bucle principal agregamos la condicional:

```python
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
```

Explicación:

En el método `__init__`, se establecen la pantalla, las fuentes de los textos y el rectángulo del botón de reintentar. En el método `draw`, se dibuja en la pantalla el texto de Game Over y el botón de reintentar. En el método `handle_event`, se manejan los eventos de pulsar el botón de reintentar y la tecla de salida.

En el bucle de juego principal, añadimos un condicional para comprobar si el juego ha terminado y si el jugador no ha ganado con `not game_state.running and not game_state.win`. Si es asi, se crea la pantalla de Game Over y se inicia un nuevo bucle while. En este bucle, se manejan los eventos de pulsar el botón de reintentar y la tecla de salida. Si se pulsa el botón de reintentar, se reinicia el estado del juego, se vacía el grupo de objetos que caen, se recrea el jugador y se sale del bucle. Por último, se dibuja la pantalla de Game Over y se actualiza la pantalla del juego.

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%207.png)

# Agregando pixel art al juego

Hasta ahora, nuestro juego se basa en formas y colores simples. Pero podemos hacerlo más atractivo visualmente agregando arte en píxeles. Para realizar esta tarea, necesitaremos imágenes en píxeles para reemplazar los rectángulos de colores que representan a Franklin, los objetos que caen y el fondo del juego. También podemos agregar música y efectos de sonido para mejorar la experiencia del juego.

## Embelleciendo el Menú del juego

Para embellecer el menú del juego, podemos agregar una imagen de fondo y cambiar la fuente y el color de los botones. También podemos agregar una animación simple, como un parpadeo, para atraer la atención hacia los botones de 'Jugar' y 'Salir'. Además, podríamos colocar en la parte superior del menú el título del juego con una fuente grande y llamativa.

## Jugador

Franklin lo representaremos como un estudiante con prendas simples, una mochila y lentes azules con cabello negro, tenemos dos imagenes: franklin_derecha.png y franklin_izquierda.png, entonces actualizamos nuestra clase Player

```python
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
```

Explicación:

En la clase `Player`, cargamos las imágenes de Franklin caminando a la derecha e izquierda. Estas imágenes se escalan para tener un tamaño de 50x90 píxeles. A continuación, establecemos la imagen inicial de Franklin como la de él caminando a la derecha. En el método `update`, cambiamos la imagen de Franklin dependiendo de la dirección en la que se está moviendo. Por último, en el método `draw`, dibujamos la imagen de Franklin en la pantalla.

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%208.png)

![Untitled](Finals%20Frenzy%20Christmas%20Edition%20ddb529c67b5c46d0b6630f1bf225600e/Untitled%209.png)