import pygame
import pygame.mixer
import sys
import re

"""pygame.init()

fondo_imagen = pygame.image.load("img/fondo.png")
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 800
fuente_2 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 20)
nombre = ''

running = True

window = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption("Juego")

while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if re.match("[A-Za-z0-9]", evento.unicode):
                nombre+= evento.unicode
            elif evento.key == pygame.K_BACKSPACE:
                nombre = nombre[:-1]
    
    nombre_render = fuente_2.render(nombre, True, (255,255,255))
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(nombre_render, (ANCHO_PANTALLA/2-190, 450))
    pygame.display.flip()
    pygame.display.update()"""

def ingresar_nombre(window, nombre):
    fondo_imagen = pygame.image.load("img/fondo.png")
    ANCHO_PANTALLA = 600
    fuente_2 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 20)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if re.match("[A-Za-z0-9]", evento.unicode):
                nombre+= evento.unicode
            elif evento.key == pygame.K_BACKSPACE:
                nombre = nombre[:-1]
    nombre_render = fuente_2.render(nombre, True, (255,255,255))
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(nombre_render, (ANCHO_PANTALLA/2-190, 500))
    pygame.display.flip()
    pygame.display.update()

    return nombre

def fin_del_juego(window, nave, invasores, puntaje, tiempo):
    fondo_imagen = pygame.image.load("img/fondo.png")
    ANCHO_PANTALLA = 600
    fuente_2 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 20)
    pantalla_actual = 9
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()

    if nave.vidas == 0:
        mensaje_render = fuente_2.render("Los invasores ganaron", True, (255,255,255))
        pos_mensaje = (ANCHO_PANTALLA/2-200, 300)
    elif len(invasores) == 0:
        mensaje_render = fuente_2.render("Felicidades! Ganaste!", True, (255,255,255))
        pos_mensaje = (ANCHO_PANTALLA/2-150, 300)

    puntaje_render = fuente_2.render(f"Tu puntaje final es {puntaje}", True, (255,255,255))
    minutos_txt = str(tiempo['minutos']).zfill(2)
    segundos_txt = str(tiempo['segundos']).zfill(2)
    tiempo_render = fuente_2.render(f"Tu duracion fue de {minutos_txt}:{segundos_txt}", True, (255,255,255))
    indicador_render = fuente_2.render("Ingrese aqui su nombre", True, (255,255,255))
    
    
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(mensaje_render, pos_mensaje)
    window.blit(puntaje_render, (ANCHO_PANTALLA/2-190, 350))
    window.blit(tiempo_render, (ANCHO_PANTALLA/2-190, 400))
    window.blit(indicador_render, (ANCHO_PANTALLA/2-190, 450))
    pygame.display.flip()
    pygame.display.update()

    return pantalla_actual

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