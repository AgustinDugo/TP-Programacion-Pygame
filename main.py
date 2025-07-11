import pygame # Se importa la librería pygame.
from configuraciones import *
from menu import *
pygame.init() # inicializar todos los módulos necesarios de PyGame

pygame.display.set_caption("Menú del Juego") # Establece el título de la ventana como "Menú del Juego".
#imagen = pygame.image.load("TP-Programacion-Pygame\imagenes\image fondo (2).png")
#imagen = pygame.transform.scale(imagen,(ANCHO_VENTANA,ALTO_VENTANA))
# Colores
# Se definen algunos colores comunes usando tuplas RGB para usarlos más adelante en los botones y el fondo.
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 120, 215)
GRIS = (200, 200, 200)

# Fuente
# Se crea una fuente predeterminada (None) con tamaño 50, para escribir el texto de los botones.
fuente = pygame.font.SysFont(None, 50)
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# Definir los botones (x, y, ancho, alto)
# Se crea una lista de diccionarios, donde cada uno representa un botón con:
#   -"texto": lo que se va a mostrar.
#   -"rect": un rectángulo de PyGame que define la posición y elj tamaño del botón.
corriendo = True
menu(corriendo)
    