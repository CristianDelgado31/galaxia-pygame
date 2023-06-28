import pygame, sys
from pygame.locals import *
from color import *
from base_de_datos import *

#CLASES

from dimensiones_ventana import *
from clase_naves_enemigas import *
from clase_nave_principal import *
from clase_disparo_nave_enemiga import*
from clsae_disparo_nave_principal import *
from funciones_vida import *
from game import Game


pygame.init()

pygame.mixer.init()
#SONIDOS
musica_fondo = pygame.mixer.Sound("sonidos\music_fondo.mp3")
musica_fondo.play(-1)
musica_fondo.set_volume(0.2)

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego galaxia")
#TIEMPO
clock = pygame.time.Clock()
#JUEGO
game = Game()

#score_jugador
def score_jugador(score):#borrador
    print(score)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if game.fondo_menu.rect_marco_start.collidepoint(mouse_x, mouse_y):
                    if game.flag_mostrar_menu == True and game.flag_no_mostrar_juego == False:
                        game.flag_mostrar_menu = False
                        game.score.acumulador_puntos = 0 # reinicio acumulador de puntos
                        game.ventana_ingresar_nombre.ingreso = ''

                        #reubico el rect de volver al menu en la ventana game over
                        game.fondo_game_over.rect_image_volver_menu.y = -1000
                        game.fondo_menu.rect_marco_ranking.y = -1000
                        game.ventana_ingresar_nombre.rect_image_boton_play.y = 500


                if game.fondo_menu.rect_marco_ranking.collidepoint(mouse_x, mouse_y):
                    # Se ha producido una colisión
                    print("Ingreso a ranking")
                    #print(score.acumulador_puntos)#puedo mandar los datos a una base de datos
                    game.flag_no_mostrar_juego = True
                    game.flag_mostrar_menu = False
                    game.flag_ranking = True

                    #desp los devuelvo a su posicion con una colision dentro de ventana ranking
                    game.fondo_game_over.rect_image_volver_menu.y = -1000
                    game.fondo_menu.rect_marco_ranking.y = -1000
                    #salir de ranking
                    game.ventana_ranking.rect_image_salir_ranking.y = 0


                if game.fondo_game_over.rect_image_volver_menu.collidepoint(mouse_x, mouse_y):
                    game.flag_mostrar_menu = True
                    game.flag_no_mostrar_juego = False
                    game.flag_ranking = False
                    game.flag_ventana_ingresar_nombre = True
                    #posiciono de nuevo a marco ranking
                    game.fondo_menu.rect_marco_ranking.y = 520
                    #Buen lugar para guardar los datos creo
                    print("Saliendo de game over e ingresando a menú")
                    print("Datos guardados")
                    
                    insertar_datos(game.ventana_ingresar_nombre.guardar_nombre, game.score.acumulador_puntos)

                    #vacio las listas
                    game.lista_puntajes[:] = []
                    game.lista_nombre[:] = []

                    mostrar_datos_ranking(game.lista_nombre, game.lista_puntajes)

                    #actualizar_ranking
                    game.actualizar_ranking(game, game.lista_nombre, game.lista_puntajes)


                if game.ventana_ranking.rect_image_salir_ranking.collidepoint(mouse_x, mouse_y):
                    game.flag_ranking = False
                    game.flag_no_mostrar_juego = False
                    game.flag_mostrar_menu = True
                    game.ventana_ranking.rect_image_salir_ranking.y = -1000
                    game.fondo_menu.rect_marco_ranking.y = 520
                    print("salir de ranking")

                if game.ventana_ingresar_nombre.rect_image_boton_play.collidepoint(mouse_x, mouse_y) and game.ventana_ingresar_nombre.flag_nombre == True:
                    game.flag_ventana_ingresar_nombre = False
                    game.ventana_ingresar_nombre.rect_image_boton_play.y = -1000
                    print("Inicio de juego")


        #condicion para escribir el nombre en una ventana desp de darle start
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                game.ventana_ingresar_nombre.ingreso = game.ventana_ingresar_nombre.ingreso[0:-1]
            else:
                game.ventana_ingresar_nombre.ingreso += event.unicode

    #mostrar MENU
    if game.flag_mostrar_menu == True and game.flag_ranking == False and game.flag_no_mostrar_juego == False:
        game.fondo_menu.draw(screen)
        pygame.display.flip()
    
    #Mostrar RANKING
    elif game.flag_mostrar_menu == False and game.flag_no_mostrar_juego == True and game.flag_ranking == True:
        screen.fill((COLOR_BLANCO))
        game.ventana_ranking.draw(screen)
        pygame.display.flip()
    
    #mostrar INGRESAR NOMBRE
    elif game.flag_ventana_ingresar_nombre == True and game.flag_mostrar_menu == False:
        screen.fill((GRIS))
        game.ventana_ingresar_nombre.update(screen)
        pygame.display.flip()

    #mostrar JUEGO
    elif game.flag_mostrar_menu == False and game.flag_no_mostrar_juego == False and game.flag_ventana_ingresar_nombre == False:

        for enemigos in lista_naves_enemigas:
            if enemigos.rect_imagen_enemiga.colliderect(game.nave_jugador.rect) and enemigos not in game.enemigos_colisionados:
                # Verifica colisión entre nave principal y enemigo, y si el enemigo no está en la lista de colisiones previas
                game.enemigos_colisionados.append(enemigos)  # Agrega el enemigo a la lista de colisiones
                game.lives -= 1  # Resta una vida

        game.nivel.actualizar_nivel(game.score)

        screen.fill((GRIS))  # Limpia la pantalla

        game.fondo_juego.draw(screen)

        for disparo in disparos:
            disparo.verificar_colision(game.score)
            disparo.update(screen)  # Actualiza la lógica de los disparos

        for bala_enemiga in lista_balas_enemigas:
            bala_enemiga.update(screen)
            if bala_enemiga.rect_bala_enemiga.colliderect(game.nave_jugador.rect):#Verifica si hay colision entre la nave principal y las balas enemigas
                    bala_enemiga.flag = False
                    bala_enemiga.flag = bala_enemiga.flag
                    bala_enemiga.rect_bala_enemiga.y = -1000
                    bala_enemiga.rect_bala_enemiga.x = -1000
                    ######## OCURRE COLISION Y QUITA UN CORAZON ########
                    game.lives -= 1

        for nave_enemiga in lista_naves_enemigas:
            nave_enemiga.update_enemigo(screen) # Actualiza la lógica de las naves enemigas

        for vida in lista_vidas:
            vida.update(screen)

        game.nave_jugador.update(screen)

        game.score.draw(screen)
        
        game.nivel.draw(screen)

        actualizar_vidas(game.lives)

        #RESETEAR VALORES PARA JUGAR DE NUEVO
        if game.lives <= 1 or game.score.value == 7000:
            game.reiniciar_valores(game)

        pygame.display.flip()
        clock.tick(60)

    #Mostrar fin del juego
    elif game.flag_no_mostrar_juego == True:
        screen.fill((COLOR_BLANCO))
        #mando a la mierda el marco de ranking
        game.fondo_menu.rect_marco_ranking.y = -1000

        game.fondo_game_over.draw(screen)
        ####
        pygame.display.flip()
        


