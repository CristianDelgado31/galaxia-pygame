import pygame
from color import *
from clsae_disparo_nave_principal import crear_naves_enemigas

class Score:
    def __init__(self, x, y, font_size=24, color=(COLOR_BLANCO)):
        self.value = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.x = x
        self.y = y
        self.agregar_puntos = 100
        self.acumulador_puntos = 0

    def increase(self):
        self.value += self.agregar_puntos
        #NIVELES
        if self.value == 500:   #NIVEL 2
            crear_naves_enemigas(10)
        if self.value == 1500:  #NIVEL 3
            crear_naves_enemigas(20)
        if self.value == 3500:  #NIVEL 4
            crear_naves_enemigas(30)
        if self.value == 6000:  #NIVEL 5
            crear_naves_enemigas(50)
        self.acumulador_puntos += self.agregar_puntos

    def draw(self, screen):
        text_score = self.font.render("Score: " + str(self.value), True, self.color)
        screen.blit(text_score, (self.x, self.y))
    
        