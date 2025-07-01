from imagenes import *
from Configuraciones import *
import sys
import pygame  
ANCHO_VENTANA = 700
ALTO_VENTANA = 600
titulo = ""
lista_titulos = []
contador = 0 
#PALETA DE COLORES
NEGRO = (0, 0, 0)
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_GRIS = (128,128,128)
COLOR_AMARILLO = (255 ,255,0)
COLOR_CELESTE = (0,0,128)
COLOR_AZUL = (0,0,255)
VALOR_BORDER_RADIUS = 20
DELAY_CLIC = 500  # 500 milisegundos de retraso entre clics

#CONFIGURAR IMAGENES
pygame.init()
imagen = pygame.image.load("TP-Programacion-Pygame\imagenes\image fondo (2).png")
imagen = pygame.transform.scale(imagen,(ANCHO_VENTANA,ALTO_VENTANA))

#CREAR UNA FUENTE 
fuente = pygame.font.SysFont("Arial", 30)
texto_titulo = fuente.render(str(titulo), True, NEGRO)

#CREAR PANTALLA 
pantalla = pygame.display.set_mode((ANCHO_VENTANA , ALTO_VENTANA))
pygame.display.set_caption("EL ETERNAUTA")

"--------------------------------------------------------------------------------------------------------------------------------------------"

pantalla_actual = "menu"

def mostrar_menu():
    reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    pantalla.blit(imagen, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton_salir.collidepoint(evento.pos):
                print("Botón Salir presionado.")
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print (evento.pos)
                poscicion_click = list(evento.pos)
                if ((poscicion_click[0]>300 and poscicion_click[0]<500) and (poscicion_click[1]>20 and poscicion_click[1]<120)):
                    titulo = lista_titulos[contador]
                    texto_titulo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccionado = (seleccionado - 1) % 3
                elif evento.key == pygame.K_DOWN:
                    seleccionado = (seleccionado + 1) % 3
                elif evento.key == pygame.K_RETURN:
                    if seleccionado == 0:
                        print(">> Jugar seleccionado")
                        # iniciar_juego()
                    elif seleccionado == 1:
                        print(">> Opciones seleccionadas")
                        # mostrar_opciones()
                    elif seleccionado == 2:
                        pygame.quit()
                        sys.exit()
            
            #pantalla.fill((30, 30, 30))  # Limpiar pantalla
        funcion_generar_boton("Iniciar", pos_boton, pantalla)
        funcion_generar_boton("Opciones", pos_boton_2, pantalla)
        dibujar_boton_salir(pantalla, rect_boton_salir, "Salir")

        # Dibujar el fondo
        pygame.display.flip()
        #reloj.tick(60)

# Ejecutar el menú
mostrar_menu()



pygame.quit()
