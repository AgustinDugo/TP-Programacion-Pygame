from configuraciones import *
from ranking import *
from juego import *
from creditos import *

pygame.init() # inicializar todos los módulos necesarios de PyGame


pygame.display.set_caption("Menú del Juego") # Establece el título de la ventana como "Menú del Juego".


fuente = pygame.font.SysFont(None, 50)
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
botones = [
    {"texto": "Jugar", "rect": pygame.Rect(300, 150, 200, 60)},
    {"texto": "Ranking", "rect": pygame.Rect(300, 230, 200, 60)},
    {"texto": "Créditos", "rect": pygame.Rect(300, 310, 200, 60)},
    {"texto": "Salir", "rect": pygame.Rect(300, 390, 200, 60)}
]
def dibujar_menu():
    mouse_pos = pygame.mouse.get_pos()
    fondo_menu_img = pygame.image.load("imagenes/fondo.eternauta.ranking2.jpg").convert()
    fondo_menu_img = pygame.transform.scale(fondo_menu_img, (ANCHO_VENTANA, ALTO_VENTANA))

    ventana.blit(fondo_menu_img,(0,0)) # # Pinta el fondo de blanco
    #ventana.blit("imagenes\menu.png", (0, 0))
    for boton in botones:
        rect = boton["rect"]

        # Si el mouse está sobre el botón, se usa otro color
        if rect.collidepoint(mouse_pos):
            color = AZUL_CLARO
        else:
            color = AZUL

        pygame.draw.rect(ventana, color, rect)

        texto = fuente.render(boton["texto"], True, BLANCO)
        texto_rect = texto.get_rect(center=rect.center)
        ventana.blit(texto, texto_rect)

    pygame.display.update()

def menu(corriendo):
    pygame.mixer.music.load("Sonidos/fondo_menu.mp3")
    pygame.mixer.music.play(-1)
    while corriendo:
        dibujar_menu() # Llama a la función para dibujar el menú del juego

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False # Si el usuario cierra la ventana, se termina el bucle.
                pygame.mixer.music.stop()
            if evento.type == pygame.MOUSEBUTTONDOWN: # Si se presiona el mouse
                pos = pygame.mouse.get_pos() # Obtiene la posición del mouse donde se hizo clic
                
                for boton in botones:
                    if boton["rect"].collidepoint(pos): # Si el clic fue dentro del rectángulo del botón
                        print("Clic en:", boton["texto"])
                        if boton["texto"] == "Jugar":
                            iniciar_juego()
                            # Acá podemos llamar a la función de juego
                        elif boton["texto"] == "Ranking":
                            mostrar_ranking(pantalla)
                        elif boton["texto"] == "Créditos":
                            mostrar_creditos()
                            # Acá podemos llamar a la función de créditos
                        elif boton["texto"] == "Salir":
                            corriendo = False
                            pygame.mixer.music.stop()

    pygame.quit() # Se cierra correctamente PyGame liberando l