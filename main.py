import pygame
import constantes
from personaje import Personaje
from weapon import Weapon
from textos import DamageText
from itmes import Item
import  os


def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_image = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_image


#contar elementos
def contar_elemento(directorio):
    return len(os.listdir(directorio))

#lista nombre de elementos
def nombres_carpetas(directorio):
    return os.listdir(directorio)

pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
pygame.display.set_caption("primer juego")


font = pygame.font.Font("assets//fonts//Mago.ttf", 25)
#font = pygame.font.Font(None, 25)

#energia
corazon_vacio = pygame.image.load("assets//images//items//corazon3.PNG").convert_alpha()
corazon_vacio = escalar_img(corazon_vacio, constantes.SCALA_CORAZONES)
corazon_mitad = pygame.image.load("assets//images//items//corazon2.PNG").convert_alpha()
corazon_mitad = escalar_img(corazon_mitad, constantes.SCALA_CORAZONES)
corazon_lleno = pygame.image.load("assets//images//items//corazon1.PNG").convert_alpha()
corazon_lleno = escalar_img(corazon_lleno, constantes.SCALA_CORAZONES)

#importar imagenes
animaciones = [ ]
for i in range (7):
    img = pygame.image.load(f"assets//images//characters//player//Player_{i}.png").convert_alpha()
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)


#enemigos
directorio_enemigos = "assets//images//characters//enemies//"
tipo_enemigo = nombres_carpetas(directorio_enemigos)
animacion_enemigos = []
for eni in tipo_enemigo:
    lista_temp = []
    ruta_temp = f"assets//images//characters//enemies//{eni}"
    num_animaciones = contar_elemento(ruta_temp)
    for i in range(num_animaciones):
       img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}_{i+1}.png").convert_alpha()
       img_enemigo = escalar_img(img_enemigo, constantes.SCALA_ENEMIGOS)
       lista_temp.append(img_enemigo)
    animacion_enemigos.append(lista_temp)



imagen_pistola = pygame.image.load(f"assets//images//weapoms//gun.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)

imagen_bala = pygame.image.load(f"assets//images//weapoms//bala.png").convert_alpha()
imagen_bala = escalar_img(imagen_bala, constantes.SCALA_ARMA)

#cagar imagenes
posion_roja = pygame.image.load("assets//images//items//pótion.png").convert_alpha()
posion_roja = escalar_img(posion_roja, 0.06)


""" papa
coin_images = []
ruta_img = "assets//images//items//coins"
num_coin_images = contar_elemento(ruta_img)
for i in range (num_coin_images):
    img = pygame.image.load(f"assets//images//items//coins//moneda_{i+1}.png").convert_alpha()
    img = escalar_img(img, 0.08)
    coin_images.append(img)

def dibujar_texto(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    ventana.blit(img, (x, y))

"""
def vida_jugador():
    c_mitad_dibujado = False
    for i in range(4):
        if jugador.energia >=((i+1)*25):
            ventana.blit(corazon_lleno, (5+i*50, 5))
        elif jugador.energia % 25 > 0 and c_mitad_dibujado == False:
            ventana.blit(corazon_mitad, (5+i*50, 5))
            c_mitad_dibujado == True
        else:
            ventana.blit(corazon_vacio, (5+i*50, 5))



jugador: Personaje = Personaje(50, 50, animaciones, 40)


cazador = Personaje (400, 400, animacion_enemigos[0], 150)


lista_enemigos = []
lista_enemigos.append(cazador)

Pistola = Weapon(imagen_pistola, imagen_bala)

grupo_damage_text = pygame.sprite.Group()

grupos_balas = pygame.sprite.Group()

grupos_items = pygame.sprite.Group()

"""
coin = Item(350, 25, 0, coin_images )
potion = Item(380, 55, 1, [posion_roja])

grupos_items.add(coin)
grupos_items.add(potion)

"""


mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda= False


run = True

reloj = pygame.time.Clock()
while run:

    reloj.tick(constantes.FPS)


    ventana.fill(constantes.COLOR_BG)

    delta_x = 0
    delta_y = 0

    if mover_derecha:
        delta_x = constantes.VELOCIADAD
    if mover_izquierda:
        delta_x = -constantes.VELOCIADAD
    if mover_abajo:
        delta_y = constantes.VELOCIADAD
    if mover_arriba:
        delta_y = -constantes.VELOCIADAD

    jugador.movimiento(delta_x, delta_y)

    jugador.update()


    for ene in lista_enemigos:
        ene.update()

    Bala = Pistola.update(jugador)
    if Bala:
        grupos_balas.add(Bala)
        # dibuja las balas
    for bala in grupos_balas:
        # imprimir posición para depuración
        print(f"Bala {i}: x={bala.rect.centerx}, y={bala.rect.centery}")
        print(f"Jugador: x={jugador.shape.centerx}, y={jugador.shape.centery}, flip={jugador.flip}")
        bala.dibujar(ventana)


    for bala in grupos_balas:
       damage, pos_damage = bala.update(lista_enemigos)
       if damage:
           damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(damage), font, constantes.ROJO)
           grupo_damage_text.add(damage_text)


    grupo_damage_text.update()


    #actualizar items
    grupos_items.update(jugador)



    jugador.dibujar(ventana)

    for ene in lista_enemigos:
        ene.dibujar(ventana)


    Pistola.dibujar(ventana)

    #dibujar la vida

    vida_jugador()


    grupo_damage_text.draw(ventana)
  # papa  dibujar_texto(f"Score: {jugador.score}", font, (255, 255, 0 ), 700, 5)

    #dibujar items
    grupos_items.draw(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False


    pygame.display.update()

pygame.quit()