from typing import Any
import pygame



# DIMENTSIONES DE LA VENTANA 
ANCHO = 800
ALTO = 600
# COLORES A UTILIZAR 
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE = (0,255,0)
AZUL = (0,0,255)

class fire (pygame.sprite.Sprite):

    def __init__(self, x,y):
        
       super().__init__()

       self.image = pygame.image.load("disparo.png")
       self.rect = self.image.get_rect()
       self.rect.bottom = y
       self.rect.centerx = x

    def update(self):
        self.rect.y -=10

        if self.rect.bottom < 0:
            self.kill
        