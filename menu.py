from configuraciones import *
from ranking import *
from juego import *
from creditos import *
pygame.mixer.init()


pygame.display.set_caption("Menú del Juego") # Establece el título de la ventana como "Menú del Juego".
sonido_hover = pygame.mixer.Sound("Sonidos\Imagen_menu_3.wav")
fuente = pygame.font.SysFont(None, 50)
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) 

botones = [
{"texto": "Jugar", "rect": pygame.Rect(300, 200, 200, 50), "hovered": False},
{"texto": "Ranking", "rect": pygame.Rect(300, 270, 200, 50), "hovered": False},
{"texto": "Créditos", "rect": pygame.Rect(300, 340, 200, 50), "hovered": False},
{"texto": "Salir", "rect": pygame.Rect(300, 410, 200, 50), "hovered": False},
]

def dibujar_menu():

    '''Dibuja el menú principal del juego en la ventana de Pygame.

    Esta función realiza las siguientes acciones:
    - Obtiene la posición actual del cursor del mouse.
    - Carga y escala una imagen de fondo para el menú.
    - Dibuja botones en pantalla, cambiando su color si el cursor está sobre ellos.
    - Renderiza el texto de cada botón y lo coloca centrado en cada rectángulo.
    - Actualiza la pantalla para reflejar los cambios.
'''
    mouse_pos = pygame.mouse.get_pos()
    fondo_menu_img = pygame.image.load("imagenes/fondo.eternauta.ranking2.jpg").convert()
    fondo_menu_img = pygame.transform.scale(fondo_menu_img, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana.blit(fondo_menu_img, (0, 0))

    for boton in botones:
        rect = boton["rect"]
        # Verifica si el cursor del mouse está dentro del área del botón
        if rect.collidepoint(mouse_pos):
            color = AZUL_CLARO
            if not boton["hovered"]:
                sonido_hover.play() # Reproduce un sonido para dar feedback al usuario
                boton["hovered"] = True
        else:
            color = AZUL
            boton["hovered"] = False # Reinicia el estado para que el sonido pueda volver a sonar al entrar

        pygame.draw.rect(ventana, color, rect)

        # Renderizar texto y dibujarlo centrado en el rectángulo
        texto_render = fuente.render(boton["texto"], True, BLANCO)
        texto_rect = texto_render.get_rect(center=rect.center)
        ventana.blit(texto_render, texto_rect)

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
                            pygame.mixer.music.load("Sonidos/fondo_menu.mp3")
                            pygame.mixer.music.play(-1)
                        elif boton["texto"] == "Ranking":
                            mostrar_ranking(pantalla)
                        elif boton["texto"] == "Créditos":
                            mostrar_creditos()
                        
                        elif boton["texto"] == "Salir":
                            corriendo = False
                            pygame.mixer.music.stop()

    pygame.quit() # Se cierra correctamente PyGame liberando l