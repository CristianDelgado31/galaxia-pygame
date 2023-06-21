import pygame
from color import *
from dimensiones_ventana import *


#Balas enemigas
class DisparoEnemigo:#Puedo mejorarlo si uso herencia // CAMBIARLO DESPUES!!
    def __init__(self, x, y):
        self.rect_bala_enemiga = pygame.Rect(x, y, 3, 20)
        self.flag = True
        #self.flag_colision = True
        
    def update(self, screen):
        if self.flag:
            self.rect_bala_enemiga.y += 8  # Mueve el disparo hacia abajo
        #self.verificar_colision()
        self.draw(screen)
        self.restriccion_bala()

    def draw(self, screen):
        if self.flag:#deja de dibujar las balas si no True
            self.draw_bala = pygame.draw.rect(screen, (COLOR_BLANCO), self.rect_bala_enemiga)  # Dibuja el disparo en pantalla

    def restriccion_bala(self):
        if self.rect_bala_enemiga.y > ALTO_VENTANA:
            self.rect_bala_enemiga.y = -2000
            self.flag = False

         
lista_balas_enemigas = []