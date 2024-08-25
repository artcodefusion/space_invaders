import pygame
from personajes import Jugador, Bala, EnemigoNave1, EnemigoNave2, EnemigoNave3
from variables import *
import math
from pygame import mixer


pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Invasión Espacial')
fondo = pygame.image.load('fondo_espacio_1.jpg')

jugador = Jugador()
bala = Bala()

# enemigo 1
enemigo_1 = EnemigoNave1()
enemigo_2 = EnemigoNave1()

# enemigo 2
enemigo_3 = EnemigoNave2()
enemigo_4 = EnemigoNave2()

# enemigo 3
enemigo_5 = EnemigoNave3()
enemigo_6 = EnemigoNave3()

lista_enemigos = [enemigo_1, enemigo_2, enemigo_3, enemigo_4, enemigo_5, enemigo_6]

# Posiciones iniciales y velocidades de los enemigos
posicion_x_enemigos = [random.randint(10, 750) for _ in lista_enemigos]
posicion_y_enemigos = [random.randint(10, 300) for _ in lista_enemigos]
delta_x_enemigos = [0.5 for _ in lista_enemigos]  # Velocidad horizontal
delta_y_enemigos = [45 for _ in lista_enemigos]   # Movimiento hacia abajo cuando tocan el borde

def detectar_colision(x1, y1, x2, y2):
    if math.sqrt((y2-y1)**2 + (x2-x1)**2) < 18:
        return True
    else:
        return False

fuente = pygame.font.Font('freesansbold.ttf', 20)
                          
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    window.blit(texto, (x, y))
    
mixer.music.load('musica_fondo.mp3')
mixer.music.play(-1)

# inicializa la posición vertical del fondo
posicion_y_fondo = 0
velocidad_fondo = 0.2 # ajusta la velocidad del fondo

puntaje = 0

while True:
    # actualiza la posición del fondo
    posicion_y_fondo += velocidad_fondo

    # reposiciona el fondo si se ha movido completamente fuera de la pantalla
    if posicion_y_fondo > 600:
        posicion_y_fondo = 0

    # dibuja el fondo dos veces, una encima de la otra
    window.blit(fondo, (0, posicion_y_fondo))
    window.blit(fondo, (0, posicion_y_fondo - 600))

    # EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x_jugador = -0.8

            if event.key == pygame.K_RIGHT:
                delta_x_jugador = 0.8

            if event.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    bala_visible = True
                    posicion_x_bala = posicion_x_jugador
                    bala.disparar_bala(window, posicion_x_bala, posicion_y_bala)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                delta_x_jugador = 0

    # mantener en la pantalla al jugador
    if posicion_x_jugador <= 0:
        posicion_x_jugador = 0
    elif posicion_x_jugador >= 750:
        posicion_x_jugador = 750

    for i in range(len(lista_enemigos)):
        posicion_x_enemigos[i] += delta_x_enemigos[i]
        if posicion_x_enemigos[i] >= 765 or posicion_x_enemigos[i] <= 0:
            delta_x_enemigos[i] = -delta_x_enemigos[i]
            posicion_y_enemigos[i] += delta_y_enemigos[i]


    if posicion_y_bala <= 0:
        posicion_y_bala = 500
        bala_visible = False

    if bala_visible:
        bala.disparar_bala(window, posicion_x_bala, posicion_y_bala)
        posicion_y_bala -= delta_y_bala

    for i in range(len(lista_enemigos)):
        if detectar_colision(posicion_x_bala, posicion_y_bala, posicion_x_enemigos[i], posicion_y_enemigos[i]):
            sonido_colision = mixer.Sound('explosion.mp3')
            sonido_colision.play()
            puntaje += 1
            posicion_x_enemigos[i] = random.randint(10, 750)
            posicion_y_enemigos[i] = random.randint(10, 300)
            posicion_y_bala = 500
            bala_visible = False

    posicion_x_jugador += delta_x_jugador

    jugador.colocar_jugador(window, posicion_x_jugador, posicion_y_jugador)
    for i in range(len(lista_enemigos)):
        lista_enemigos[i].colocar_enemigo(window, posicion_x_enemigos[i], posicion_y_enemigos[i])


    mostrar_puntaje(10, 10)

    pygame.display.update()
