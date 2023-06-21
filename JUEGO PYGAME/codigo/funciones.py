


def actualizar_ranking(lista_puntajes, lista_nombre):
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
########################################################################
