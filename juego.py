import pygame
from utils import *
from configuraciones import *

ANCHO_VENTANA = 700
ALTO_VENTANA = 600
NEGRO = (0,0,0,)
ROJO = (250,250,250)
NEGRO = (0, 0, 0)
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_GRIS = (128,128,128)
COLOR_AMARILLO = (255 ,255,0)
COLOR_CELESTE = (0,0,128)
COLOR_AZUL = (0,0,255)





def game_over(pantalla, puntos):
    

    pantalla.fill(NEGRO)
    texto1 = fuente.render("GAME OVER", True, ROJO)
    texto2 = fuente.render("Tu puntaje: " + str(puntos), True, COLOR_CELESTE)
    texto3 = fuente.render("Ingresa tu nombre: ", True, COLOR_CELESTE)

    pantalla.blit(texto1, (ANCHO_VENTANA // 2 - 100, 150))
    pantalla.blit(texto2, (ANCHO_VENTANA // 2 - 100, 220))
    pantalla.blit(texto3, (ANCHO_VENTANA // 2 - 150, 290))
    pygame.display.flip()

    nombre = ""
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre != "":
                    esperando = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < 10 and evento.unicode.isprintable():
                        nombre += evento.unicode

        pantalla.fill(NEGRO)
        pantalla.blit(texto1, (ANCHO_VENTANA // 2 - 100, 150))
        pantalla.blit(texto2, (ANCHO_VENTANA // 2 - 100, 220))
        pantalla.blit(texto3, (ANCHO_VENTANA // 2 - 150, 290))
        texto_nombre = fuente.render(nombre, True, ROJO)
        pantalla.blit(texto_nombre, (ANCHO_VENTANA // 2 - 150 + 200, 290))
        pygame.display.flip()

    #guardar_puntaje(nombre, puntos) funcion para agregar (julian)
    #mostrar_ranking(pantalla) funciones para agregar (julian)

def iniciar_juego():


    ANCHO = 700
    ALTO = 600
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()

    #sonido_colision = pygame.mixer.Sound("recursos/colision.wav")

    personaje = {"x": 325, "y": 500, "vel": 5, "ancho": 50, "alto": 50}
    disparos = []
    enemigos = []
    contador_spawn = 0
    vidas = 3
    puntaje = 0
    jugando = True

    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

        teclas = pygame.key.get_pressed()
        mover_personaje(teclas, personaje, ANCHO, ALTO)
        disparar(teclas, personaje, disparos)
        disparos = mover_disparos(disparos)
        enemigos, contador_spawn = generar_enemigos(enemigos, contador_spawn, ANCHO)
        enemigos = mover_enemigos(enemigos, ALTO)
        disparos, enemigos, puntaje = detectar_colisiones(disparos, enemigos, puntaje)
        enemigos, vidas = detectar_colision_personaje(enemigos, personaje, vidas)

        pantalla.fill((0, 0, 0))
        pygame.draw.rect(pantalla, (255, 0, 0), (personaje["x"], personaje["y"], personaje["ancho"], personaje["alto"]))
        for disparo in disparos:
            pygame.draw.rect(pantalla, (0, 255, 0), (disparo["x"], disparo["y"], disparo["ancho"], disparo["alto"]))
        for enemigo in enemigos:
            pygame.draw.rect(pantalla, (0, 0, 255), (enemigo["x"], enemigo["y"], enemigo["ancho"], enemigo["alto"]))
        
        mostrar_hud(pantalla, fuente, vidas, puntaje)
        
        reloj.tick(60)

        if vidas <= 0:
            jugando = False
            game_over(pantalla, puntaje)
            return #mostrar_menu() Agregar funcion (mateo)
            
        pygame.display.flip()