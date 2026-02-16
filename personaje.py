import pygame
import constantes



class Personaje():
    def __init__(self, x , y, animaciones, energia):
        self.score = 0
        self.energia = energia
        self.vivo = True
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.shape = self.image.get_rect()#(pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE))


        self.shape.center = (x,y)

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False


        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

    def update (self):
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0


    def dibujar(self, ventana):
        imagen_flip = pygame.transform.flip(self.image, self.flip , False)
        ventana.blit(imagen_flip, self.shape.topleft)

        #pygame.draw.rect(ventana, constantes.COLOR_PERSONAJE, self.shape, 1)