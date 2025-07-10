import pygame
import sys
pygame.init()
ancho_boton, alto_boton = 200, 50
color_fondo = (100, 200, 255)
fuente = pygame.font.SysFont("Arial", 30)

pygame.init() # inicializar todos los módulos necesarios de PyGame

ANCHO_VENTANA = 800 # Ancho de la ventana del juego.
ALTO_VENTANA = 600 # Alto de la ventana del juego. # Crea una ventana de 800 píxeles de ancho y 600 de alto.
pygame.display.set_caption("Menú del Juego") # Establece el título de la ventana como "Menú del Juego".
#imagen = pygame.image.load("TP-Programacion-Pygame\imagenes\image fondo (2).png")
#imagen = pygame.transform.scale(imagen,(ANCHO_VENTANA,ALTO_VENTANA))
# Colores
# Se definen algunos colores comunes usando tuplas RGB para usarlos más adelante en los botones y el fondo.
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 120, 215)
GRIS = (200, 200, 200)
AZUL_CLARO = (100, 180, 255)
# Fuente
# Se crea una fuente predeterminada (None) con tamaño 50, para escribir el texto de los botones.
pygame.init() # inicializar todos los módulos necesarios de PyGame

ANCHO_VENTANA = 800 # Ancho de la ventana del juego.
ALTO_VENTANA = 600 # Alto de la ventana del juego. # Crea una ventana de 800 píxeles de ancho y 600 de alto.
pygame.display.set_caption("Menú del Juego") # Establece el título de la ventana como "Menú del Juego".



# Colores del archivo Juego.py
ROJO = (250,250,250)
COLOR_CELESTE = (0,0,128)


pantalla = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Botón sin return")

# Posición donde querés colocar el botón
pos_boton = (456, 180)
pos_boton_2 = (445, 288)

# Rect del botón para detectar clics
boton_rect = pygame.Rect(pos_boton[0], pos_boton[1], 200, 50)


