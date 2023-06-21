from clase_vida import Vidas


############### FUNCIONES VIDA  ###############

lista_vidas = []
i = 0
#Crear vidas
for vidas in range(3):
    lista_vidas.append(Vidas(20+i, 800, 30, 30))
    i+=30


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


############### FUNCIONES VIDA  ###############