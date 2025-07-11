import pygame
import sys
pygame.init()

pantalla = pygame.display.set_mode((640, 480))
color_fondo = (100, 200, 255)
fuente = pygame.font.SysFont("Arial", 30)

pygame.init() # inicializar todos los módulos necesarios de PyGame

ANCHO_VENTANA = 800 # Ancho de la ventana del juego.
ALTO_VENTANA = 600 # Alto de la ventana del juego. # Crea una ventana de 800 píxeles de ancho y 600 de alto.

# Se definen algunos colores comunes usando tuplas RGB para usarlos más adelante en los botones y el fondo.
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 120, 215)
GRIS = (200, 200, 200)
AZUL_CLARO = (100, 180, 255)
ROJO = (250,250,250)
COLOR_CELESTE = (0,0,128)



pygame.display.set_caption("Menú del Juego") # Establece el título de la ventana como "Menú del Juego".