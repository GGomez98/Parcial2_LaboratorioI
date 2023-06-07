import pygame
import random

class Misil():
    def __init__(self, x, y, ancho, alto, color) -> None:
        self.imagen = pygame.image.load('Parcial_2/img/misil.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.imagen = pygame.transform.rotate(self.imagen, 180)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.disparo = False
        self.velocidad = 10


class Nave():
    def __init__(self, x, y, ancho, alto, color) -> None:
        self.imagen = pygame.image.load('Parcial_2/img/nave.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.misil = Misil(self.rect.x+self.ancho/2-5,700,10,30,(0,0,255))
        self.frente = pygame.Rect(self.rect.x+self.ancho/2-15, self.rect.y, 30, 10)
        self.alas = pygame.Rect(self.rect.x+self.ancho/2-25, self.rect.y+30, 50, 10)
    
    def mover_nave(self,pos):
        if pos < 550:
            self.rect.x = pos
            self.frente.x = self.rect.x+self.ancho/2-15
            self.alas.x = self.rect.x+self.ancho/2-25
            if not self.misil.disparo:
                self.misil.rect.x = self.rect.x+self.ancho/2-5
    
    def disparar_misil(self):
        if self.misil.disparo:
            self.misil.rect.y -= self.misil.velocidad
            if self.misil.rect.y <= self.misil.alto-self.misil.alto*2:
                self.misil.rect.y = self.rect.y
                self.misil.rect.x = self.rect.x+self.ancho/2-self.misil.ancho/2
                self.misil.disparo = False
    
    def recibir_disparo(self, invasor):
        if self.frente.colliderect(invasor.misil.rect) or self.alas.colliderect(invasor.misil.rect):
            print("Un misil le dio a la nave")


class Invasor(pygame.sprite.Sprite):
    def __init__(self, ancho, alto, color):
        super().__init__()
        self.imagen = pygame.image.load('Parcial_2/img/invasor.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(0, 600-ancho)
        self.rect.y = random.randrange(0, 500-alto)
        self.velocidad_x = random.randrange(1,7)
        self.velocidad_y = random.randrange(1,7)
        self.color = color
        self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
        self.misil = Misil(self.rect.x+self.ancho/2, self.rect.y, 10,30,(0,0,255))
    
    def recibir_disparo(self, nave: Nave, puntos: int):
        if self.punto_disparo.colliderect(nave.misil.rect):
            self.rect.x = random.randrange(0, 600-self.ancho)
            self.rect.y = random.randrange(0, 500/2-self.alto)
            self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
            nave.misil.rect.y = nave.rect.y
            nave.misil.rect.x = nave.rect.x+nave.ancho/2-nave.misil.ancho/2
            nave.misil.disparo = False
            puntos = puntos + 1

        return puntos
            
    
    def mover(self, alto_pantalla, ancho_pantalla):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
        if not self.misil.disparo:
            self.misil.rect.y = self.rect.y
            self.misil.rect.x = self.rect.x+self.ancho/2-5 
        if self.rect.left < 0:
            self.velocidad_x += 1
        if self.rect.right > ancho_pantalla:
            self.velocidad_x *= -1
        if self.rect.bottom > alto_pantalla*0.6:
            self.velocidad_y *= -1
        if self.rect.top < 0:
            self.velocidad_y += 1
    
    def disparar_misil(self, alto_pantalla):
        self.misil.disparo = True
        self.misil.rect.y += random.randrange(3,5)
        if self.misil.rect.y >= alto_pantalla + alto_pantalla/2:
            self.misil.rect.y = self.rect.y
            self.misil.rect.x = self.rect.x+self.ancho/2-self.misil.ancho/2
            self.misil.disparo = False