import pygame
import pygame.mixer
import objetos
from pantallas import *
from funciones import *

pygame.init()
pygame.mixer.init()

fondo_imagen = pygame.image.load("img/fondo.png")
ALTO_PANTALLA = 800
ANCHO_PANTALLA = 600
pantalla_actual = 1
crear_tabla("DB/puntuaciones.db", 'puntuaciones')

fuente = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 70)
fuente_2 = pygame.font.Font('fonts/ethnocentric/ethnocentric rg.otf', 20)
titulo = fuente.render("Invasores", True, (255,255,255))

btn_start = objetos.Boton(100,300,410,121,'img/start_BTN.png')
btn_higscore = objetos.Boton(255,441,121,121, 'img/highscores.png')

nave = objetos.Nave(350,700,50,50,(255,0,0))
invasores = pygame.sprite.Group()
puntaje = 0
tiempo = {"minutos": 0, "segundos": 0}
nivel_iniciado = False
puntuaciones = get_datos("DB/puntuaciones.db")
cargar_lista(puntuaciones, "DB/puntuaciones.csv")

nombre = ''

running = True

timer_10_milisegundos = pygame.USEREVENT
pygame.time.set_timer(timer_10_milisegundos, 10)

timer_recuperacion = pygame.USEREVENT+2

timer_segundo = pygame.USEREVENT+3
pygame.time.set_timer(timer_segundo, 1000)

timer_3_segundos = pygame.USEREVENT+4

window = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.display.set_caption("Juego")

while running:

    if pantalla_actual == 1:
        pantalla_actual = pantalla_inicio(btn_start, btn_higscore, pantalla_actual ,window)
    
    if pantalla_actual == 2:
        pantalla_actual = pantalla_instrucciones(window, pantalla_actual)
        pygame.time.set_timer(timer_3_segundos, 3000)
    
    if pantalla_actual == 3:
        pantalla_actual = cortina(window, pantalla_actual, timer_3_segundos, "Nivel 1")

    if pantalla_actual == 4:
        if not nivel_iniciado:
            crear_invasores(5, invasores, 5, 10, 50)
            nivel_iniciado = True
        elif len(invasores) == 0 and nivel_iniciado:
            pantalla_actual = 5
            nivel_iniciado = False
            pygame.time.set_timer(timer_3_segundos, 3000)
        puntaje = nivel(window, invasores, nave, timer_10_milisegundos, timer_recuperacion, timer_segundo, tiempo, fuente_2, puntaje, "Nivel 1")
        if nave.vidas == 0:
            pantalla_actual = 9

    if pantalla_actual == 5:
        pantalla_actual = cortina(window, pantalla_actual, timer_3_segundos, "Nivel 2")

    if pantalla_actual == 6:
        if not nivel_iniciado:
            crear_invasores(10, invasores, 10, 15, 75)
            nivel_iniciado = True
        elif len(invasores) == 0 and nivel_iniciado:
            pantalla_actual = 7
            nivel_iniciado = False
            pygame.time.set_timer(timer_3_segundos, 3000)
        puntaje = nivel(window, invasores, nave, timer_10_milisegundos, timer_recuperacion, timer_segundo, tiempo, fuente_2, puntaje, "Nivel 2")
        if nave.vidas == 0:
            pantalla_actual = 9

    if pantalla_actual == 7:
        pantalla_actual = cortina(window, pantalla_actual, timer_3_segundos, "Nivel 3")
    if pantalla_actual == 8:
        if not nivel_iniciado:
            crear_invasores(20, invasores, 20, 25, 100)
            nivel_iniciado = True
        puntaje = nivel(window, invasores, nave, timer_10_milisegundos, timer_recuperacion, timer_segundo, tiempo, fuente_2, puntaje, "Nivel 3")
        if nave.vidas == 0 or len(invasores) == 0:
            pantalla_actual = 9
    
    if pantalla_actual == 9:
        nombre = fin_del_juego(window, nave, invasores, puntaje, tiempo, nombre)
        if nombre == 'datos cargados':
            nombre = ''
            puntaje = 0
            tiempo = {"minutos": 0, "segundos": 0}
            nave = objetos.Nave(350,700,50,50,(255,0,0))
            pantalla_actual = 1
            invasores = pygame.sprite.Group()
            nivel_iniciado = False
            puntuaciones = get_datos("DB/puntuaciones.db")
            cargar_lista(puntuaciones, "DB/puntuaciones.csv")
    
    if pantalla_actual == 10:
        pantalla_actual = pantalla_puntuaciones(window, pantalla_actual)

    

