import pygame

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
        teclas (pygame.key.ScancodeWrapper): Resultado de pygame.key.get_pressed(), 
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
    if teclas[pygame.K_UP] and personaje["y"] > 0:
        personaje["y"] -= personaje["vel"]
    if teclas[pygame.K_DOWN] and personaje["y"] + personaje["alto"] < alto_pantalla:
        personaje["y"] += personaje["vel"]
