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


class Game:#esta clase deberia ir a en otro archivo
    def __init__(self) -> None:
        self.fondo_juego = Fondo()#Tips ser mas generico, agregar valores a las clases como img, velocidad, etc
        self.fondo_menu = Menu()
        self.nave_jugador = NaveJugador()
        self.fondo_game_over = FondoGameOver()
        self.ventana_ingresar_nombre = VentanaIngreseNombre()
        self.ventana_ranking = Ranking()
        self.score = Score(10, 10)
        self.nivel = Nivel(ANCHO_VENTANA/2,10)
        self.lives = 4
        self.enemigos_colisionados = []
        self.lista_nombre = []
        self.lista_puntajes = []
        self.lista_nombre = []
        self.lista_puntajes = []
        self.flag_mostrar_menu = True
        self.flag_no_mostrar_juego = False
        self.flag_ranking = False
        self.flag_ventana_ingresar_nombre = True

    def reiniciar_valores(self, game):
        if game.lives <= 1 or game.score.value == 7000:
            game.fondo_game_over.rect_image_volver_menu.y = 630
            game.flag_no_mostrar_juego = True
            game.lives = 4
            game.score.value = 0
            game.enemigos_colisionados[:] = []
            game.nivel.nivel = 1
            lista_naves_enemigas[:] = []
            lista_balas_enemigas[:] = []
            disparos[:] = []
            for vida in lista_vidas:
                vida.flag_vida = True
            cantidad_naves_enemigas = 5
            crear_naves_enemigas(cantidad_naves_enemigas)
            game.nave_jugador.rect.x = (ANCHO_VENTANA/2)

    def actualizar_ranking(self, game, lista_nombres, lista_puntajes):
        game.ventana_ranking.nombre_primer_puesto = lista_nombres[0]
        game.ventana_ranking.puntaje_primer_puesto = lista_puntajes[0]
        if len(lista_puntajes) >= 3:
            game.ventana_ranking.nombre_segundo_puesto = lista_nombres[1]
            game.ventana_ranking.puntaje_segundo_puesto = lista_puntajes[1]
            game.ventana_ranking.nombre_tercer_puesto = lista_nombres[2]
            game.ventana_ranking.puntaje_tercer_puesto = lista_puntajes[2]
        elif len(lista_puntajes) == 2:
            game.ventana_ranking.nombre_segundo_puesto = lista_nombres[1]
            game.ventana_ranking.puntaje_segundo_puesto = lista_puntajes[1]

