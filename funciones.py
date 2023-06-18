import objetos

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