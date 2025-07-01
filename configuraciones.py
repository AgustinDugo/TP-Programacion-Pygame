import pygame
import sys
pygame.init()
ancho_boton, alto_boton = 200, 50
color_fondo = (100, 200, 255)
fuente = pygame.font.SysFont("Arial", 30)
def funcion_generar_boton(texto, posicion, pantalla):
    """
    Dibuja directamente un botón en la pantalla.

    Parámetros:
        texto (str): Texto que se mostrará en el botón.
        posicion (tuple): Posición (x, y) en la pantalla.
        pantalla (Surface): La superficie donde se dibuja el botón.
    """
    
    color_texto = (0, 0, 0)

    # Crear superficie del botón
    boton_surface = pygame.Surface((ancho_boton, alto_boton))
    boton_surface.fill(color_fondo)

    # Renderizar texto
    texto_render = fuente.render(texto, True, color_texto)
    texto_rect = texto_render.get_rect(center=(ancho_boton // 2, alto_boton // 2))
    boton_surface.blit(texto_render, texto_rect)

    # Dibujar en la pantalla en la posición dada
    pantalla.blit(boton_surface, posicion)

"---------------------------------------------------------------------------------------------------------------------------"
pos_boton = (442, 390)  # (x, y)
rect_boton_salir = pygame.Rect(pos_boton[0], pos_boton[1], ancho_boton, alto_boton)

# Función para dibujar el botón
def dibujar_boton_salir(pantalla, rect_boton, texto):
    color_fondo = (100, 200, 255)
    color_texto = (0, 0, 0)

    # Dibujar rectángulo del botón
    pygame.draw.rect(pantalla, color_fondo, rect_boton)

    # Renderizar texto
    texto_render = fuente.render(texto, True, color_texto)
    texto_rect = texto_render.get_rect(center=rect_boton.center)
    pantalla.blit(texto_render, texto_rect)


pantalla = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Botón sin return")

# Posición donde querés colocar el botón
pos_boton = (456, 180)
pos_boton_2 = (445, 288)

# Rect del botón para detectar clics
boton_rect = pygame.Rect(pos_boton[0], pos_boton[1], 200, 50)
"---------------------------------------------------------------------------------------------------------------------"
def crear_pantalla_con_imagen(ancho, alto):
    """
    Crea una pantalla de Pygame con una imagen de fondo.

    Parámetros:
        imagen_ruta (str): Ruta a la imagen (ej: "fondo.jpg").
        ancho (int): Ancho de la pantalla.
        alto (int): Alto de la pantalla.

    Retorna:
        Surface: la pantalla creada.
    """
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Pantalla con imagen")

    # Cargar y escalar imagen al tamaño de la pantalla
    #imagen = pygame.image.load(imagen_ruta)
    #imagen = pygame.transform.scale(imagen, (ancho, alto))

    pantalla.blit(pantalla, (0, 0))
    pygame.display.flip()

    return pantalla  # Se devuelve por si querés usarla luego en tu código
