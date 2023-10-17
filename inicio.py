
import pygame
from enemy import enemy
from enemy import enemy2
from fire import fire


# colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE = (0,255,0)
AZUL = (0,0,255)

# dimensiones de ventana
ANCHO = 800
ALTO = 600

#FPS
FPS = 60
#FUENTES
consolas = pygame.font.match_font('consolas')
Times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')
# clase de jugador


class player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
    # Cargamos la imagen
        self.image = pygame.image.load("nave_espacial.png")
    # Seleccionamos el rectangulo del sprite
        self.rect = self.image.get_rect()
        # Centramos rectangulo
        self.rect.center = (400, 550)
        # Asignamos velocidad
        self.velocidad_x = 0
        self.velocidad_y = 0
        # Cadencia
        self.cadencia = 300
        # obtenemos el tiempo del ultimo disparo
        self.ultimate = pygame.time.get_ticks()


    def disparos(self):
        bala = fire(self.rect.centerx + 10, self.rect.centery - 10)
        Balas.add(bala)

    def disparos2(self):
        bala = fire(self.rect.centerx - 20, self.rect.centery - 5)
        Balas.add(bala)

    def update(self):

        # Asignamos velocidad cada veza que se ejecuta el ciclo
        self.velocidad_x = 0
        self.velocidad_y = 0
    # Variable para captar las pulsaciones del teclado
        teclas = pygame.key.get_pressed()
        # Movimiento hacia la izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        # Movimiento hacia la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        # Movimiento hacia la arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        # Movimiento hacia la abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        # tecla de disparo
        if teclas[pygame.K_r]:
            tiempo = pygame.time.get_ticks()
            if tiempo - self.ultimate > self.cadencia:
                self.disparos()
                self.disparos2()
                self.ultimate = tiempo
                laser.play()

    # Actualizamos la posicion del personaje

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limitantes de bordes

        # Borde izquierdo y derecho
        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        # Bordes arriba y abajo
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

        if self.rect.top < 0:
            self.rect.top = 0


# clase de jugador2

class player2(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
    # Cargamos la imagen
        self.image = pygame.image.load("nave_espacial.png")
    # Seleccionamos el rectangulo del sprite
        self.rect = self.image.get_rect()
        # Centramos rectangulo
        self.rect.center = (600, 550)
        # Asignamos velocidad
        self.velocidad_x = 0
        self.velocidad_y = 0
        # Cadencia
        self.cadencia = 300
        # obtenemos el tiempo del ultimo disparo
        self.ultimate = pygame.time.get_ticks()

    def disparos(self):
        bala = fire(self.rect.centerx + 10, self.rect.centery - 10)
        Balas.add(bala)

    def disparos2(self):
        bala = fire(self.rect.centerx - 20, self.rect.centery - 5)
        Balas.add(bala)

    def update(self):

        # Asignamos velocidad cada veza que se ejecuta el ciclo
        self.velocidad_x = 0
        self.velocidad_y = 0
    # Variable para captar las pulsaciones del teclado
        teclas = pygame.key.get_pressed()
        # Movimiento hacia la izquierda

        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -10
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 10
        if teclas[pygame.K_UP]:
            self.velocidad_y = -10
        if teclas[pygame.K_DOWN]:
            self.velocidad_y = 10
        if teclas[pygame.K_p]:
            tiempo = pygame.time.get_ticks()
            if tiempo - self.ultimate > self.cadencia:
                self.disparos()
                self.disparos2()
                self.ultimate = tiempo
                pygame.mixer_music.set_volume(0.01)
                laser.play()

    # Actualizamos la posicion del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
    # Limitantes de bordes

        # Borde izquierdo y derecho
        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        # Bordes arriba y abajo
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

        if self.rect.top < 0:
            self.rect.top = 0


# clase de inicio de videojuego
class inicio():
    pygame.init()

#sonidos de ambiente
    #sonido de disparo
laser = pygame.mixer.Sound('disparo.wav')
    # sonido de puntos
puntos = pygame.mixer.Sound('Puntos.wav')
    # sonido de ambiente
ambiente = pygame.mixer.Sound("ambiental.mp3")
    # cambio de volumen de sonidos
pygame.mixer_music.set_volume(0.2)
ambiente.play()
    # sonido de muerte
Muerte = pygame.mixer.Sound('Muerte.wav')
    


# dibujamos la pantalla de el jugador
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Titulo de la ventana

pygame.display.set_caption('Space')

# fondo de videojuego

fondo = pygame.transform.scale(pygame.image.load(
    "space1.webp").convert(), (1000, 600))

# Establecemos FPS

clock = pygame.time.Clock()

# Sprites

Jugador1 = pygame.sprite.Group()
Jugador2 = pygame.sprite.Group()
Balas = pygame.sprite.Group()
Enemigos = pygame.sprite.Group()
jugadores = pygame.sprite.Group()

# add sprites

jugador1 = player()
jugador2 = player2()
Jugador1.add(jugador1)
Jugador2.add(jugador2)
jugadores.add(jugador1,jugador2)
# Sistema de puntuacion

puntuacion = 0
def texto(pantalla,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True,color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    pantalla.blit(superficie,rectangulo)




# ciclo del videojuego

ejecutando = True

# ciclo de ejecutado del videojuego

while ejecutando:
    clock.tick(FPS)

# para tomar los eventos de la ventana de el videojuego
    pantalla.blit(fondo, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            ejecutando = False
            pygame.quit()
            

# Muestra de puntuacion
    texto(pantalla,Times,str(puntuacion).zfill(4),BLANCO,60,700,50)
# Actualizacion de sprites
    Jugador1.update()
    Jugador2.update()
    Balas.update()
    Enemigos.update()

    # colisiones
    colision_nave = pygame.sprite.groupcollide(Enemigos,Jugador1,False,False)
    colision_nave2 = pygame.sprite.groupcollide(Enemigos,Jugador2,False,False)
    colision_bala = pygame.sprite.groupcollide(Enemigos,Balas,True,True)
    #enemies = [enemigo1, enemigo2]
    # condiciones de colision
    if colision_nave:
        puntuacion -= 1 
        pygame.mixer_music.set_volume(5)
        if puntuacion < 0:
            puntuacion = 0
            jugador1.kill()
            Muerte.play()

    if colision_nave2:
        puntuacion -= 1
        pygame.mixer_music.set_volume(5)
        if puntuacion < 0:
            puntuacion = 0
            jugador2.kill()
            Muerte.play()
        
    
        if not jugadores:
            break
        

    if puntuacion > 300:
        jugador1.cadencia - 500
        jugador2.cadencia - 500

    if colision_bala:
        puntuacion += 10
        puntos.play()
        Muerte.play()
           
    if not Enemigos:
        # SE EJECUTA UN BUCLE
        if puntuacion <= 500:
            for x in range(3):
            # Agregar personajes max 3
                enemigo1 = enemy()
                Enemigos.add(enemigo1)
            for x in range(2):
            # Agregar personajes max 2
                enemigo2 = enemy2()
                Enemigos.add(enemigo2)
        else: 
            for x in range(3):
                enemigo1 = enemy()
                Enemigos.add(enemigo1)
            for x in range(8):
                enemigo2 = enemy2()
                Enemigos.add(enemigo2)
        if puntuacion >= 1000:
            jugador1.cadencia + 1000
            for x in range(10):
                enemigo1 = enemy()
                Enemigos.add(enemigo1)
            for x in range(10):
                enemigo2 = enemy2()
                Enemigos.add(enemigo2)
            if colision_nave:
                puntuacion -= 10 
            if colision_nave2:
                puntuacion -= 10
                
        if puntuacion >= 5000:
            jugador1.cadencia + 200
            for x in range(80):
                enemigo1 = enemy()
                Enemigos.add(enemigo1)
            for x in range(50):
                enemigo2 = enemy2()
                Enemigos.add(enemigo2)
            if colision_nave:
                puntuacion -= 30 
            if colision_nave2:
                puntuacion -= 30 
            
            ambiente = pygame.mixer.Sound('ambiental2.mp3')
            ambiente.play()
            
                

    # Dibujando sprites en pantalla

    Jugador1.draw(pantalla)
    Jugador2.draw(pantalla)
    Enemigos.draw(pantalla)
    Balas.draw(pantalla)

    pygame.display.flip()
