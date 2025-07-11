import pygame
import random

def cargar_imagen(path, ancho=None, alto=None):
    """
    Carga una imagen desde un archivo y opcionalmente la escala a un tamaño específico.

    Args:
        path (str): Ruta al archivo de imagen.
        ancho (int, opcional): Nuevo ancho de la imagen. Si no se especifica, 
        se mantiene el original.
        alto (int, opcional): Nuevo alto de la imagen. 
        Si no se especifica, se mantiene el original.

    Returns:
        pygame.Surface: Superficie de Pygame con la imagen cargada 
        y escalada si corresponde.

    """
    imagen = pygame.image.load(path).convert_alpha()
    if ancho and alto:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return imagen

def mover_personaje(teclas, personaje, ancho_pantalla, alto_pantalla):
    """
    Mueve un personaje en función de las teclas presionadas, 
    dentro de los límites de la pantalla.

    Args:
        teclas: Resultado de pygame.key.get_pressed(), 
        representa el estado de las teclas.
        personaje (dict): Diccionario con los datos del personaje. 
        Debe contener las claves:
            - "x" (int): Posición horizontal del personaje.
            - "y" (int): Posición vertical del personaje.
            - "vel" (int): Velocidad de movimiento (número de píxeles por frame).
            - "ancho" (int): Ancho del personaje.
            - "alto" (int): Alto del personaje.
        ancho_pantalla (int): Ancho total de la pantalla o superficie de juego.
        alto_pantalla (int): Alto total de la pantalla o superficie de juego.

    Returns:
        None: La función modifica directamente las coordenadas del diccionario `personaje`.
    """
    if teclas[pygame.K_LEFT] and personaje["x"] > 0:
        personaje["x"] -= personaje["vel"]
    if teclas[pygame.K_RIGHT] and personaje["x"] + personaje["ancho"] < ancho_pantalla:
        personaje["x"] += personaje["vel"]
    if teclas[pygame.K_UP] and personaje["y"] > 360:
        personaje["y"] -= personaje["vel"]
    if teclas[pygame.K_DOWN] and personaje["y"] + personaje["alto"] < alto_pantalla:
        personaje["y"] += personaje["vel"]


def disparar(personaje: dict[str, int], disparos: list[dict[str, int]]):
    """
    Agrega un nuevo disparo a la lista si se presiona la barra espaciadora.

    Args:
        teclas: Estado actual de las teclas presionadas.
        personaje: Diccionario con la posición y tamaño del personaje.
        disparos: Lista de diccionarios representando los disparos activos.
    """
  
    nuevo_disparo = {
        "x": personaje["x"] + personaje["ancho"] // 2 - 5,
        "y": personaje["y"],
        "ancho": 10,
        "alto": 20,
        "vel": 7
    }
    disparos.append(nuevo_disparo)


def mover_disparos(disparos: list[dict[str, int]]) -> list[dict[str, int]]:
    """
    Mueve los disparos hacia arriba y elimina los que salen de la pantalla.

    Args:
        disparos: Lista de disparos activos.

    Returns:
        Lista actualizada de disparos que aún están en pantalla.
    """
    nuevos_disparos = []
    for disparo in disparos:
        disparo["y"] -= disparo["vel"]
        if disparo["y"] + disparo["alto"] > 0:
            nuevos_disparos.append(disparo)
    return nuevos_disparos



def generar_enemigos(enemigos: list[dict[str, int]], contador_spawn: int, ancho_pantalla: int, velocidad_enemigo: int) -> tuple[list[dict[str, int]], int]:
    """
    Genera un nuevo enemigo cada 60 cuadros.

    Args:
        enemigos: Lista de enemigos actuales.
        contador_spawn: Contador de cuadros desde el último spawn.
        ancho_pantalla: Ancho de la pantalla para posicionar al enemigo.

    Returns:
        Una tupla con la lista de enemigos actualizada y el contador reiniciado o incrementado.
    """
    if contador_spawn >= 60:
        nuevo_enemigo = {
            "x": random.randint(0, ancho_pantalla - 40),
            "y": -40,
            "ancho": 40,
            "alto": 40,
            "vel":velocidad_enemigo
        }
        enemigos.append(nuevo_enemigo)
        contador_spawn = 0
    return enemigos, contador_spawn + 1


def mover_enemigos(enemigos: list, alto_pantalla: int) -> list[dict[str, int]]:
    """
    Mueve a los enemigos hacia abajo y elimina los que salen de la pantalla.

    Args:
        enemigos: Lista de enemigos activos.
        alto_pantalla: Altura de la pantalla.

    Returns:
        Lista de enemigos que aún están en pantalla.
    """
    nuevos_enemigos = []
    for enemigo in enemigos:
        enemigo["y"] += enemigo["vel"]
        if enemigo["y"] < alto_pantalla:
            nuevos_enemigos.append(enemigo)
    return nuevos_enemigos

impacto = pygame.mixer.Sound("Sonidos/impacto.eternauta.mp3")
def detectar_colisiones(disparos: list[dict[str, int]], enemigos: list[dict[str, int]], puntaje: list[dict[str, int]]) -> tuple[list[dict[str, int]], list[dict[str, int]], int]:
    """
    Detecta colisiones entre disparos y enemigos, y actualiza el puntaje.

    Args:
        disparos: Lista de disparos activos.
        enemigos: Lista de enemigos activos.
        puntaje: Puntaje actual.

    Returns:
        Tupla con la lista actualizada de disparos, enemigos y el puntaje.
    """
    nuevos_enemigos = []
    nuevos_disparos = []
    

    for enemigo in enemigos:
        colisiono = False
        for disparo in disparos:
            rect_enemigo = pygame.Rect(enemigo["x"], enemigo["y"], enemigo["ancho"], enemigo["alto"])
            rect_disparo = pygame.Rect(disparo["x"], disparo["y"], disparo["ancho"], disparo["alto"])
            if rect_enemigo.colliderect(rect_disparo):
                colisiono = True
                puntaje += 10
                impacto.play()
                break
        if not colisiono:
            nuevos_enemigos.append(enemigo)

    # Solo guardamos los disparos que no colisionaron
    for disparo in disparos:
        colisiono = False
        for enemigo in enemigos:
            rect_enemigo = pygame.Rect(enemigo["x"], enemigo["y"], enemigo["ancho"], enemigo["alto"])
            rect_disparo = pygame.Rect(disparo["x"], disparo["y"], disparo["ancho"], disparo["alto"])
            if rect_enemigo.colliderect(rect_disparo):
                colisiono = True
                break
        if not colisiono:
            nuevos_disparos.append(disparo)

    return nuevos_disparos, nuevos_enemigos, puntaje

def detectar_colision_personaje(enemigos: list[dict[str, int]], personaje: dict[str, int], vidas: int, sonido_colision) -> tuple[list[dict[str, int]], int]:
    """
    Detecta si un enemigo colisiona con el personaje.

    Args:
        enemigos: Lista de enemigos activos.
        personaje: Diccionario con la posición y tamaño del personaje.
        vidas: Número actual de vidas.
        sonido_colision: Sonido que se reproduce al colisionar.

    Returns:
        Tupla con la lista de enemigos actualizada y las vidas restantes.
    """
    nuevos_enemigos = []
    personaje_rect = pygame.Rect(personaje["x"], personaje["y"], personaje["ancho"], personaje["alto"])

    for enemigo in enemigos:
        rect_enemigo = pygame.Rect(enemigo["x"], enemigo["y"], enemigo["ancho"], enemigo["alto"])
        if personaje_rect.colliderect(rect_enemigo):
            vidas -= 1
            sonido_colision.play()
        else:
            nuevos_enemigos.append(enemigo)

    return nuevos_enemigos, vidas


def mostrar_hud(pantalla, fuente, vidas: int, puntaje: int):
    """
    Muestra el HUD con las vidas y el puntaje en pantalla.

    Args:
        pantalla: Superficie de la pantalla donde se dibuja el HUD.
        fuente: Fuente usada para renderizar el texto.
        vidas: Número de vidas restantes.
        puntaje: Puntaje actual del jugador.
    """
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, (255, 255, 255))
    texto_puntaje = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto_vidas, (10, 10))
    pantalla.blit(texto_puntaje, (10, 40))


def verificar_game_over(vidas: int) -> bool:
    """
    Verifica si el juego ha terminado por quedarse sin vidas.

    Args:
        vidas: Número de vidas actuales.

    Returns:
        True si el jugador no tiene vidas, False en caso contrario.
    """
    return vidas <= 0


def esperar_tecla():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                return