import pygame
import pygame.mixer
import sys

def pantalla_instrucciones(window, pantalla_actual):
    fondo_imagen = pygame.image.load("Parcial_2/img/fondo.png")
    ethnocentric = pygame.font.Font('Parcial_2/fonts/ethnocentric/ethnocentric rg.otf', 19)
    instrucciones_1 = ethnocentric.render("Destruye a los invasores y evita que", True, (255,255,255))
    instrucciones_2 = ethnocentric.render("te disparen.", True, (255,255,255))
    instrucciones_3 = ethnocentric.render("Muevete con el mouse y haz click", True, (255,255,255))
    instrucciones_4 = ethnocentric.render("derecho para disparar.", True, (255,255,255))
    instrucciones_5 = ethnocentric.render("Click derecho para iniciar", True, (255,255,255))
    pantalla_actual = 2
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