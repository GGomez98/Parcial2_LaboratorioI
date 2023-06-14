import pygame
import pygame.mixer
import random
import re
import sys
import objetos

def temporizador(tiempo: dict):
    tiempo['segundos'] += 1
    if tiempo['segundos']>59:
        tiempo['segundos'] = 0
        tiempo['minutos'] += 1

    return tiempo

def nivel(window, invasores, nave, timer_10_milisegundos, timer_recuperacion, timer_segundo, tiempo, fuente, puntaje, nivel):
    ALTO_PANTALLA = 800
    ANCHO_PANTALLA = 600
    fondo_imagen = pygame.image.load("img/fondo.png")

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
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
        if evento.type == timer_recuperacion and nave.recuperandose and nave.vidas != 0:
            nave.recuperandose = False
            nave.imagen = pygame.image.load('img/nave.png')
            nave.imagen = pygame.transform.scale(nave.imagen, (nave.ancho, nave.alto))
        if evento.type == timer_segundo and not nave.destruida:
            temporizador(tiempo)
        for invasor in invasores:
            if invasor.rect.x == nave.rect.x and not nave.destruida and invasor.ingreso and not invasor.misil.disparo:
                if not invasor.misil.disparo:
                    invasor.sonido_disparo.play()
                invasor.misil.disparo = True
                #pygame.time.set_timer(timer_disparo_invasores, random.randrange(1000, 5000))
        if nave.vidas == 0:
            nave.destruida = True
    for invasor in invasores:
        puntaje = invasor.recibir_disparo(nave, puntaje)
        invasor.eliminar(invasores)
        nave.recibir_disparo(invasor, timer_recuperacion)
    puntaje_txt = str(puntaje).zfill(5)
    puntaje_render = fuente.render(f"Puntaje: {puntaje_txt}", True, (255,255,255))
    vidas_render = fuente.render(f"Vidas: {nave.vidas}", True, (255,255,255))
    segundos_txt = str(tiempo['segundos']).zfill(2)
    minutos_txt =  str(tiempo['minutos']).zfill(2)
    tiempo_txt = f"{minutos_txt}:{segundos_txt}"
    tiempo_render = fuente.render(tiempo_txt, True, (255,255,255))
    nivel_render = fuente.render(nivel, True, (255,255,255))
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(nave.imagen, nave.rect)
    window.blit(nave.misil.imagen, nave.misil.rect)
    for invasor in invasores:
        window.blit(invasor.misil.imagen, invasor.misil.rect)
        window.blit(invasor.imagen, invasor.rect)
    window.blit(puntaje_render, (5,20))
    window.blit(vidas_render, (ANCHO_PANTALLA-130,20))
    window.blit(tiempo_render, (ANCHO_PANTALLA/2-45,20))
    window.blit(nivel_render, (ANCHO_PANTALLA/2+50,20))
    pygame.display.flip()
    pygame.display.update()

    return puntaje
    