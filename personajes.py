import pygame


class Jugador:
    ruta_icono_nave = '/Users/oscar/Desktop/GitHub/space_invaders/iconos/nave.png'
    icono_jugador = pygame.image.load(ruta_icono_nave)

    def colocar_jugador(self, ventana, posicion_x, posicion_y):
        ventana.blit(self.icono_jugador, (posicion_x, posicion_y))


class EnemigoNave1:
    ruta_icono_nave = '/Users/oscar/Desktop/GitHub/space_invaders/iconos/nave_enemiga.png'
    icono_enemigo = pygame.image.load(ruta_icono_nave)

    def colocar_enemigo(self, ventana, posicion_x, posicion_y):
        ventana.blit(self.icono_enemigo, (posicion_x, posicion_y))


class EnemigoNave2:
    ruta_icono_nave = '/Users/oscar/Desktop/GitHub/space_invaders/iconos/nave_enemiga_2.png'
    icono_enemigo = pygame.image.load(ruta_icono_nave)

    def colocar_enemigo(self, ventana, posicion_x, posicion_y):
        ventana.blit(self.icono_enemigo, (posicion_x, posicion_y))

class EnemigoNave3:
    ruta_icono_nave = '/Users/oscar/Desktop/GitHub/space_invaders/iconos/nave_enemiga_3.png'
    icono_enemigo = pygame.image.load(ruta_icono_nave)

    def colocar_enemigo(self, ventana, posicion_x, posicion_y):
        ventana.blit(self.icono_enemigo, (posicion_x, posicion_y))

class Bala:
    ruta_icono_bala = '/Users/oscar/Desktop/GitHub/space_invaders/iconos/bala.png'
    icono_bala = pygame.image.load(ruta_icono_bala)

    def colocar_bala(self, ventana, posicion_x, posicion_y):
        ventana.blit(self.icono_bala, (posicion_x, posicion_y))

    def disparar_bala(self, ventana, x, y):
        ventana.blit(self.icono_bala, (x, y+5))