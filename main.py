import pygame # Se importa la librería pygame.
from configuraciones import *
from juego import *
from imagenes import *
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

# Fuente
# Se crea una fuente predeterminada (None) con tamaño 50, para escribir el texto de los botones.
fuente = pygame.font.SysFont(None, 50)
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# Definir los botones (x, y, ancho, alto)
# Se crea una lista de diccionarios, donde cada uno representa un botón con:
#   -"texto": lo que se va a mostrar.
#   -"rect": un rectángulo de PyGame que define la posición y el tamaño del botón.
botones = [
    {"texto": "Jugar", "rect": pygame.Rect(300, 150, 200, 60)},
    {"texto": "Ranking", "rect": pygame.Rect(300, 230, 200, 60)},
    {"texto": "Créditos", "rect": pygame.Rect(300, 310, 200, 60)},
    {"texto": "Salir", "rect": pygame.Rect(300, 390, 200, 60)}
]

corriendo = True # Variable de control del bucle principal del juego.

def dibujar_menu():

    fondo_menu_img = pygame.image.load("imagenes/fondo.eternauta.ranking2.jpg").convert()
    fondo_menu_img = pygame.transform.scale(fondo_menu_img, (ANCHO_VENTANA, ALTO_VENTANA))

    ventana.blit(fondo_menu_img,(0,0)) # # Pinta el fondo de blanco
    #ventana.blit("imagenes\menu.png", (0, 0))
    for boton in botones:
        pygame.draw.rect(ventana, AZUL, boton["rect"]) # Dibuja un rectángulo azul para cada botón
        texto = fuente.render(boton["texto"], True, BLANCO) # Renderiza el texto del botón en blanco
        texto_rect = texto.get_rect(center=boton["rect"].center) # Obtiene la posición del centro del rectángulo
        ventana.blit(texto, texto_rect) # Dibuja el texto en la ventana
    pygame.display.update() # Actualiza la ventana

while corriendo:
    dibujar_menu() # Llama a la función para dibujar el menú del juego

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False # Si el usuario cierra la ventana, se termina el bucle.

        if evento.type == pygame.MOUSEBUTTONDOWN: # Si se presiona el mouse
            pos = pygame.mouse.get_pos() # Obtiene la posición del mouse donde se hizo clic
            print(pos)
            for boton in botones:
                if boton["rect"].collidepoint(pos): # Si el clic fue dentro del rectángulo del botón
                    print("Clic en:", boton["texto"])
                    if boton["texto"] == "Jugar":
                        print("Iniciando el juego...")
                        iniciar_juego()
                        # Acá podemos llamar a la función de juego
                    elif boton["texto"] == "Ranking":
                        print("Mostrando el ranking...")
                        # Acá podemos llamar a la función de ranking
                    elif boton["texto"] == "Créditos":
                        print("Mostrando los créditos...")
                        # Acá podemos llamar a la función de créditos
                    elif boton["texto"] == "Salir":
                        corriendo = False
            

pygame.quit() # Se cierra correctamente PyGame liberando l