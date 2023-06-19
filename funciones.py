import objetos
import csv

def crear_invasores(cantidad, lista_invasores, velocidad_misil_min, velocidad_misil_max, valor):

    for _ in range(cantidad):
        invasor = objetos.Invasor(70,50,(0,255,0), valor, velocidad_misil_min, velocidad_misil_max)
        lista_invasores.add(invasor)

def temporizador(tiempo: dict):
    tiempo['segundos'] += 1
    if tiempo['segundos']>59:
        tiempo['segundos'] = 0
        tiempo['minutos'] += 1

    return tiempo

def leer_csv(archivo_csv, fuente, window):
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        i = 1
        primer_linea = True

        for linea in lector_csv:
            if primer_linea:
                linea = f"{linea[0].ljust(10)}{linea[1].ljust(15)}{linea[2].ljust(15)}{linea[3].ljust(15)}"
                primer_linea = False
            else:
                linea = f"{linea[0]}{linea[1].rjust(20)}{linea[2].rjust(17)}{linea[3].rjust(21)}"
            linea_render = fuente.render(linea, True, (255,255,255))
            window.blit(linea_render, (10, i*50))
            i+=1

