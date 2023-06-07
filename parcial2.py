import pygame
import random
import sys
import objetos

def crear_invasores(cantidad, lista_invasores):

    for _ in range(cantidad):
        invasor = objetos.Invasor(70,50,(0,255,0))
        lista_invasores.add(invasor)


pygame.init()

fondo_imagen = pygame.image.load("Parcial_2/img/fondo.png")
ALTO_PANTALLA = 800
ANCHO_PANTALLA = 600

nave = objetos.Nave(350,700,50,50,(255,0,0))
invasores = pygame.sprite.Group()
puntaje = 0
fuente_puntaje = pygame.font.SysFont('Helvetica', 30)

crear_invasores(5, invasores)

running = True

timer_10_milisegundos = pygame.USEREVENT
pygame.time.set_timer(timer_10_milisegundos, 10)

timer_segundo = pygame.USEREVENT+1
pygame.time.set_timer(timer_segundo, 1000)

window = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption("Juego")

while running:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False
            sys.exit()
        if evento.type == pygame.MOUSEMOTION:
            nave.mover_nave(evento.pos[0])

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            nave.misil.disparo = True
            
        if evento.type == timer_10_milisegundos:
            nave.disparar_misil()
            for invasor in invasores:
                invasor.mover(ALTO_PANTALLA, ANCHO_PANTALLA)
                invasor.disparar_misil(ALTO_PANTALLA)
            
        
    for invasor in invasores:
        puntaje = invasor.recibir_disparo(nave, puntaje)
        puntaje_render = fuente_puntaje.render(f"Puntaje: {puntaje}", True, (255,255,255))
        nave.recibir_disparo(invasor)
    
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    #pygame.draw.rect(window, nave.color, nave.rect)
    window.blit(nave.imagen, nave.rect)
    #pygame.draw.rect(window, nave.misil.color, nave.misil.rect)
    window.blit(nave.misil.imagen, nave.misil.rect)
    for invasor in invasores:
        #pygame.draw.rect(window, invasor.color, invasor.rect)
        #pygame.draw.rect(window, (100,100,100), invasor.punto_disparo)
        #pygame.draw.rect(window, invasor.misil.color, invasor.misil.rect)
        window.blit(invasor.misil.imagen, invasor.misil.rect)
        window.blit(invasor.imagen, invasor.rect)
    window.blit(puntaje_render, (5,20))
    #pygame.draw.rect(window, (0,0,0), nave.frente)
    #pygame.draw.rect(window, (0,0,0), nave.alas)
    pygame.display.flip()
    pygame.display.update()