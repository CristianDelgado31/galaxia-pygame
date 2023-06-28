import pygame
import random
#from main_copia_original import sonido_disparo
from dimensiones_ventana import *
from clase_disparo_nave_enemiga import *



class NaveEnemiga:
    def __init__(self,x, y, ancho, alto):
        self.image_nave_enemiga = pygame.image.load("imagenes\\naveEnemigaa.png")
        self.image_nave_enemiga = pygame.transform.scale(self.image_nave_enemiga,(ancho,alto))
        self.rect_imagen_enemiga = self.image_nave_enemiga.get_rect()
        self.rect_imagen_enemiga.y = y
        self.rect_imagen_enemiga.x = x
        self.flag_nave_enemiga = True
        self.posicion_orientacion = 5
        
    def update_enemigo(self, screen):
        if self.flag_nave_enemiga:
            self.mostrar_naves_enemigas(screen)
            self.mover_nave_enemiga()
            self.disparo()

        elif not self.flag_nave_enemiga:
            self.rect_imagen_enemiga.y = -1000
            self.rect_imagen_enemiga.x = -1000
            self.mostrar_naves_enemigas(screen)
             

    def mostrar_naves_enemigas(self, screen):
        #pygame.draw.rect(screen,(COLOR_BLANCO),self.rect_imagen_enemiga)
        screen.blit(self.image_nave_enemiga,self.rect_imagen_enemiga)


    def mover_nave_enemiga(self):#LIMITE DE LA NAVE ENEMIGA
        self.rect_imagen_enemiga.y += self.posicion_orientacion
        if self.rect_imagen_enemiga.y >= ALTO_VENTANA:
            self.rect_imagen_enemiga.y = random.randrange(800) * -1
            self.rect_imagen_enemiga.x = random.randrange(30, 700)

    def disparo(self):
        x = self.rect_imagen_enemiga.centerx  # Obtiene la posición "x" de la nave
        y = self.rect_imagen_enemiga.top  # Obtiene la posición "y" de la nave
        if random.randrange(0,200) == 11 and self.rect_imagen_enemiga.y >= 0:
            disparo_enemigo = DisparoEnemigo(x, y)  # Crea una instancia de Disparo en la posición de la nave
            lista_balas_enemigas.append(disparo_enemigo)  # Agrega el disparo a la lista
            self.sonido_disparo = pygame.mixer.Sound("sonidos\SpaceLaserShot.wav")
            self.sonido_disparo.set_volume(0.2)
            self.sonido_disparo.play()

