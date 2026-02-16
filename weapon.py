import pygame
import constantes
import math
import random





class Weapon ():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.disparar = False

    def update(self, personaje):
        bala = None
        self.forma.center = personaje.shape.center
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.shape.width/ 3
            self.rotar_arma(False)
            flip_factor = 1  # normal
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.shape.width / 3
            self.rotar_arma(True)
            flip_factor = -1  # invertir horizontal
        # distancia desde el centro del arma hasta el cañón
        offset_dist = 20  # píxeles, ajusta a tu gusto



           # mouse_pos = pygame.mouse.get_pos()
            #diferencia_x = mouse_pos[0] - self.forma.x
            #diferencia_y = mouse_pos[1] - self.forma.y
            #self.angulo = math.degrees(math.atan2(diferencia_y, diferencia_x))

        #Si presiona el click izq del mouse debe disparar bala
        if pygame.mouse.get_pressed()[0] and self.disparar == False:
            # calcular el desplazamiento según el ángulo
            offset_x = math.cos(math.radians(self.angulo)) * offset_dist * flip_factor
            offset_y = math.sin(math.radians(self.angulo)) * offset_dist
            #bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)

            # Ajustar ángulo de la bala si el personaje está volteado
            bala_angulo = self.angulo if not personaje.flip else 180 - self.angulo
            # crear bala desplazada
            bala = Bullet(
                self.imagen_bala,
                self.forma.centerx + offset_x,
                self.forma.centery + offset_y,
                self.angulo
            )
            self.disparar = True
            return bala
        if pygame.mouse.get_pressed()[0] == False:
            self.disparar = False
            return bala
        """    
        mouse_click = pygame.mouse.get_pressed()[0]
        tiempo_actual = pygame.time.get_ticks()


        if mouse_click and tiempo_actual - self.ultimo_disparo >= self.cooldown:
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.ultimo_disparo = tiempo_actual

        return bala
        """
        #self.forma.y = self.forma.y + 5

    def rotar_arma(self, rotar):
        if rotar == True:
           imagen_base = pygame.transform.flip(self.imagen_original, True, False)
           #      imagen_flip = pygame.transform.flip(self.imagen, True, False)
           #     self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_base = self.imagen_original
        self.imagen = pygame.transform.rotate(imagen_base, self.angulo)
        self.forma = self.imagen.get_rect(center=self.forma.center)

    # else:
        #    imagen_flip = pygame.transform.flip(self.imagen, False, False)
         #   self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        #self.imagen = pygame.transform.rotate(self.imagen,
         #                                     self.angulo)
        interfaz.blit(self.imagen, self.forma)



class Bullet(pygame.sprite.Sprite):
     def __init__(self,image, x, y, angle, escala =0.4):
         pygame.sprite.Sprite.__init__(self)
         #self.imagen_original = image
         self.imagen_original = pygame.transform.scale(
             image,
             (
                 int(image.get_width() * escala),
                 int(image.get_height() * escala)
             )
         )
         self.angulo = angle
         self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
         self.rect = self.image.get_rect()
         self.rect.center = (x, y)
        #calculo de la velocidad de la bala
         velocidad = 10
         self.delta_x = math.cos(math.radians(self.angulo)) * velocidad
         self.delta_y = math.sin(math.radians(self.angulo)) * velocidad


     def update(self, lista_enemigos):
        daño = 0
        pos_daño = None
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y


        if self.rect.x <= 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.right < constantes.ANCHO_VENTANA:
            self.kill()

        for enemigo  in lista_enemigos:
            if enemigo.shape.colliderect(self.rect):
                daño = 15 + random.randint(-7, 7)
                pos_daño = enemigo.shape
                enemigo.energia = enemigo.energia - daño
                self.kill()
                break
        return daño, pos_daño



     def dibujar (self, interfaz, offset_y = 5.5):
        interfaz.blit(self.image, (self.rect.centerx,
                      self.rect.centery - int(self.image.get_height()/2) - offset_y))
