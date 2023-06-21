import pygame
from color import *

class Ranking:
    def __init__(self) -> None:
        self.image_salir_de_ranking = pygame.image.load("JUEGO PYGAME\imagenes\\retroceder_del_ranking.png")
        self.image_salir_de_ranking = pygame.transform.scale(self.image_salir_de_ranking,(100,100))
        self.rect_image_salir_ranking = self.image_salir_de_ranking.get_rect()
        self.rect_image_salir_ranking.y = -1000
        self.rect_image_salir_ranking.x = 0
        ##puestos ranking
        self.image_puestos_ranking = pygame.image.load("JUEGO PYGAME\imagenes\puestos_rank.png")
        self.image_puestos_ranking = pygame.transform.scale(self.image_puestos_ranking,(600,600))
        self.rect_image_puestos_ranking = self.image_puestos_ranking.get_rect()
        self.rect_image_puestos_ranking.y = 200
        self.rect_image_puestos_ranking.x = 110
        ##textos de puestos en el ranking
        self.font_puestos = pygame.font.SysFont(None, 40)
        #rank 1
        self.nombre_primer_puesto = "Jugador 1"
        self.puntaje_primer_puesto = 0
        #rank 2
        self.nombre_segundo_puesto = "Jugador 2"
        self.puntaje_segundo_puesto = 0
        #trank 3
        self.nombre_tercer_puesto = "Jugador 3"
        self.puntaje_tercer_puesto = 0


    def draw(self, screen):
        screen.blit(self.image_salir_de_ranking, self.rect_image_salir_ranking)
        screen.blit(self.image_puestos_ranking, self.rect_image_puestos_ranking)
        
        #ranking
        #1ro
        self.texto_nombre_puesto = self.font_puestos.render(self.nombre_primer_puesto, True, (COLOR_BLANCO))
        self.texto_puntaje_primer_puesto = self.font_puestos.render(str(self.puntaje_primer_puesto), True, (COLOR_BLANCO))
        screen.blit(self.texto_nombre_puesto, (346, 505))
        screen.blit(self.texto_puntaje_primer_puesto, (368, 550))
        #2do
        self.texto_nombre_puesto_dos = self.font_puestos.render(self.nombre_segundo_puesto, True, (COLOR_BLANCO))
        self.texto_puntaje_segundo_puesto = self.font_puestos.render(str(self.puntaje_segundo_puesto), True, (COLOR_BLANCO))
        screen.blit(self.texto_nombre_puesto_dos, (148, 575))
        screen.blit(self.texto_puntaje_segundo_puesto, (168, 620))
        #3er
        self.texto_nombre_puesto_tres = self.font_puestos.render(self.nombre_tercer_puesto, True, (COLOR_BLANCO))
        self.texto_puntaje_tercer_puesto = self.font_puestos.render(str(self.puntaje_tercer_puesto), True, (COLOR_BLANCO))
        screen.blit(self.texto_nombre_puesto_tres, (548, 575))
        screen.blit(self.texto_puntaje_tercer_puesto, (568, 610))