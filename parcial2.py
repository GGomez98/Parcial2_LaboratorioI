import pygame
import pygame.mixer
import random
import re
import sys
import objetos

def crear_invasores(cantidad, lista_invasores):

    for _ in range(cantidad):
        invasor = objetos.Invasor(70,50,(0,255,0), 50)
        lista_invasores.add(invasor)

def temporizador(tiempo: dict):
    tiempo['segundos'] += 1
    if tiempo['segundos']>59:
        tiempo['segundos'] = 0
        tiempo['minutos'] += 1
    
    #segundos_txt = str(tiempo['segundos']).zfill(2)
    #minutos_txt =  str(tiempo['minutos']).zfill(2)

    return tiempo

pygame.init()
pygame.mixer.init()

fondo_imagen = pygame.image.load("Parcial_2/img/fondo.png")
ALTO_PANTALLA = 800
ANCHO_PANTALLA = 600

nave = objetos.Nave(350,700,50,50,(255,0,0))
invasores = pygame.sprite.Group()
puntaje = 0
fuente = pygame.font.SysFont('Helvetica', 30)
tiempo = {"minutos": 0, "segundos": 0}

crear_invasores(5, invasores)

running = True

timer_10_milisegundos = pygame.USEREVENT
pygame.time.set_timer(timer_10_milisegundos, 10)

timer_disparo_invasores = pygame.USEREVENT+1
pygame.time.set_timer(timer_disparo_invasores, random.randrange(500, 1500))

timer_recuperacion = pygame.USEREVENT+2
pygame.time.set_timer(timer_recuperacion, 3000)

timer_segundo = pygame.USEREVENT+3
pygame.time.set_timer(timer_segundo, 1000)

window = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption("Juego")

while running:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False
            sys.exit()
        if evento.type == pygame.MOUSEMOTION and not nave.destruida:
            nave.mover_nave(evento.pos[0])

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not nave.destruida:
            if not nave.misil.disparo:
                nave.sonido_disparo.play()
            nave.misil.disparo = True
            
        if evento.type == timer_10_milisegundos and not nave.destruida:
            nave.disparar_misil()
            for invasor in invasores:
                if invasor.ingreso:
                    invasor.mover(ALTO_PANTALLA, ANCHO_PANTALLA)
                    if invasor.misil.disparo :
                        invasor.disparar_misil(ALTO_PANTALLA)
                else:
                    invasor.ingresar()
        
        if evento.type == timer_recuperacion and nave.recuperandose:
            nave.recuperandose = False
        
        if evento.type == timer_segundo and not nave.destruida:
            temporizador(tiempo)
        
        for invasor in invasores:
            if (evento.type == timer_disparo_invasores or invasor.rect.x == nave.rect.x) and not nave.destruida and invasor.ingreso and not invasor.misil.disparo:
                if not invasor.misil.disparo:
                    invasor.sonido_disparo.play()
                invasor.misil.disparo = True
        
        if nave.vidas == 0:
            nave.destruida = True
            
        
    for invasor in invasores:
        puntaje = invasor.recibir_disparo(nave, puntaje, invasores)
        puntaje_render = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
        nave.recibir_disparo(invasor)
        invasor.aumentar_dificultad(nave)
    

    
    vidas_render = fuente.render(f"Vidas: {nave.vidas}", True, (255,255,255))
    
    segundos_txt = str(tiempo['segundos']).zfill(2)
    minutos_txt =  str(tiempo['minutos']).zfill(2)
    tiempo_txt = f"{minutos_txt}:{segundos_txt}"
    tiempo_render = fuente.render(tiempo_txt, True, (255,255,255))
    
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
    window.blit(vidas_render, (ANCHO_PANTALLA-100,20))
    window.blit(tiempo_render, (ANCHO_PANTALLA/2-50,20))
    #pygame.draw.rect(window, (0,0,0), nave.frente)
    #pygame.draw.rect(window, (0,0,0), nave.alas)
    pygame.display.flip()
    pygame.display.update()