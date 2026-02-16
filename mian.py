import pygame 
import constante

from Personaje import Personaje


jugador = Personaje(50, 50)



pygame.init()


ventana = pygame.display.set_mode((constante.ANCHO_VENTANA, constante.ALTO_VENTANA))

pygame.display.set_caption("puto")

run = True

jugador.dibujar(ventana)

while run:
    for event in pygame.event.get( ):
        if event.type( ) == pygame.QUIT():
            run = False

    pygame.display.update()

pygame.quit()