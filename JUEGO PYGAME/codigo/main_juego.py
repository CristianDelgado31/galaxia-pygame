import pygame, sys
from pygame.locals import *
from color import *
from base_de_datos import *

#CLASES
from clase_ventana_ingresar_nombre import VentanaIngreseNombre
from clase_fondo import *
from clase_ranking import Ranking
from clase_nivel import Nivel
from clase_score import Score
from dimensiones_ventana import *
from clase_naves_enemigas import *
from clase_nave_principal import *
from clase_disparo_nave_enemiga import*
from clsae_disparo_nave_principal import *
from funciones_vida import *


pygame.init()

pygame.mixer.init()
#SONIDOS
musica_fondo = pygame.mixer.Sound("sonidos\music_fondo.mp3")
musica_fondo.play(-1)
musica_fondo.set_volume(0.2)

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

                    #vacio las listas
                    lista_puntajes[:] = []
                    lista_nombre[:] = []

                    mostrar_datos_ranking(lista_nombre, lista_puntajes)
                                        
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


                    #actualizar_ranking
                    ventana_ranking.nombre_primer_puesto = lista_nombre[0]
                    ventana_ranking.puntaje_primer_puesto = lista_puntajes[0]

                    if len(lista_puntajes) >= 3:
                        ventana_ranking.nombre_segundo_puesto = lista_nombre[1]
                        ventana_ranking.puntaje_segundo_puesto = lista_puntajes[1]

                        ventana_ranking.nombre_tercer_puesto = lista_nombre[2]
                        ventana_ranking.puntaje_tercer_puesto = lista_puntajes[2]

                    elif len(lista_puntajes) == 2:
                        ventana_ranking.nombre_segundo_puesto = lista_nombre[1]
                        ventana_ranking.puntaje_segundo_puesto = lista_puntajes[1]


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
        fondo_menu.draw(screen)
        pygame.display.flip()
    
    #Mostrar RANKING
    elif flag_mostrar_menu == False and flag_no_mostrar_juego == True and flag_ranking == True:
        screen.fill((COLOR_BLANCO))
        ventana_ranking.draw(screen)
        pygame.display.flip()
    
        #mostrar INGRESAR NOMBRE
    elif flag_ventana_ingresar_nombre == True and flag_mostrar_menu == False:
        screen.fill((GRIS))
        #ventana_ingresar_nombre.draw(screen)
        ventana_ingresar_nombre.update(screen)
        #print(ventana_ingresar_nombre.ingreso)
        pygame.display.flip()

    #mostrar JUEGO
    elif flag_mostrar_menu == False and flag_no_mostrar_juego == False and flag_ventana_ingresar_nombre == False:

        for enemigos in lista_naves_enemigas:
            if enemigos.rect_imagen_enemiga.colliderect(game.rect) and enemigos not in enemigos_colisionados:
                # Verifica colisión entre nave principal y enemigo, y si el enemigo no está en la lista de colisiones previas
                enemigos_colisionados.append(enemigos)  # Agrega el enemigo a la lista de colisiones
                lives -= 1  # Resta una vida

        #Opcional
        # Limpia la lista de colisiones para eliminar enemigos que ya no están colisionando con la nave principal
        #enemigos_colisionados = [enemy for enemy in enemigos_colisionados if enemy.rect_imagen_enemiga.colliderect(game.rect)]

        nivel.actualizar_nivel(score)

        screen.fill((GRIS))  # Limpia la pantalla

        fondo.draw(screen)

        for disparo in disparos:
            disparo.verificar_colision(score)
            disparo.update(screen)  # Actualiza la lógica de los disparos

        for bala_enemiga in lista_balas_enemigas:
            bala_enemiga.update(screen)
            if bala_enemiga.rect_bala_enemiga.colliderect(game.rect):#Verifica si hay colision entre la nave principal y las balas enemigas
                    bala_enemiga.flag = False
                    bala_enemiga.flag = bala_enemiga.flag
                    bala_enemiga.rect_bala_enemiga.y = -1000
                    bala_enemiga.rect_bala_enemiga.x = -1000
                    ######## OCURRE COLISION Y QUITA UN CORAZON ########
                    lives -= 1

        for nave_enemiga in lista_naves_enemigas:
            nave_enemiga.update_enemigo(screen) # Actualiza la lógica de las naves enemigas

        for vida in lista_vidas:
            vida.update(screen)

        game.update(screen)

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

    #Mostrar fin del juego
    elif flag_no_mostrar_juego == True:
        screen.fill((COLOR_BLANCO))
        #mando a la mierda el marco de ranking
        fondo_menu.rect_marco_ranking.y = -1000

        fondo_game_over.draw(screen)
        ####
        pygame.display.flip()
        


