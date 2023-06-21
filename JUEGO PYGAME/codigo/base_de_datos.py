import sqlite3


with sqlite3.connect("datos_jugadores.db") as conexion:
    try:
        sentencia = ''' create table jugadores
                        (
                            nombre text,
                            puntaje integer
                        )
                    '''
        conexion.execute(sentencia)
        print("Se creo la tabla jugadores")

    except sqlite3.OperationalError:
        print("La tabla jugadores ya existe")


def insertar_datos(nombre, puntaje):
    with sqlite3.connect("datos_jugadores.db") as conexion:
        try:
            conexion.execute("insert into jugadores(nombre,puntaje) values (?,?)", (nombre, puntaje))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")


#SELECT
def mostrar_datos_ranking(lista_nombre, lista_puntajes):
    import sqlite3
    with sqlite3.connect("datos_jugadores.db") as conexion:
        cursor = conexion.execute("SELECT * FROM jugadores order by puntaje DESC")
        for fila in cursor:
            lista_nombre.append(fila[0])
            lista_puntajes.append(fila[1])
