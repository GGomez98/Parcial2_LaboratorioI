import pygame
import pygame.mixer
import sys

def pantalla_inicio(btn_start, pantalla_actual, window):
    ANCHO_PANTALLA = 600
    fondo_imagen = pygame.image.load("Parcial_2/img/fondo.png")
    ethnocentric = pygame.font.Font('Parcial_2/fonts/ethnocentric/ethnocentric rg.otf', 70)
    titulo = ethnocentric.render("Invasores", True, (255,255,255))
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if btn_start.rect.x <= mouse_x <= btn_start.rect.x+btn_start.ancho and btn_start.rect.y <= mouse_y <= btn_start.rect.y+btn_start.alto:
                print("pantalla_actual") 
                print("Se hizo click en el boton!")
                pantalla_actual = 2
    
    window.fill((0,0,0))
    window.blit(fondo_imagen, (0,0))
    window.blit(btn_start.imagen, btn_start.rect)
    window.blit(titulo, (ANCHO_PANTALLA/2-titulo.get_width()/2,100))
    pygame.display.flip()
    pygame.display.update()
                

    return pantalla_actual