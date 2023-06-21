import pygame
from dimensiones_ventana import *
#from clsae_disparo_nave_principal import disparos
#from main_copia_original import sonido_disparo
from clsae_disparo_nave_principal import Disparo

disparos = []

class Nave:
    def __init__(self):
        self.image = pygame.image.load("JUEGO PYGAME\imagenes\\nave1.png") # Carga la imagen de la nave
        self.image = pygame.transform.scale(self.image,(40,40))
        self.posicion = (ANCHO_VENTANA/2,ALTO_VENTANA)
        self.rect = self.image.get_rect(midbottom = self.posicion)
        #self.rect.center = (400, 770)  # Posición inicial de la nave
        self.velocidad_nave = 5
        self.max_restriccion = ANCHO_VENTANA
        #enfriamiento
        self.flag = True
        self.laser_time = 0
        self.laser_cooldown = 400
        self.collision_detected = False
        self.sonido_explosion = pygame.mixer.Sound("JUEGO PYGAME\sonidos\explosion.mp3")
        self.sonido_explosion.set_volume(0.1)
    

    def update(self, screen):
        # Aquí iría la lógica de movimiento de la nave
        self.interacciones()
        self.restriccion()
        self.recarga()
        self.draw(screen)

    def recarga(self):
        if not self.flag:#Si es False entra
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.flag = True

    def interacciones(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad_nave
        elif teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad_nave

        if teclas[pygame.K_SPACE] and self.flag:
            self.flag = False
            self.laser_time = pygame.time.get_ticks()

            x = self.rect.centerx  # Obtiene la posición "x" de la nave
            y = self.rect.top  # Obtiene la posición "y" de la nave
            disparo = Disparo(x, y)  # Crea una instancia de Disparo en la posición de la nave
            disparos.append(disparo)  # Agrega el disparo a la lista
            #
            self.sonido_explosion.play()

    def draw(self, screen):
        #pygame.draw.rect(screen,(COLOR_AMARILLO),self.rect)
        screen.blit(self.image, self.rect)
        
    def restriccion(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_restriccion:
            self.rect.right = self.max_restriccion
    
