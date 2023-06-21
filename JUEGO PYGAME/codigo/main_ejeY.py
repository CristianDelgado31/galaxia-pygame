import pygame, sys
from pygame.locals import *
from color import *
import random
import re
from base_de_datos import *


ANCHO_VENTANA = 800
ALTO_VENTANA = 800


############################# VENTANAS DEL JUEGO ###########################################
class Fondo:
    def __init__(self) -> None:
        #Fondo
        self.imagen_fondo = pygame.image.load("imagenes\\fondo.png")
        self.image = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.rect_fondo = self.imagen_fondo.get_rect()

    def draw(self):
        screen.blit(self.imagen_fondo, self.rect_fondo)


class FondoGameOver(Fondo):
    def __init__(self) -> None:
        super().__init__()
        #imagen calavera
        """self.imagen_fondo = pygame.image.load("imagenes\\calavera.png")#imagen de prueba
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(400,400))
        self.rect_fondo = self.imagen_fondo.get_rect()
        self.rect_fondo.x = 200
        self.rect_fondo.y = 50"""
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

    def draw(self):
        screen.blit(self.image_game_over, self.rect_fondo_game_over)
        screen.blit(self.image_volver_menu, self.rect_image_volver_menu)
        #screen.blit(self.imagen_fondo, self.rect_fondo)
        #texto
        screen.blit(self.text_volver_inicio, (210, 345))

class Menu(Fondo):
    def __init__(self) -> None:
        super().__init__()
        #imagen marco start
        self.imagen_marco_start = pygame.image.load("imagenes\\marco_gamer.png")
        self.imagen_marco_start = pygame.transform.scale(self.imagen_marco_start,(300,100))
        #self.imagen_marco = pygame.transform.rotate(self.imagen_marco, 1)
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
        

    def draw(self):
        screen.blit(self.imagen_fondo, self.rect_fondo)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect_start)
        #GALAXIA
        screen.blit(self.texto_galaxia, (self.x, self.y))
        #marcos
        screen.blit(self.imagen_marco_start, self.rect_marco_start)
        screen.blit(self.imagen_marco_ranking, self.rect_marco_ranking)
        #start y ranking
        screen.blit(self.text_start, (380, 385))
        screen.blit(self.texto_ranking, (358, 555))


class Ranking:
    def __init__(self) -> None:
        self.image_salir_de_ranking = pygame.image.load("imagenes\\retroceder_del_ranking.png")
        self.image_salir_de_ranking = pygame.transform.scale(self.image_salir_de_ranking,(100,100))
        self.rect_image_salir_ranking = self.image_salir_de_ranking.get_rect()
        self.rect_image_salir_ranking.y = -1000
        self.rect_image_salir_ranking.x = 0
        ##puestos ranking
        self.image_puestos_ranking = pygame.image.load("imagenes\puestos_rank.png")
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


    def draw(self):
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




class VentanaIngreseNombre:
    def __init__(self) -> None:
        self.font_input_nombre = pygame.font.SysFont("Arial", 30)
        self.ingreso = ''
        self.ingreso_rect = pygame.Rect(300,300,200,50)
        #self.font_input_surface = self.font_input.render(self.ingreso, True, BLACK)
        #imagen boton play
        self.imagen_boton_play = pygame.image.load("imagenes\\boton_play.png")
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

    def draw(self):
        #if self.flag_nombre == False:
        pygame.draw.rect(screen, COLOR_BLANCO, self.ingreso_rect)
        self.font_input_surface = self.font_input_nombre.render(self.ingreso, True, BLACK)
        screen.blit(self.font_input_surface, (self.ingreso_rect.x + 5, self.ingreso_rect.y + 5))
        screen.blit(self.imagen_boton_play, self.rect_image_boton_play)
        screen.blit(self.texto_titulo_ingrese_nombre, (200, 100))
    
    def verificar_nombre(self):
        if re.match('^([a-zA-Z]{4,12})$', self.ingreso):
            self.flag_nombre = True
            self.guardar_nombre = self.ingreso

    def update(self):
        self.draw()
        self.verificar_nombre()
        

########################################################################################################################################################
########################################################################################################################################################

class Nave:
    def __init__(self):
        self.image = pygame.image.load("imagenes\\nave1.png") # Carga la imagen de la nave
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
    

    def update(self):
        # Aquí iría la lógica de movimiento de la nave
        self.interacciones()
        self.restriccion()
        self.recarga()
        self.draw()

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
            sonido_disparo.play()

    def draw(self):
        #pygame.draw.rect(screen,(COLOR_AMARILLO),self.rect)
        screen.blit(self.image, self.rect)
        
    def restriccion(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_restriccion:
            self.rect.right = self.max_restriccion
    

########################################################################################################################################################
########################################################################################################################################################

class Vidas:
    def __init__(self, x, y, ancho, alto):
        #vidas
        self.vidas = pygame.image.load("imagenes\\vidas.png")
        self.vidas = pygame.transform.scale(self.vidas,(ancho,alto))
        self.posicion_rect_vidas = (x,y)
        self.rect_vidas = self.vidas.get_rect(midbottom = self.posicion_rect_vidas)
        self.flag_vida = True

    def update(self):
        if self.flag_vida:
            screen.blit(self.vidas, self.rect_vidas)


lista_vidas = []
i = 0
#Crear vidas
for vidas in range(3):
    lista_vidas.append(Vidas(20+i, 800, 30, 30))
    i+=30

#
def iterar_lista_vidas(posicion):
    for vida in range(len(lista_vidas)):
        if vida == posicion:
            lista_vidas[vida].flag_vida = False


def actualizar_vidas(numero):
    if numero == 3:
        lista_vidas[2].flag_vida = False
    elif numero == 2:
        lista_vidas[1].flag_vida = False
    elif numero == 1:
        lista_vidas[0].flag_vida = False
        game_over()

def game_over():
    print("PERDISTE")

########################################################################################################################################################
########################################################################################################################################################

class Disparo:
    def __init__(self, x, y):
        self.rect_bala = pygame.Rect(x, y, 3, 20)  # Crea un rectángulo para representar el disparo
        self.flag = True
        self.flag_score = False

    def update(self):
        self.rect_bala.y -= 8  # Mueve el disparo hacia arriba
        self.verificar_colision()
        self.draw()
        self.restriccion_bala()

    def draw(self):
        if self.flag == True:
            self.draw_bala = pygame.draw.rect(screen, (COLOR_BLANCO), self.rect_bala)  # Dibuja el disparo en pantalla

    def verificar_colision(self):
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
                sonido_explosion.play()

    def restriccion_bala(self):
        if self.rect_bala.y <= 0:
            self.rect_bala.y = -2000
            self.flag = False

disparos = []
########################################################################################################################################################
########################################################################################################################################################

#Nave enemiga
class NaveEnemiga:
    def __init__(self,x, y, ancho, alto):
        self.image_nave_enemiga = pygame.image.load("imagenes\\naveEnemigaa.png")
        self.image_nave_enemiga = pygame.transform.scale(self.image_nave_enemiga,(ancho,alto))
        self.rect_imagen_enemiga = self.image_nave_enemiga.get_rect()
        self.rect_imagen_enemiga.y = y
        self.rect_imagen_enemiga.x = x
        self.flag_nave_enemiga = True
        self.posicion_orientacion = 5 #recomendado 5
        
    def update_enemigo(self):
        if self.flag_nave_enemiga:
            self.mostrar_naves_enemigas()
            self.mover_nave_enemiga()
            self.disparo()

        elif not self.flag_nave_enemiga:
            self.rect_imagen_enemiga.y = -1000
            self.rect_imagen_enemiga.x = -1000
            self.mostrar_naves_enemigas()
             

    def mostrar_naves_enemigas(self):
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
            sonido_disparo.play()


lista_naves_enemigas = []

def crear_naves_enemigas(cantidad):
    for i in range(cantidad):#recomendado 20
        lista_naves_enemigas.append(NaveEnemiga(random.randrange(30,700), random.randrange(2000)*-1, 30, 30))#recomendado 2000 en randrange
        

cantidad_naves_enemigas = 5
crear_naves_enemigas(cantidad_naves_enemigas)


########################################################################################################################################################
########################################################################################################################################################

#Balas enemigas
class DisparoEnemigo:#Puedo mejorarlo si uso herencia // CAMBIARLO DESPUES!!
    def __init__(self, x, y):
        self.rect_bala_enemiga = pygame.Rect(x, y, 3, 20)
        self.flag = True
        #self.flag_colision = True
        
    def update(self):
        if self.flag:
            self.rect_bala_enemiga.y += 8  # Mueve el disparo hacia abajo
        #self.verificar_colision()
        self.draw()
        self.restriccion_bala()

    def draw(self):
        if self.flag:#deja de dibujar las balas si no True
            self.draw_bala = pygame.draw.rect(screen, (COLOR_BLANCO), self.rect_bala_enemiga)  # Dibuja el disparo en pantalla

    def restriccion_bala(self):
        if self.rect_bala_enemiga.y > ALTO_VENTANA:
            self.rect_bala_enemiga.y = -2000
            self.flag = False

    def verificar_colision(self):
        for disparos_enemigos in lista_balas_enemigas:#Capaz puedo ponerlo abajo de todo
            if self.rect_bala_enemiga.colliderect(game.rect):
                self.flag = False
                disparos_enemigos.flag = self.flag
                self.rect_bala_enemiga.y = -1000
                self.rect_bala_enemiga.x = -1000

                ######## OCURRE COLISION Y QUITA UN CORAZON ########
                if lista_vidas[2].flag_vida == True:
                    posicion = 2
                elif lista_vidas[2].flag_vida == False and lista_vidas[1].flag_vida == False:
                    posicion = 0
                elif lista_vidas[1].flag_vida == True:
                    posicion = 1
                iterar_lista_vidas(posicion)

         
lista_balas_enemigas = []

########################################################################################################################################################
########################################################################################################################################################

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
    
        

########################################################################################################################################################
########################################################################################################################################################
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

    def actualizar_nivel(self):
        if score.value >= 500 and score.value < 1500:
            self.nivel = 2
        if score.value >= 1500 and score.value < 3500:#ERROR EN EL NIVEL 2 
            self.nivel = 3
        if score.value >= 3500 and score.value < 6000:
            self.nivel = 4
        if score.value >= 6000:
            self.nivel = 5


########################################################################################################################################################
########################################################################################################################################################

pygame.init()

pygame.mixer.init()
#SONIDOS
musica_fondo = pygame.mixer.Sound("sonidos\music_fondo.mp3")
musica_fondo.play(-1)
musica_fondo.set_volume(0.2)
#
sonido_disparo = pygame.mixer.Sound("sonidos\SpaceLaserShot.wav")
sonido_disparo.set_volume(0.2)
#
sonido_explosion = pygame.mixer.Sound("sonidos\explosion.mp3")
sonido_explosion.set_volume(0.1)

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mejor juego de galaxia")
#TIEMPO
clock = pygame.time.Clock()
#CLASES
fondo = Fondo()
fondo_menu = Menu()
game = Nave()
fondo_game_over = FondoGameOver()
ventana_ingresar_nombre = VentanaIngreseNombre()
ventana_ranking = Ranking()
#SCORE
score = Score(10, 10)
#NIVEL
nivel = Nivel(ANCHO_VENTANA/2,10)

#VIDAS
lives = 4  # Cantidad inicial de vidas
enemigos_colisionados = []  # Lista para almacenar las naves enemigas con las que ha colisionado la nave principal

#BANDERAS PARA DISTINTA UBICACION DEL JUEGO
flag_mostrar_menu = True
flag_no_mostrar_juego = False
flag_fin_juego = False
flag_ranking = False#Borrador
flag_ventana_ingresar_nombre = True

lista_nombre = []
lista_puntajes = []
contador_puestos = 0

#score_jugador
def score_jugador(score):
    print(score)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if fondo_menu.rect_marco_start.collidepoint(mouse_x, mouse_y):
                    if flag_mostrar_menu == True and flag_no_mostrar_juego == False:
                        flag_mostrar_menu = False
                        score.acumulador_puntos = 0#puntos totales de la ultima partida
                        ventana_ingresar_nombre.ingreso = ''
                        #print(score.acumulador_puntos)#verifico si esta en 0 de nuevo

                        #reubico el rect de volver al menu en la ventana game over
                        fondo_game_over.rect_image_volver_menu.y = -1000
                        fondo_menu.rect_marco_ranking.y = -1000
                        ventana_ingresar_nombre.rect_image_boton_play.y = 500


                if fondo_menu.rect_marco_ranking.collidepoint(mouse_x, mouse_y):
                    # Se ha producido una colisión
                    print("Ingreso a ranking")
                    #print(score.acumulador_puntos)#puedo mandar los datos a una base de datos
                    flag_no_mostrar_juego = True
                    flag_mostrar_menu = False
                    flag_ranking = True

                    #desp los devuelvo a su posicion con una colision dentro de ventana ranking
                    fondo_game_over.rect_image_volver_menu.y = -1000
                    fondo_menu.rect_marco_ranking.y = -1000
                    #salir de ranking
                    ventana_ranking.rect_image_salir_ranking.y = 0


                if fondo_game_over.rect_image_volver_menu.collidepoint(mouse_x, mouse_y):
                    flag_mostrar_menu = True
                    flag_no_mostrar_juego = False
                    flag_ranking = False
                    flag_ventana_ingresar_nombre = True
                    #posiciono de nuevo a marco ranking
                    fondo_menu.rect_marco_ranking.y = 520
                    #Buen lugar para guardar los datos creo
                    print("Saliendo de game over e ingresando a menú")
                    print("Datos guardados")
                    print(ventana_ingresar_nombre.ingreso)
                    print(score.acumulador_puntos)
                    
                    insertar_datos(ventana_ingresar_nombre.guardar_nombre, score.acumulador_puntos)

                    mostrar_datos_ranking(lista_nombre, lista_puntajes)
                    #print(lista_puntajes)
                    
                    
                    #print(lista_puntajes)                       
                    #ordena bien los puntajes de mayor a menor
                    if len(lista_puntajes) >= 2:
                        for i in range(len(lista_puntajes)-1):
                            for j in range(i+1, len(lista_puntajes)):
                                if lista_puntajes[i] < lista_puntajes[j]:
                                    aux_puntaje = lista_puntajes[i]
                                    lista_puntajes[i] = lista_puntajes[j]
                                    lista_puntajes[j] = aux_puntaje

                                    aux_nombre = lista_nombre[i]
                                    lista_nombre[i] = lista_nombre[j]
                                    lista_nombre[j] = aux_nombre

                    print(lista_puntajes)
                    print(lista_nombre)

                #actualizar_ranking
                    ventana_ranking.nombre_primer_puesto = lista_nombre[0]
                    ventana_ranking.puntaje_primer_puesto = lista_puntajes[0]

                    if len(lista_puntajes) > 3:
                        ventana_ranking.nombre_segundo_puesto = lista_nombre[1]
                        ventana_ranking.puntaje_segundo_puesto = lista_puntajes[1]

                        ventana_ranking.nombre_tercer_puesto = lista_nombre[2]
                        ventana_ranking.puntaje_tercer_puesto = lista_puntajes[2]

                    elif len(lista_puntajes) == 3:
                        ventana_ranking.nombre_segundo_puesto = lista_nombre[1]
                        ventana_ranking.puntaje_segundo_puesto = lista_puntajes[1]

                    #print(lista_nombre)
                    #print(lista_puntajes)
                    #contador_puestos+=1

                    #print(ventana_ranking.nombre_primer_puesto)
                    #print(ventana_ranking.puntaje_primer_puesto)

                if ventana_ranking.rect_image_salir_ranking.collidepoint(mouse_x, mouse_y):
                    flag_ranking = False
                    flag_no_mostrar_juego = False
                    flag_mostrar_menu = True
                    ventana_ranking.rect_image_salir_ranking.y = -1000
                    fondo_menu.rect_marco_ranking.y = 520
                    print("salir de ranking")

                if ventana_ingresar_nombre.rect_image_boton_play.collidepoint(mouse_x, mouse_y) and ventana_ingresar_nombre.flag_nombre == True:
                    flag_ventana_ingresar_nombre = False
                    ventana_ingresar_nombre.rect_image_boton_play.y = -1000
                    print("Inicio de juego")



        #condicion para escribir el nombre en una ventana desp de darle start
        if event.type == pygame.KEYDOWN:
            #flag_mostrar_menu == False and flag_no_mostrar_juego == False and flag_ranking == True and 
            if event.key == pygame.K_BACKSPACE:
                ventana_ingresar_nombre.ingreso = ventana_ingresar_nombre.ingreso[0:-1]
            else:
                ventana_ingresar_nombre.ingreso += event.unicode

    #mostrar MENU
    if flag_mostrar_menu == True and flag_ranking == False and flag_no_mostrar_juego == False:#and flag_ranking == False puedo agregar esto quizas
        #screen.fill((COLOR_BLANCO))
        fondo_menu.draw()
        pygame.display.flip()
    
    #Mostrar RANKING
    elif flag_mostrar_menu == False and flag_no_mostrar_juego == True and flag_ranking == True:
        screen.fill((COLOR_BLANCO))
        ventana_ranking.draw()
        pygame.display.flip()
    
        #mostrar INGRESAR NOMBRE
    elif flag_ventana_ingresar_nombre == True and flag_mostrar_menu == False:
        screen.fill((GRIS))
        ventana_ingresar_nombre.update()
        #print(ventana_ingresar_nombre.ingreso)
        pygame.display.flip()

    #mostrar JUEGO
    elif flag_mostrar_menu == False and flag_no_mostrar_juego == False and flag_ventana_ingresar_nombre == False:
        ########################################################################################################################
        for enemigos in lista_naves_enemigas:
            if enemigos.rect_imagen_enemiga.colliderect(game.rect) and enemigos not in enemigos_colisionados:
                # Verifica colisión entre nave principal y enemigo, y si el enemigo no está en la lista de colisiones previas
                enemigos_colisionados.append(enemigos)  # Agrega el enemigo a la lista de colisiones
                lives -= 1  # Resta una vida

        #Opcional
        # Limpia la lista de colisiones para eliminar enemigos que ya no están colisionando con la nave principal
        #enemigos_colisionados = [enemy for enemy in enemigos_colisionados if enemy.rect_imagen_enemiga.colliderect(game.rect)]

        nivel.actualizar_nivel()

        screen.fill((GRIS))  # Limpia la pantalla #lo bueno borrar igual

        fondo.draw()

        for disparo in disparos:
            disparo.update()  # Actualiza la lógica de los disparos

        for bala_enemiga in lista_balas_enemigas:
            bala_enemiga.update()
            if bala_enemiga.rect_bala_enemiga.colliderect(game.rect):#Verifica si hay colision entre la nave principal y las balas enemigas
                    bala_enemiga.flag = False
                    bala_enemiga.flag = bala_enemiga.flag
                    bala_enemiga.rect_bala_enemiga.y = -1000
                    bala_enemiga.rect_bala_enemiga.x = -1000
                    ######## OCURRE COLISION Y QUITA UN CORAZON ########
                    lives -= 1

        for nave_enemiga in lista_naves_enemigas:
            nave_enemiga.update_enemigo() # Actualiza la lógica de las naves enemigas

        for vida in lista_vidas:
            vida.update()

        game.update()

        score.draw(screen)
        nivel.draw(screen)

        actualizar_vidas(lives)

        #RESETEAR VALORES PARA JUGAR DE NUEVO
        if lives <= 1 or score.value == 7000:
            fondo_game_over.rect_image_volver_menu.y = 630
            flag_no_mostrar_juego = True
            lives = 4
            score.value = 0
            enemigos_colisionados[:] = []
            nivel.nivel = 1
            lista_naves_enemigas[:] = []
            lista_balas_enemigas[:] = []
            disparos[:] = []
            for vida in lista_vidas:
                vida.flag_vida = True
            cantidad_naves_enemigas = 5
            crear_naves_enemigas(cantidad_naves_enemigas)
            game.rect.x = (ANCHO_VENTANA/2)

        pygame.display.flip()
        clock.tick(60)
        #######################################################################################################################
    
    elif flag_no_mostrar_juego == True:
        screen.fill((COLOR_BLANCO))
        #mando a la mierda el marco de ranking
        fondo_menu.rect_marco_ranking.y = -1000

        fondo_game_over.draw()
        ####
        pygame.display.flip()
        


