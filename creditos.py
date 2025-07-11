import pygame
import sys
from configuraciones import *
ANCHO_VENTANA = 700
ALTO_VENTANA = 600
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

def crear_textos_creditos(fuente):
    return [
        "TRABAJO PRÁCTICO: JUEGO - EL ETERNAUTA",
        "",
        "Desarrollado por:",
        "",
        "Alumno 1: Mateo irizarri",
        "Alumno 2: Julian Fernandez",
        "Alumno 3: Agustin Dugo",
        "",
        "Recursos utilizados:",
        "- Imágenes de El Eternauta adaptadas",
        "- Efectos de sonido de freesound.org / kenney.nl",
        "- Música libre de Mixkit (si corresponde)",
        "",
        "Gracias por jugar :)",
        "",
        "Presione ESC para salir..."
    ]

def renderizar_creditos(pantalla, textos, fuente, offset_y):
    pantalla.fill(COLOR_NEGRO)
    i = 0
    while i < len(textos):
        linea = textos[i]
        texto_render = fuente.render(linea, True, COLOR_BLANCO)
        x = ANCHO_VENTANA // 2 - texto_render.get_width() // 2
        y = offset_y + i * 40
        pantalla.blit(texto_render, (x, y))
        i += 1
    pygame.display.flip()

def mostrar_creditos():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Créditos")
    fuente = pygame.font.SysFont("Arial", 28)
    reloj = pygame.time.Clock()

    textos = crear_textos_creditos(fuente)
    offset_y = ALTO_VENTANA

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False

        offset_y -= 1  # velocidad del scroll
        renderizar_creditos(pantalla, textos, fuente, offset_y)

        if offset_y + len(textos) * 40 < 0:
            corriendo = False

        reloj.tick(60)

