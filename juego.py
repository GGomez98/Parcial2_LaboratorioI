import pygame
import pygame.mixer
import random
import re
import sys
import objetos
from inicio import *
from instrucciones import *
from nivel_1 import *

def crear_invasores(cantidad, lista_invasores):

    for _ in range(cantidad):
        invasor = objetos.Invasor(70,50,(0,255,0), 50)
        lista_invasores.add(invasor)

def temporizador(tiempo: dict):
    tiempo['segundos'] += 1
    if tiempo['segundos']>59:
        tiempo['segundos'] = 0
        tiempo['minutos'] += 1

    return tiempo

pygame.init()
pygame.mixer.init()

fondo_imagen = pygame.image.load("Parcial_2/img/fondo.png")
ALTO_PANTALLA = 800
ANCHO_PANTALLA = 600
pantalla_actual = 1

fuente = pygame.font.Font('Parcial_2/fonts/ethnocentric/ethnocentric rg.otf', 70)
fuente_pantalla_2 = pygame.font.Font('Parcial_2/fonts/ethnocentric/ethnocentric rg.otf', 20)
titulo = fuente.render("Invasores", True, (255,255,255))

btn_start = objetos.Boton(100,300,410,121)

nave = objetos.Nave(350,700,50,50,(255,0,0))
invasores = pygame.sprite.Group()
puntaje = 0
tiempo = {"minutos": 0, "segundos": 0}
nivel_iniciado = False

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

    if pantalla_actual == 1:
        pantalla_actual = pantalla_inicio(btn_start, pantalla_actual,window)
    
    if pantalla_actual == 2:
        pantalla_actual = pantalla_instrucciones(window, pantalla_actual)
    
    if pantalla_actual == 3:
        if not nivel_iniciado:
            crear_invasores(5, invasores)
            nivel_iniciado = True
        puntaje = nivel_1(window, invasores, nave, timer_10_milisegundos, timer_recuperacion, timer_segundo, timer_disparo_invasores, tiempo, fuente_pantalla_2, puntaje)