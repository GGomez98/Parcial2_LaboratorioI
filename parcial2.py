import pygame
import random
import sys
sys.path.append('/Parcial_2/objetos.py')
import objetos

aux_nave = objetos.Nave(350,400,50,50,(255,0,0))
aux_invasor = objetos.Invasor(70,50,(0,255,0))
aux_misil = objetos.Misil(aux_nave.rect.x+aux_nave.ancho/2-5,400,10,30,(0,0,255), False)


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
    pygame.draw.rect(window, (100,100,100), aux_invasor.punto_disparo)
    window.blit(aux_misil.imagen, aux_misil.rect)
    window.blit(aux_nave.imagen, aux_nave.rect)
    window.blit(aux_invasor.imagen, aux_invasor.rect)
    pygame.display.flip()