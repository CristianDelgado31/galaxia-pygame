import pygame
from color import *
from clase_naves_enemigas import *
#from main_copia_original import sonido_explosion
#from main_copia_original import score


class Disparo:
    def __init__(self, x, y):
        self.rect_bala = pygame.Rect(x, y, 3, 20)  # Crea un rectángulo para representar el disparo
        self.flag = True
        self.flag_score = False
        self.sonido_explosion = pygame.mixer.Sound("sonidos\explosion.mp3")
        self.sonido_explosion.set_volume(0.1)

    def update(self, screen):
        self.rect_bala.y -= 8  # Mueve el disparo hacia arriba
        #self.verificar_colision()
        self.draw(screen)
        self.restriccion_bala()

    def draw(self, screen):
        if self.flag == True:
            self.draw_bala = pygame.draw.rect(screen, (COLOR_BLANCO), self.rect_bala)  # Dibuja el disparo en pantalla

    def verificar_colision(self, score):
        for nave_enemiga in lista_naves_enemigas:
            if self.rect_bala.colliderect(nave_enemiga.rect_imagen_enemiga):
                self.flag = False
                nave_enemiga.flag_nave_enemiga = self.flag
                self.rect_bala.y = -1000
                self.rect_bala.x = -1000
                if not self.flag_score:
                    score.increase()### FUNCION DEL SCORE (RESUELTO CON BANDERA)
                    self.flag_score = True
                #sonido explosion
                self.sonido_explosion.play()

    def restriccion_bala(self):
        if self.rect_bala.y <= 0:
            self.rect_bala.y = -2000
            self.flag = False


lista_naves_enemigas = []

def crear_naves_enemigas(cantidad):
    for i in range(cantidad):#recomendado 20
        lista_naves_enemigas.append(NaveEnemiga(random.randrange(30,700), random.randrange(2000)*-1, 30, 30))#recomendado 2000 en randrange

cantidad_naves_enemigas = 5
        
crear_naves_enemigas(cantidad_naves_enemigas)