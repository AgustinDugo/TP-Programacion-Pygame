#------------------------------------------Ranking JSON-------------------------------------------------------------
import os
import json

ARCHIVO_RANKING = "ranking.json"

def guardar_puntaje(nombre, puntaje):
    # Si el archivo no existe, lo crea con una lista vacía
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
    if not os.path.exists(ARCHIVO_RANKING) or os.path.getsize(ARCHIVO_RANKING) == 0:
        return []

    with open(ARCHIVO_RANKING, "r") as archivo:
        ranking = json.load(archivo)

    for i in range(len(ranking)):
        for j in range(0, len(ranking) - i - 1):
            if ranking[j]["puntaje"] < ranking[j + 1]["puntaje"]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    return ranking

# def mostrar_ranking(pantalla):
#     pantalla.fill(NEGRO)
#     ranking = leer_ranking()
#     fuente_chica = pygame.font.SysFont("Arial", 24)

#     texto_titulo = fuente.render("Ranking de Puntajes", True, COLOR_AMARILLO)
#     pantalla.blit(texto_titulo, (ANCHO_VENTANA // 2 - 150, 50))

#     for i, jugador in enumerate(ranking[:5]):  # Mostramos solo los 5 mejores
#         texto = fuente_chica.render(f"{i+1}. {jugador['nombre']} - {jugador['puntaje']}", True, COLOR_BLANCO)
#         pantalla.blit(texto, (ANCHO_VENTANA // 2 - 150, 100 + i * 40))

#     pygame.display.flip()
#     pygame.time.wait(5000)  # Esperar 5 segundos antes de salir
