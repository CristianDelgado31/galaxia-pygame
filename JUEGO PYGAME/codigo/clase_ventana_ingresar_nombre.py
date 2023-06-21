import pygame
from color import *
import re

class VentanaIngreseNombre:
    def __init__(self) -> None:
        self.font_input_nombre = pygame.font.SysFont("Arial", 30)
        self.ingreso = ''
        self.ingreso_rect = pygame.Rect(300,300,200,50)
        #self.font_input_surface = self.font_input.render(self.ingreso, True, BLACK)
        #imagen boton play
        self.imagen_boton_play = pygame.image.load("JUEGO PYGAME\imagenes\\boton_play.png")
        self.imagen_boton_play = pygame.transform.scale(self.imagen_boton_play,(100,100))
        self.rect_image_boton_play = self.imagen_boton_play.get_rect()
        self.rect_image_boton_play.y = 500
        self.rect_image_boton_play.x = 350
        #texto Ingrese su nombre
        self.font_titulo_ingrese_nombre = pygame.font.Font(None, 70)
        self.texto_titulo_ingrese_nombre = self.font_titulo_ingrese_nombre.render("Ingrese su nombre", True, COLOR_BLANCO)
        #Guardar Nombre
        self.guardar_nombre = ""
        self.flag_nombre = False

    def draw(self, screen):
        #if self.flag_nombre == False:
        pygame.draw.rect(screen, COLOR_BLANCO, self.ingreso_rect)
        self.font_input_surface = self.font_input_nombre.render(self.ingreso, True, BLACK)
        screen.blit(self.font_input_surface, (self.ingreso_rect.x + 5, self.ingreso_rect.y + 5))
        screen.blit(self.imagen_boton_play, self.rect_image_boton_play)
        screen.blit(self.texto_titulo_ingrese_nombre, (200, 100))
    
    def verificar_nombre(self):
        if re.match('^([a-zA-Z]+)$', self.ingreso):
            self.flag_nombre = True
            self.guardar_nombre = self.ingreso
        else:
            self.flag_nombre = False

    def update(self, screen):
        self.draw(screen)
        self.verificar_nombre()