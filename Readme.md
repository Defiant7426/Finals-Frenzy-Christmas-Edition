# Finals Frenzy: Christmas Edition

Alumnos: 

- De la Cruz Valdiviezo, Pedro Luis David
- Azaña Vega, Luis Angel

# Descripción del juego

El juego trata sobre un estudiante universitario llamado Franklin que está inscrito en el ciclo de primavera. Lamentablemente, la universidad empezó las clases unas semanas tarde, por lo que los exámenes finales son una semana antes de Navidad. Si el estudiante no aprueba estos exámenes, tendrá que ir a los exámenes sustitutorios que justo caen en la semana de Navidad y así no podrá disfrutar con sus amigos y familiares. Para que el estudiante pueda pasar los exámenes, debe superar una serie de retos. Concretamente, en este juego, los estudiantes deben recoger los objetos que caen del cielo. Los objetos pueden ser de soporte o trampas donde pierdes vida.

# Caracteristicas del juego

1. Personaje principal:
    - Franklin: Es un típico estudiante de UNI que siempre está luchando por mantener el equilibrio entre sus estudios y su vida social. Es inteligente pero se confía o falta en los primeros exámenes, por lo que todo el peso recae en los últimos exámenes pues solo trabaja bajo presión.
2. Obstaculos de soporte:
    - Libros: Este objeto ayudan a aumentar la puntuación y asi tener mas probabilidades de pasar esos tediosos examenes
    - Café: Este suministro te da energía por lo que despues de consumirlo el estudiante recibe una cierta velocidad
3. Obstaculos de trampa:
    - Youtube: Este es un obstáculo que distrae a Franklin, lo que reduce su tiempo de estudio y le quita vida.
    - Tiktok: Otro obstáculo distractor que, cuando Franklin interactúa con él, disminuye su tiempo de estudio y vida.
    - Valorant: Este juego es una trampa que consume gran parte del tiempo de estudio de Franklin, reduciendo su vida.
    - Lol (League of Legends): Un juego altamente adictivo que, si Franklin se involucra con él, pierde valioso tiempo de estudio y vida.
    - Chess: Aunque es un juego mental, puede consumir mucho tiempo. Si Franklin pasa demasiado tiempo jugando al ajedrez, su tiempo de estudio y vida se reducen.
    - Almohada: Este ítem puede hacer que Franklin se duerma, lo que lo inmobiliza por un tiempo.
4. Sistema de puntuación:
    - Cada libro recogido suma puntos en la cuenta total de Franklin
    - Cada café recogido otorga un impulso de energía, permitiendo a Franklin recoger libros más rápidamente por un período de tiempo limitado.
    - Cada trampa recogida le resta puntos o lo inmobiliza durante un tiempo pequeño.
5. Niveles del juego:
    
    Franklin tiene para estudiar unas cuantas horas para el examen, en total son 5 examenes por lo que solo hay 5 niveles
    
6. Flujo del Juego:
    
    En cada examen, Franklin tiene unas cuantas horas limitadas para estudiar todo el curso. Cada vez que Franklin acumula puntos, el puntaje crece (empieza con 0 y el máximo es 20). Si el puntaje llega a 20, el juego termina, pues es el máximo puntaje que puede tener en un examen. La nota mínima para aprobar crece cada vez que el nivel es mayor; en el primer examen, la nota mínima es 10 y en el último es 17.
    
7. Final del juego:
    
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