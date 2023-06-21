import pygame

class Vidas:
    def __init__(self, x, y, ancho, alto):
        #vidas
        self.vidas = pygame.image.load("JUEGO PYGAME\imagenes\\vidas.png")
        self.vidas = pygame.transform.scale(self.vidas,(ancho,alto))
        self.posicion_rect_vidas = (x,y)
        self.rect_vidas = self.vidas.get_rect(midbottom = self.posicion_rect_vidas)
        self.flag_vida = True

    def update(self,screen):
        if self.flag_vida:
            screen.blit(self.vidas, self.rect_vidas)