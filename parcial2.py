import pygame
import random
import sys
import objetos

aux_nave = objetos.Nave(350,700,50,50,(255,0,0))
aux_misil = objetos.Misil(aux_nave.rect.x+aux_nave.ancho/2-5,700,10,30,(0,0,255))
fondo_imagen = pygame.image.load("Parcial_2/img/fondo.png")
invasores = []

def crear_invasores(cantidad):

    for _ in range(cantidad):
        invasor = objetos.Invasor(70,50,(0,255,0))
        invasores.append(invasor)

crear_invasores(5)


pygame.init()

running = True

window = pygame.display.set_mode((600,800))
pygame.display.set_caption("Juego")

timer_disparo_misil = pygame.USEREVENT
pygame.time.set_timer(timer_disparo_misil, 10)

while running:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False
            sys.exit()
        if evento.type == pygame.MOUSEMOTION:
            aux_nave.mover_nave(evento.pos[0])
            if not aux_misil.disparo:
                aux_misil.rect.x = aux_nave.rect.x+aux_nave.ancho/2-5
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            aux_misil.disparo = True
        aux_misil.disparar(aux_nave, evento, timer_disparo_misil)
        for invasor in invasores:
            invasor.recibir_disparo(aux_misil, aux_nave, timer_disparo_misil, evento)
    
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    #pygame.draw.rect(window, aux_nave.color, aux_nave.rect)
    #pygame.draw.rect(window, aux_misil.color, aux_misil.rect)
    window.blit(aux_misil.imagen, aux_misil.rect)
    window.blit(aux_nave.imagen, aux_nave.rect)
    for invasor in invasores:
        #pygame.draw.rect(window, invasor.color, invasor.rect)
        #pygame.draw.rect(window, (100,100,100), invasor.punto_disparo)
        window.blit(invasor.imagen, invasor.rect)
    pygame.display.flip()
    pygame.display.update()