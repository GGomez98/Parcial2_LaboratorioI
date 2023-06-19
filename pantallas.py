import pygame
import pygame.mixer
import sys
import re
from database import *
from funciones import *

def fin_del_juego(window, nave, invasores, puntaje, tiempo, nombre):
    fondo_imagen = pygame.image.load("img/fondo.png")
    ANCHO_PANTALLA = 600
    fuente_2 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 20)
    fuente_3 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 18)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if re.match("[A-Za-z0-9]", evento.unicode) and len(nombre) < 5:
                nombre+= evento.unicode
            elif evento.key == pygame.K_BACKSPACE:
                nombre = nombre[:-1]
            elif evento.key == pygame.K_RETURN:
                if nombre != '':
                    tiempo_txt = f"{str(tiempo['minutos']).zfill(2)}: {str(tiempo['segundos']).zfill(2)}"
                    insert_datos(nombre, puntaje, tiempo_txt, "bd_btf.db")
                    nombre = 'datos cargados'

    retorno = nombre

    if nave.vidas == 0:
        mensaje_render = fuente_2.render("Los invasores ganaron", True, (255,255,255))
        pos_mensaje = (ANCHO_PANTALLA/2-200, 300)
    elif len(invasores) == 0:
        mensaje_render = fuente_2.render("Felicidades! Ganaste!", True, (255,255,255))
        pos_mensaje = (ANCHO_PANTALLA/2-150, 300)

    nombre_render = fuente_2.render(nombre, True, (255,255,255))
    puntaje_render = fuente_2.render(f"Tu puntaje final es {puntaje}", True, (255,255,255))
    minutos_txt = str(tiempo['minutos']).zfill(2)
    segundos_txt = str(tiempo['segundos']).zfill(2)
    tiempo_render = fuente_2.render(f"Tu duracion fue de {minutos_txt}:{segundos_txt}", True, (255,255,255))
    indicador_render = fuente_2.render("Ingrese aqui su nombre", True, (255,255,255))
    enter_render = fuente_3.render("Oprima 'Enter' para ingresar su nombre", True, (255,255,255))

    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(mensaje_render, pos_mensaje)
    window.blit(puntaje_render, (ANCHO_PANTALLA/2-190, 350))
    window.blit(tiempo_render, (ANCHO_PANTALLA/2-190, 400))
    window.blit(indicador_render, (ANCHO_PANTALLA/2-190, 450))
    pygame.draw.rect(window, (128,128,128), (ANCHO_PANTALLA/2-125, 500, 200, 50))
    window.blit(nombre_render, (ANCHO_PANTALLA/2-120, 510))
    window.blit(enter_render, (ANCHO_PANTALLA/2-290, 700))
    pygame.display.flip()
    pygame.display.update()

    return retorno

def cortina(window, pantalla_actual, timer, nivel):
    fondo_imagen = pygame.image.load("img/fondo.png")
    ANCHO_PANTALLA = 600
    fuente_2 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 20)
    nivel_render = fuente_2.render(nivel, True, (255,255,255))
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()  
        if evento.type == timer and nivel == "Nivel 1":
            pantalla_actual = 4
        elif evento.type == timer and nivel == "Nivel 2":
            pantalla_actual = 6
        elif evento.type == timer and nivel == "Nivel 3":
            pantalla_actual = 8

    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(nivel_render, (ANCHO_PANTALLA/2-50, 400))
    pygame.display.flip()
    pygame.display.update()

    return pantalla_actual
    

def pantalla_instrucciones(window, pantalla_actual):
    fondo_imagen = pygame.image.load("img/fondo.png")
    ethnocentric = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 19)
    instrucciones_1 = ethnocentric.render("Destruye a los invasores y evita que", True, (255,255,255))
    instrucciones_2 = ethnocentric.render("te disparen.", True, (255,255,255))
    instrucciones_3 = ethnocentric.render("Muevete con el mouse y haz click", True, (255,255,255))
    instrucciones_4 = ethnocentric.render("derecho para disparar.", True, (255,255,255))
    instrucciones_5 = ethnocentric.render("Click izquierdo para iniciar", True, (255,255,255))
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()  
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pantalla_actual = 3
    
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(instrucciones_1, (10,100))
    window.blit(instrucciones_2, (10,130))
    window.blit(instrucciones_3, (10,170))
    window.blit(instrucciones_4, (10,200))
    window.blit(instrucciones_5, (100,700))
    pygame.display.flip()
    pygame.display.update()

    return pantalla_actual


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

def pantalla_inicio(btn_start, btn_higscore, pantalla_actual, window):
    ANCHO_PANTALLA = 600
    fondo_imagen = pygame.image.load("img/fondo.png")
    ethnocentric = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 70)
    titulo = ethnocentric.render("Invasores", True, (255,255,255))
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if btn_start.rect.collidepoint(mouse_x,mouse_y):
                pantalla_actual = 2
            elif btn_higscore.rect.collidepoint(mouse_x,mouse_y):
                pantalla_actual = 10
    
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(btn_start.imagen, btn_start.rect)
    window.blit(btn_higscore.imagen, btn_higscore.rect)
    window.blit(titulo, (ANCHO_PANTALLA/2-titulo.get_width()/2,100))
    pygame.display.flip()
    pygame.display.update()
                

    return pantalla_actual

def pantalla_puntuaciones(window, pantalla_actual):

    fondo_imagen = pygame.image.load("img/fondo.png")
    fuente_3 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 18)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
           if evento.key == pygame.K_ESCAPE:
            pantalla_actual = 1
    
    salir_render = fuente_3.render("Oprima 'ESC' para salir", True, (255,255,255))
    

    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    leer_csv("puntuaciones.csv", fuente_3, window)
    window.blit(salir_render,(135, 750))
    pygame.display.flip()
    pygame.display.update()

    return pantalla_actual