#------------------------------------------Ranking JSON-------------------------------------------------------------
import pygame
import os
import json

ANCHO_VENTANA = 800 # Ancho de la ventana del juego.
ALTO_VENTANA = 600 # Alto de la ventana del juego. # Crea una ventana de 800 píxeles de ancho y 600 de alto.
BLANCO = (255, 255, 255)
ARCHIVO_RANKING = "ranking.json"

def guardar_puntaje(nombre, puntaje):
    """
    guarda nombre y puntaje
    args:
        str: nombre del usuario
        int: guarda entero en archivo .jason
    returns:    
        list
    """
    if not os.path.exists(ARCHIVO_RANKING):
        with open(ARCHIVO_RANKING, "w") as archivo:
            json.dump([], archivo)

    ranking = []
    if os.path.getsize(ARCHIVO_RANKING) > 0:
        with open(ARCHIVO_RANKING, "r") as archivo:
            ranking = json.load(archivo)

    ranking.append({"nombre": nombre, "puntaje": puntaje})

    with open(ARCHIVO_RANKING, "w") as archivo:
        json.dump(ranking, archivo, indent=4)
ARCHIVO_RANKING = "ranking.json"

def ordenar_ranking():
    """
    ordena matriz  
    args:
        archivo .json
    retuns:
        (list)
    """
    if not os.path.exists(ARCHIVO_RANKING) or os.path.getsize(ARCHIVO_RANKING) == 0:
        return []

    with open(ARCHIVO_RANKING, "r") as archivo:
        ranking = json.load(archivo)

    for i in range(len(ranking)):
        for j in range(0, len(ranking) - i - 1):
            if ranking[j]["puntaje"] < ranking[j + 1]["puntaje"]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    return ranking

def mostrar_ranking(pantalla):
    """
    recibe imagen para usar de fondo de pantalla
    args:
        pantalla
    return:
        fondo de pantalla con imagen recibida
    """
    fondo_ranking_img = pygame.image.load("imagenes/eternauta8.jpg").convert()
    fondo_ranking_img = pygame.transform.scale(fondo_ranking_img, (ANCHO_VENTANA, ALTO_VENTANA))

    pantalla.blit(fondo_ranking_img, (0, 0))

    ranking = ordenar_ranking()
    fuente_chica = pygame.font.SysFont("Courier New", 40)

    i = 0
    for jugador in ranking[:5]:
        texto = fuente_chica.render(f"{i+1}. {jugador['nombre']} - {jugador['puntaje']}", True, BLANCO)
        pantalla.blit(texto, (ANCHO_VENTANA // 2 - 150, 100 + i * 40))
        i += 1
    pygame.display.flip()
    pygame.time.wait(5000)  
