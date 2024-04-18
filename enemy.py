import pygame
import random
import os

# Dimensiones de la ventana
ANCHO = 1000
ALTO = 800

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (250, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Directorio de assets
ASSETS_DIR = "assets"

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(ASSETS_DIR, "enemy1.png"))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(250 - self.rect.height)
        self.velocidad_x = random.randrange(1, 8)
        self.velocidad_y = random.randrange(1, 4)

    def update(self):
        self.rect.x -= self.velocidad_x
        self.rect.y += self.velocidad_y
        if self.rect.left < 0:
            self.velocidad_x -= 1
        if self.rect.right > ANCHO:
            self.velocidad_x += 1
        if self.rect.bottom > 600:
            self.velocidad_y -= 1
        if self.rect.top < 0:
            self.velocidad_y += 1

class enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(ASSETS_DIR, "enemy2.png"))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(250 - self.rect.height)
        self.velocidad_x = random.randrange(1, 2)
        self.velocidad_y = random.randrange(1, 5)

    def update(self):
        self.rect.x -= self.velocidad_x
        self.rect.y += self.velocidad_y
        if self.rect.left < 0:
            self.velocidad_x -= 1
        if self.rect.right > ANCHO:
            self.velocidad_x += 1
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        if self.rect.top < 0:
            self.velocidad_y += 1
