import pygame
from utils import *
from configuraciones import *
from ranking import *
from imagenes import *




def game_over(pantalla, puntos):

    fondo_gameover_img = pygame.image.load("imagenes/fondo.eternauta.gameover.jpg").convert()
    fondo_gameover_img = pygame.transform.scale(fondo_gameover_img, (ANCHO_VENTANA, ALTO_VENTANA))


    
    pantalla.blit(fondo_gameover_img, (0, 0))
    
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

        pantalla.blit(fondo_gameover_img, (0, 0))

        pantalla.blit(texto1, (ANCHO_VENTANA // 2 - 100, 150))
        pantalla.blit(texto2, (ANCHO_VENTANA // 2 - 100, 220))
        pantalla.blit(texto3, (ANCHO_VENTANA // 2 - 150, 290))
        texto_nombre = fuente.render(nombre, True, ROJO)
        pantalla.blit(texto_nombre, (ANCHO_VENTANA // 2 - 150 + 200, 290))
        pygame.display.flip()

    guardar_puntaje(nombre, puntos) 
    mostrar_ranking(pantalla) 

def iniciar_juego():

    ANCHO = 700
    ALTO = 600
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    velocidad_enemigo = 3
    marcador_dificultad = 0  # contador para subir la dificultad

    #sonido_colision = pygame.mixer.Sound("recursos/colision.wav")

    personaje = {"x": 325, "y": 500, "vel": 5, "ancho": 50, "alto": 50}

    personaje_img = pygame.image.load("imagenes/personaje.eternauta.png").convert_alpha()
    personaje_img = pygame.transform.scale(personaje_img, (personaje["ancho"], personaje["alto"]))

    enemigo_img = pygame.image.load("imagenes/enemigo.eternauta.png").convert_alpha()
    enemigo_img = pygame.transform.scale(enemigo_img, (50, 50))

    disparo_img = pygame.image.load("imagenes/disparos.eternauta.png").convert_alpha()
    disparo_img = pygame.transform.scale(disparo_img, (20, 30))

    fondo_img = pygame.image.load("imagenes/fondo.eternauta.webp").convert()
    fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

    sonido = pygame.mixer.Sound("Sonidos/Disparo.eternauta.mp3")

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
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                disparar(personaje, disparos)
                sonido.play()
        teclas = pygame.key.get_pressed()
        mover_personaje(teclas, personaje, ANCHO, ALTO)
        disparos = mover_disparos(disparos)
        enemigos, contador_spawn = generar_enemigos(enemigos, contador_spawn, ANCHO, velocidad_enemigo)
        enemigos = mover_enemigos(enemigos, ALTO)
        disparos, enemigos, puntaje = detectar_colisiones(disparos, enemigos, puntaje)
        enemigos, vidas = detectar_colision_personaje(enemigos, personaje, vidas)

        # pantalla.fill((0, 0, 0))
        pantalla.blit(fondo_img, (0, 0))

        # pygame.draw.rect(pantalla, (255, 0, 0), (personaje["x"], personaje["y"], personaje["ancho"], personaje["alto"]))
        pantalla.blit(personaje_img, (personaje["x"], personaje["y"]))

        for disparo in disparos:
            # pygame.draw.rect(pantalla, (0, 255, 0), (disparo["x"], disparo["y"], disparo["ancho"], disparo["alto"]))
            pantalla.blit(disparo_img, (disparo["x"], disparo["y"]))
        for enemigo in enemigos:
            # pygame.draw.rect(pantalla, (0, 0, 255), (enemigo["x"], enemigo["y"], enemigo["ancho"], enemigo["alto"]))
            pantalla.blit(enemigo_img, (enemigo["x"], enemigo["y"]))
        
        mostrar_hud(pantalla, fuente, vidas, puntaje)
        
        reloj.tick(60)

        if verificar_game_over(vidas):
            jugando = False
            game_over(pantalla, puntaje)
        
        marcador_dificultad += 1
        if marcador_dificultad % (60 * 30) == 0:  # cada 30 segundos (60 FPS * 30)
            if velocidad_enemigo < 15:  # límite para no volverlo injugable
                velocidad_enemigo += 1
                print(f"Dificultad aumentada: velocidad enemigos = {velocidad_enemigo}")

            
        pygame.display.flip()

