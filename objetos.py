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
        self.rect.y = random.randrange(0, 500/2-alto)
        self.color = color
        self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
    
    def recibir_disparo(self, misil, nave):
        if self.punto_disparo.colliderect(misil.rect):
            self.rect.x = random.randrange(0, 600-self.ancho)
            self.rect.y = random.randrange(0, 500/2-self.alto)
            self.punto_disparo = pygame.Rect(self.rect.x+10, self.rect.y+50-10, 50, 10)
            misil.rect.y = nave.rect.y
            misil.rect.x = nave.rect.x+nave.ancho/2-misil.ancho/2
            misil.disparo = False


class Misil():
    def __init__(self, x, y, ancho, alto, color, disparo) -> None:
        self.imagen = pygame.image.load('Parcial_2/img/misil.png')
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.disparo = disparo
    
    def disparar(self, nave: Nave):
        self.rect.y -= 10
        if self.rect.y <= self.alto-self.alto*2:
            self.rect.y = nave.rect.y
            self.rect.x = nave.rect.x+nave.ancho/2-self.ancho/2
            self.disparo = False


"""aux_nave = Nave(350,400,50,50,(255,0,0))
aux_invasor = Invasor(70,50,(0,255,0))
aux_misil = Misil(aux_nave.rect.x+aux_nave.ancho/2-5,400,10,30,(0,0,255), False)


pygame.init()

running = True

window = pygame.display.set_mode((600,500))
pygame.display.set_caption("Prueba objetos")

timer_disparo_misil = pygame.USEREVENT
pygame.time.set_timer(timer_disparo_misil, 10)

while running:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False
        if evento.type == pygame.MOUSEMOTION:
            aux_nave.mover_nave(evento.pos[0])
            if not aux_misil.disparo:
                aux_misil.rect.x = aux_nave.rect.x+aux_nave.ancho/2-5
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            aux_misil.disparo = True
        if evento.type == timer_disparo_misil and aux_misil.disparo:
            aux_misil.disparar(aux_nave)
            aux_invasor.recibir_disparo(aux_misil, aux_nave)
    
    window.fill((0,0,0))
    pygame.draw.rect(window, aux_nave.color, aux_nave.rect)
    pygame.draw.rect(window, aux_invasor.color, aux_invasor.rect)
    pygame.draw.rect(window, aux_misil.color, aux_misil.rect)
    window.blit(aux_misil.imagen, aux_misil.rect)
    window.blit(aux_nave.imagen, aux_nave.rect)
    window.blit(aux_invasor.imagen, aux_invasor.rect)
    pygame.display.flip()"""
        