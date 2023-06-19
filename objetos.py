import pygame
import random
import pygame.mixer

class Misil():
    def __init__(self, x, y, ancho, alto, color) -> None:
        self.imagen = pygame.image.load('img/misil.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.disparo = False


class Nave():
    def __init__(self, x, y, ancho, alto, color) -> None:
        self.imagen = pygame.image.load('img/nave.png')
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
        self.vidas = 5
        self.destruida = False
        self.invasores_destruidos = 0
        self.recuperandose = False
        self.sonido_disparo = pygame.mixer.Sound("sound/laser1.wav")
        self.sonido_disparo.set_volume(0.5)
        self.sonido_destruido = pygame.mixer.Sound("sound/explosion.wav")
        self.sonido_destruido.set_volume(0.5)
        self.sonido_victoria = pygame.mixer.Sound("sound/won.wav")
        self.sonido_victoria.set_volume(0.5)
        self.ejecutar_sonido = True
    
    def mover_nave(self,pos):
        if pos < 550:
            self.rect.x = pos
            self.frente.x = self.rect.x+self.ancho/2-15
            self.alas.x = self.rect.x+self.ancho/2-25
            if not self.misil.disparo:
                self.misil.rect.x = self.rect.x+self.ancho/2-5
    
    def disparar_misil(self):
        if self.misil.disparo:
            self.misil.rect.y -= 10
            if self.misil.rect.y <= self.misil.alto-self.misil.alto*2:
                self.misil.rect.y = self.rect.y
                self.misil.rect.x = self.rect.x+self.ancho/2-self.misil.ancho/2
                self.misil.disparo = False
    
    def recibir_disparo(self, invasor, timer_recuperacion):
        if (self.frente.colliderect(invasor.misil.rect) or self.alas.colliderect(invasor.misil.rect)) and not self.recuperandose:
            pygame.time.set_timer(timer_recuperacion, 3000)
            invasor.misil.rect.y = invasor.rect.y
            invasor.misil.rect.x = invasor.rect.x+invasor.ancho/2-invasor.misil.ancho/2
            invasor.misil.disparo = False
            self.vidas -= 1
            self.recuperandose = True
            self.imagen = pygame.image.load('img/nave_recuperandose.png')
            self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))


class Invasor(pygame.sprite.Sprite):
    def __init__(self, ancho, alto, color, valor, velocidad_misil_min, velocidad_misil_max):
        super().__init__()
        self.imagen = pygame.image.load('img/invasor.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(0, 600-ancho)
        self.rect.y = random.randrange(-900,-100)
        self.velocidad_x = random.randrange(1,3)
        self.velocidad_y = random.randrange(1,3)
        self.color = color
        self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
        self.misil = Misil(self.rect.x+self.ancho/2, self.rect.y, 10,30,(0,0,255))
        self.ingreso = False
        self.misil.imagen = pygame.transform.rotate(self.misil.imagen, 180)
        self.velocidad_misil_min= velocidad_misil_min
        self.velocidad_misil_max= velocidad_misil_max
        self.valor = valor
        self.sonido_disparo = pygame.mixer.Sound("sound/laser4.wav")
        self.sonido_disparo.set_volume(0.5)
        self.disparo_recibido = False
    
    def eliminar(self, lista_invasores):
        if self.disparo_recibido and self.misil.rect.top <= 0 or self.disparo_recibido and not self.misil.disparo:
            lista_invasores.remove(self)

    def recibir_disparo(self, nave: Nave, puntos: int):
        if nave.misil.rect.colliderect(self.punto_disparo):
            puntos = puntos + self.valor
            nave.invasores_destruidos += 1
            self.rect.y = -500
            self.rect.x = -500
            nave.misil.rect.y = nave.rect.y
            nave.misil.rect.x = nave.rect.x+nave.ancho/2-nave.misil.ancho/2
            nave.misil.disparo = False
            self.imagen = pygame.transform.scale(self.imagen, (0, 0))
            self.disparo_recibido = True

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
        self.misil.rect.y += random.randrange(self.velocidad_misil_min,self.velocidad_misil_max)
        if self.misil.rect.y >= alto_pantalla + alto_pantalla/2:
            self.misil.rect.y = self.rect.y
            self.misil.rect.x = self.rect.x+self.ancho/2-self.misil.ancho/2
            self.misil.disparo = False
    
    def ingresar(self):
        self.rect.y += self.velocidad_y
        self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
        if not self.misil.disparo:
            self.misil.rect.y = self.rect.y
            self.misil.rect.x = self.rect.x+self.ancho/2-5 
        if self.rect.bottom >= 150:
            self.ingreso = True

class Boton():
    def __init__(self, x, y, ancho, alto, imagen) -> None:
        self.imagen = pygame.image.load(imagen)
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y