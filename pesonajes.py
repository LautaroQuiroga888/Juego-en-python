import pygame
import constante

class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.rect(0, 0, constante.ALTO_PERSONAJE, constante.ANCHO_PERSONAJE)
        self.shape.center = (x, y) 

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constante.COLOR_PERSONAJE, self.shape)      