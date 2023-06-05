import pygame
import random



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
    
    def mover_nave(self,pos):
        if pos < 550:
            self.rect.x = pos

class Invasor():
    def __init__(self, ancho, alto, color) -> None:
        self.imagen = pygame.image.load('Parcial_2/img/invasor.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(0, 600-ancho)
        self.rect.y = random.randrange(0, 650-alto)
        self.color = color
        self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
    
    def recibir_disparo(self, misil, nave: Nave, timer, evento):
        if evento.type == timer and misil.disparo:
            if self.punto_disparo.colliderect(misil.rect):
                self.rect.x = random.randrange(0, 600-self.ancho)
                self.rect.y = random.randrange(0, 500/2-self.alto)
                self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
                misil.rect.y = nave.rect.y
                misil.rect.x = nave.rect.x+nave.ancho/2-misil.ancho/2
                misil.disparo = False


class Misil():
    def __init__(self, x, y, ancho, alto, color) -> None:
        self.imagen = pygame.image.load('Parcial_2/img/misil.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.disparo = False
    
    def disparar(self, nave: Nave, evento, timer):
        if evento.type == timer and self.disparo:
            self.rect.y -= 10
            if self.rect.y <= self.alto-self.alto*2:
                self.rect.y = nave.rect.y
                self.rect.x = nave.rect.x+nave.ancho/2-self.ancho/2
                self.disparo = False
