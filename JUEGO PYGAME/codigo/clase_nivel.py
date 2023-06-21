import pygame
from color import *

class Nivel:
    def __init__(self, x, y, font_size=24, color=(COLOR_BLANCO)) -> None:
        self.font = pygame.font.Font(None,font_size )
        self.x = x
        self.y = y
        self.color = color
        self.nivel = 1

    def draw(self, screen):
        texto_nivel = self.font.render("Nivel: " + str(self.nivel), True, self.color)
        screen.blit(texto_nivel, (self.x, self.y))

    def actualizar_nivel(self, score):
        if score.value >= 500 and score.value < 1500:
            self.nivel = 2
        if score.value >= 1500 and score.value < 3500:#ERROR EN EL NIVEL 2 
            self.nivel = 3
        if score.value >= 3500 and score.value < 6000:
            self.nivel = 4
        if score.value >= 6000:
            self.nivel = 5