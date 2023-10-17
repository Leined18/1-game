import pygame
import random

ANCHO = 800
ALTO = 600

NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE = (0,255,0)
AZUL = (0,0,255)

class enemy(pygame.sprite.Sprite):
    def __init__(self):

        # heredamos la variable de la clase sprite
        super().__init__()
        # cargar la imagen del enemigo
        self.image = pygame.image.load("enemy1.png")
        #Obtener el rectangulo del sprite

        self.rect = self.image.get_rect()
        # posicionar mi imagen

        self.rect.center = (450, 500)

        # Aparicion aleatoria
            # Aparicion en x
        self.rect.x = random.randrange(ANCHO - self.rect.width)
            # Aparicion en y
        self.rect.y = random.randrange(250 - self.rect.height)

        # Movimientos del personaje

        self.velocidad_x = random.randrange(1,8)
        self.velocidad_y = random.randrange(1,4)
 
    def update(self):

        self.rect.x -= self.velocidad_x
        self.rect.y += self.velocidad_y 

    #  Limite de mi rango izquierdo
        if self.rect.left <0:
            self.velocidad_x -=1
    #  Limite de mi rango derecho
        if self.rect.right >ANCHO:
            self.velocidad_x +=1
    #  Limite de mi rango de abajo
        if self.rect.bottom >600:
            self.velocidad_y -=1
    #  Limite de mi rango superior
        if self.rect.top <0:
            self.velocidad_y +=1


class enemy2(pygame.sprite.Sprite):
    def __init__(self):

        # heredamos la variable de la clase sprite
        super().__init__()
        # cargar la imagen del enemigo
        self.image = pygame.image.load("enemy2.png")
        #Obtener el rectangulo del sprite

        self.rect = self.image.get_rect()
        # posicionar mi imagen

        self.rect.center = (450, 500)

        # Aparicion aleatoria
            # Aparicion en x
        self.rect.x = random.randrange(ANCHO - self.rect.width)
            # Aparicion en y
        self.rect.y = random.randrange(250 - self.rect.height)

        # Movimientos del personaje

        self.velocidad_x = random.randrange(1,10)
        self.velocidad_y = random.randrange(1,7)
 
    def update(self):

        self.rect.x -= self.velocidad_x
        self.rect.y += self.velocidad_y 

    #  Limite de mi rango izquierdo
        if self.rect.left <0:
            self.velocidad_x -=1

    #  Limite de mi rango derecho
        if self.rect.right >ANCHO:
            self.velocidad_x +=1

    #  Limite de mi rango de abajo
        if self.rect.bottom >ALTO:
            self.velocidad_y -=1

    #  Limite de mi rango superior
        if self.rect.top <0:
            self.velocidad_y +=1
        

        