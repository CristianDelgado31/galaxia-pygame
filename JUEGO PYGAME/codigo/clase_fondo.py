import pygame
#from main_copia_original import ANCHO_VENTANA, ALTO_VENTANA
from dimensiones_ventana import *
from color import *

class Fondo:
    def __init__(self) -> None:
        #Fondo
        #self.screen = screen
        self.imagen_fondo = pygame.image.load("imagenes\\fondo.png")
        self.image = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.rect_fondo = self.imagen_fondo.get_rect()

    def draw(self, screen):
        screen.blit(self.imagen_fondo, self.rect_fondo)


class FondoGameOver(Fondo):
    def __init__(self) -> None:
        super().__init__()
        #imagen game over
        self.image_game_over = pygame.image.load("imagenes\\game_over2.png")#imagen de prueba game over
        self.image_game_over = pygame.transform.scale(self.image_game_over,(500,500))
        self.rect_fondo_game_over = self.image_game_over.get_rect()
        self.rect_fondo_game_over.x = 150
        self.rect_fondo_game_over.y = -100
        #imagen volver a inicio
        self.image_volver_menu = pygame.image.load("imagenes\\volver_al_menu.png")#imagen de prueba game over
        self.image_volver_menu = pygame.transform.scale(self.image_volver_menu,(100,100))
        self.rect_image_volver_menu = self.image_volver_menu.get_rect()
        self.rect_image_volver_menu.x = 360
        self.rect_image_volver_menu.y = 630
        #TEXTOS
        #texto: desear volver?
        self.font_volver_inicio = pygame.font.SysFont(None, 50)
        self.text_volver_inicio = self.font_volver_inicio.render("¿Desea volver al inicio?", True, (BLACK))

    def draw(self, screen):
        screen.blit(self.image_game_over, self.rect_fondo_game_over)
        screen.blit(self.image_volver_menu, self.rect_image_volver_menu)
        #texto
        screen.blit(self.text_volver_inicio, (210, 345))

    
class Menu(Fondo):
    def __init__(self) -> None:
        super().__init__()
        #imagen marco start
        self.imagen_marco_start = pygame.image.load("imagenes\\marco_gamer.png")
        self.imagen_marco_start = pygame.transform.scale(self.imagen_marco_start,(300,100))
        #imagen y rect de marco start
        self.rect_marco_start = self.imagen_marco_start.get_rect()
        self.rect_marco_start.x = 260
        self.rect_marco_start.y = 350
        #imagen y rect de marco ranking
        self.imagen_marco_ranking = pygame.image.load("imagenes\\marco_gamer.png")
        self.imagen_marco_ranking = pygame.transform.scale(self.imagen_marco_ranking,(300,100))
        self.rect_marco_ranking = self.imagen_marco_ranking.get_rect()
        self.rect_marco_ranking.x = 260
        self.rect_marco_ranking.y = 520

        #titulo GALAXIA
        self.font_galaxia = pygame.font.Font(None, 70)
        self.texto_galaxia = self.font_galaxia.render("Galaxia", True, COLOR_BLANCO)
        self.x = 310
        self.y = 100
        #texto START
        self.font_start = pygame.font.SysFont(None, 40)    
        self.text_start = self.font_start.render("Start", True, (COLOR_BLANCO))
        #texto RANKING
        self.font_ranking = pygame.font.SysFont(None, 40)    
        self.texto_ranking = self.font_ranking.render("Ranking", True, (COLOR_BLANCO))
        

    def draw(self, screen):
        screen.blit(self.imagen_fondo, self.rect_fondo)
        #GALAXIA
        screen.blit(self.texto_galaxia, (self.x, self.y))
        #marcos
        screen.blit(self.imagen_marco_start, self.rect_marco_start)
        screen.blit(self.imagen_marco_ranking, self.rect_marco_ranking)
        #start y ranking
        screen.blit(self.text_start, (380, 385))
        screen.blit(self.texto_ranking, (358, 555))
