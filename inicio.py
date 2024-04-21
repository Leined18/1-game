import pygame
import math
from enemy import enemy
from enemy import enemy2
from fire import fire

# Directorio de assets
ASSETS_DIR = "assets"

# colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
RED = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE = (0,255,0)
AZUL = (0,0,255)

# dimensiones de ventana
ANCHO = 1000
ALTO = 800

#FPS
FPS = 60
#FUENTES
consolas = pygame.font.match_font('consolas')
Times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

# clase de jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, player_number):
        super().__init__()
        # Cargamos la imagen
        self.image = pygame.image.load(ASSETS_DIR + "/nave_espacial.png")
        # Seleccionamos el rectángulo del sprite
        self.rect = self.image.get_rect()
        # Centramos rectángulo según el número de jugador
        if player_number == 1:
            self.rect.center = (400, 550)
        else:
            self.rect.center = (600, 550)
        # Asignamos velocidad
        self.velocidad_x = 0
        self.velocidad_y = 0
        # Cadencia
        self.cadencia = 1000
        # Obtenemos el tiempo del último disparo
        self.ultimate = pygame.time.get_ticks()
        # Teclas de control
        if player_number == 1:
            self.keys = {
                "left": pygame.K_a,
                "right": pygame.K_d,
                "up": pygame.K_w,
                "down": pygame.K_s,
                "shoot": pygame.K_r
            }
        else:
            self.keys = {
                "left": pygame.K_LEFT,
                "right": pygame.K_RIGHT,
                "up": pygame.K_UP,
                "down": pygame.K_DOWN,
                "shoot": pygame.K_p
            }  

        self.is_dead = False  # Bandera para verificar si el jugador está muerto
        self.recover_time = 0  # Tiempo de recuperación inicial

    def disparos(self):
        bala = fire(self.rect.centerx + 10, self.rect.centery - 10)
        groups["bullets"].add(bala)

    def disparos2(self):
        bala = fire(self.rect.centerx - 20, self.rect.centery - 5)
        groups["bullets"].add(bala)

    def update(self):
        if self.is_dead:
            return

        # Asignamos velocidad cada vez que se ejecuta el ciclo
        self.velocidad_x = 0
        self.velocidad_y = 0
        # Variable para captar las pulsaciones del teclado
        teclas = pygame.key.get_pressed()
        # Movimientos según teclas
        if teclas[self.keys["left"]]:
            self.velocidad_x = -5  # Reduced speed
        if teclas[self.keys["right"]]:
            self.velocidad_x = 5   # Reduced speed
        if teclas[self.keys["up"]]:
            self.velocidad_y = -5  # Reduced speed
        if teclas[self.keys["down"]]:
            self.velocidad_y = 5   # Reduced speed
        # Tecla de disparo
        if teclas[self.keys["shoot"]]:
            tiempo = pygame.time.get_ticks()
            if tiempo - self.ultimate > self.cadencia:
                self.disparos()
                self.disparos2()
                self.ultimate = tiempo
                laser.play()

        # Actualizamos la posición del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limitantes de bordes
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        if self.rect.top < 0:
            self.rect.top = 0
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def restore(self, player_number):
        self.rect.center = (400, 550) if player_number == 1 else (600, 550)
        self.is_dead = False  # El jugador vuelve a estar vivo
        self.recover_time = 0  # Reiniciar el tiempo de recuperación

    def kill(self):
        super().kill()
        self.is_dead = True  # Marcar al jugador como muerto
        self.recover_time = pygame.time.get_ticks() + 5000  # Tiempo de recuperación: 5 segundos (5000 ms)

    def check_revive(self):
        if self.is_dead and pygame.time.get_ticks() > self.recover_time:
            self.restore(1 if self.keys["left"] == pygame.K_a else 2)  # Restaurar jugador

# clase de inicio de videojuego
class inicio():
    pygame.init()

# sonidos de ambiente
laser = pygame.mixer.Sound(ASSETS_DIR + '/disparo.wav')
puntos = pygame.mixer.Sound(ASSETS_DIR + '/Puntos.wav')
ambiente = pygame.mixer.Sound(ASSETS_DIR + "/ambiental.mp3")
pygame.mixer_music.set_volume(0.2)
ambiente.play()
Muerte = pygame.mixer.Sound(ASSETS_DIR + '/Muerte.wav')

# dibujamos la screen de el jugador
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Taco Trouble')

# fondo de videojuego
fondo = pygame.transform.scale(pygame.image.load(ASSETS_DIR + "/space1.webp").convert(), (ANCHO, ALTO))

# Establecemos FPS
clock = pygame.time.Clock()

# Sprites
groups = {
    "bullets": pygame.sprite.Group(),
    "enemies": pygame.sprite.Group(),
    "players": [],
    "deadplayers": []
}

# add sprites
p1 = pygame.sprite.Group()
p2 = pygame.sprite.Group()
player1 = Player(1)
player2 = Player(2)
p1.add(player1)  
p2.add(player2)
groups["players"].extend([p1, p2])

# Sistema de puntuacion
puntuacion = 0
# sistema de recuperacion
def texto(screen,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True,color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    screen.blit(superficie,rectangulo)

# ciclo del videojuego
ejecutando = True

# ciclo de ejecutado del videojuego
while ejecutando:
    clock.tick(FPS)
    screen.blit(fondo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()

    # Muestra de puntuacion
    texto(screen, Times, str(puntuacion).zfill(4), BLANCO, 70, 700, 60)

    # Actualizacion de sprites
    for player_group in groups["players"]:
        player_group.update()
    groups["bullets"].update()
    groups["enemies"].update()

    # colisiones
    colision_nave = pygame.sprite.groupcollide(groups["enemies"], groups["players"][0], False, False)
    colision_nave2 = pygame.sprite.groupcollide(groups["enemies"], groups["players"][1], False, False)
    colision_bala = pygame.sprite.groupcollide(groups["enemies"], groups["bullets"], True, True)


    # condiciones de colision
    if colision_nave or colision_nave2:
        if colision_nave:
            player1.kill()
            Muerte.play()
        if colision_nave2:
            player2.kill() 
            Muerte.play()
        
    if player1.is_dead == True and player2.is_dead == True: # por ahora se cierra el juego al morir los dos jugadores
        ejecutando = False
        break

    if colision_bala:
        puntuacion += 10
        puntos.play()
        Muerte.play()

    if not groups["enemies"]:
        num_enemies1 = 3 if puntuacion <= 500 else 3
        num_enemies2 = 2 if puntuacion <= 500 else 8
        # Agregar personajes
        for x in range(num_enemies1):
            enemigo1 = enemy()
            groups["enemies"].add(enemigo1)
        for x in range(num_enemies2):
            enemigo2 = enemy2()
            groups["enemies"].add(enemigo2)

    if puntuacion > 1000:
        ambiente = pygame.mixer.Sound(ASSETS_DIR + '/ambiental2.mp3')
        ambiente.play()

    # Dibujando sprites en screen
    for player_group in groups["players"]:
        player_group.draw(screen)
    groups["enemies"].draw(screen)
    groups["bullets"].draw(screen)
    pygame.display.flip()
