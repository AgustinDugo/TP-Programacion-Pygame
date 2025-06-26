from imagenes import *
import sys
import pygame  
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
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

flag_correr = True
'''''while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print (evento.pos)
            poscicion_click = list(evento.pos)
            if ((poscicion_click[0]>300 and poscicion_click[0]<500) and (poscicion_click[1]>20 and poscicion_click[1]<120)):
                titulo = lista_titulos[contador]
                texto_titulo

        
    #PINTAMOS EL FONDO DE COLOR 
    pantalla.fill(NEGRO) 
    pygame.draw.rect(pantalla, NEGRO, (300,20,200,100))
    pantalla.blit(texto_titulo,(150,170))
    pantalla.blit(imagen,(1,1))
    pygame.display.flip()
'''''
"--------------------------------------------------------------------------------------------------------------------------------------------"
corriendo = True
pantalla_actual = "menu"

def mostrar_menu():
    seleccionado = 0  # 0 = Jugar, 1 = Opciones, 2 = Salir
    reloj = pygame.time.Clock()

    while corriendo:
        pantalla.blit(imagen, (0, 0))

        # Dibujar botones uno por uno
        color_jugar = COLOR_AZUL if seleccionado == 0 else COLOR_BLANCO
        texto_jugar = fuente.render("Jugar", True, color_jugar)
        rect_jugar = texto_jugar.get_rect(center=(ANCHO_VENTANA // 2, 196))
        pantalla.blit(texto_jugar, rect_jugar)

        color_opciones = COLOR_AZUL if seleccionado == 1 else COLOR_BLANCO
        texto_opciones = fuente.render("Opciones", True, color_opciones)
        rect_opciones = texto_opciones.get_rect(center=(ANCHO_VENTANA // 2, 280))
        pantalla.blit(texto_opciones, rect_opciones)

        color_salir = COLOR_AZUL if seleccionado == 2 else COLOR_BLANCO
        texto_salir = fuente.render("Salir", True, color_salir)
        rect_salir = texto_salir.get_rect(center=(ANCHO_VENTANA // 2, 360))
        pantalla.blit(texto_salir, rect_salir)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
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

            if evento.type == pygame.MOUSEMOTION:
                if rect_jugar.collidepoint(evento.pos):
                    seleccionado = 0
                elif rect_opciones.collidepoint(evento.pos):
                    seleccionado = 1
                elif rect_salir.collidepoint(evento.pos):
                    seleccionado = 2
                    

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if rect_jugar.collidepoint(evento.pos):
                    print(">> Jugar clickeado")
                elif rect_opciones.collidepoint(evento.pos):
                    print(">> Opciones clickeado")
                elif rect_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        reloj.tick(60)

# Ejecutar el menú
mostrar_menu()



pygame.quit()
