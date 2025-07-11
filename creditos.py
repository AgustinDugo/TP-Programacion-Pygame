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
    """
    Renderiza en pantalla los créditos del juego de forma vertical.

    Esta función limpia la pantalla, recorre una lista de líneas de texto (los créditos)
    y los dibuja uno debajo del otro, centrados horizontalmente, comenzando desde un
    desplazamiento vertical. Finalmente actualiza la pantalla para mostrar
    los textos renderizados.

    Parámetros:
    - pantalla: superficie de Pygame donde se dibujan los textos.
    - textos: lista de cadenas de texto, cada una representando una línea de los créditos.
    - fuente: objeto pygame.font.Font utilizado para renderizar el texto.
    - offset_y: entero que representa el desplazamiento vertical inicial desde donde
    comienzan a dibujarse las líneas. Esto permite animar el desplazamiento (scroll) de los créditos.
    """
    pantalla.fill(COLOR_NEGRO)
    i = 0
    while i < len(textos):
        linea = textos[i]  # Línea de texto a renderizar
        texto_render = fuente.render(linea, True, COLOR_BLANCO)
        x = ANCHO_VENTANA // 2 - texto_render.get_width() // 2
        y = offset_y + i * 40  # Posición vertical con separación entre líneas
        pantalla.blit(texto_render, (x, y))
        i += 1
    pygame.display.flip()

def mostrar_creditos():
    """
    Esta función:
    - Inicializa Pygame y crea una ventana para mostrar los créditos.
    - Usa una fuente estándar para renderizar el texto.
    - Llama a `crear_textos_creditos()` para obtener las líneas de texto a mostrar.
    - Usa `renderizar_creditos()` para dibujar las líneas con un efecto de scroll hacia arriba.
    - Permite cerrar la pantalla con la tecla ESC o el botón de cerrar ventana.
    - Finaliza automáticamente cuando todos los créditos han salido de la pantalla.
    
    """
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

