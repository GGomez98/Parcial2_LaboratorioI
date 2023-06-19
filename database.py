import sqlite3

def insert_datos(nombre, puntuacion, tiempo, db):
    with sqlite3.connect(db) as conexion:
        try:
            conexion.execute("insert into puntuaciones(nombre,puntuacion,tiempo)values (?,?,?)", (nombre, puntuacion, tiempo))
            conexion.commit()
        except:
            print("Error")

def get_datos(db):

    datos = []

    with sqlite3.connect(db) as conexion:
        cursor=conexion.execute("SELECT * FROM puntuaciones ORDER BY puntuacion DESC, tiempo LIMIT 10")
        for fila in cursor:
            datos.append(fila)
    
    return datos

def crear_tabla(db, nombre_tabla):
    with sqlite3.connect(db) as conexion:
        try:
            sentencia = f''' create table {nombre_tabla}
            (
            id integer primary key autoincrement,
            nombre text,
            puntuacion integer,
            tiempo text
            )
            '''
            conexion.execute(sentencia)
            print(f"Se creo la tabla {nombre_tabla}")
        except sqlite3.OperationalError:
            print(f"La tabla {nombre_tabla} ya existe")

def borrar_tabla(db, tabla):
    with sqlite3.connect(db) as conexion:
        sentencia = f"DROP TABLE IF EXISTS {tabla}"
        conexion.execute(sentencia)

def guardar_archivo(nombre_archivo, contenido):

    if isinstance(contenido, str):
        archivo = open(nombre_archivo,'w+')
        archivo.write(contenido)
        archivo.close()
        print("Se cargo el archivo: "+nombre_archivo)
        retorno = True
    else:
        print('Error al cargar el archivo: '+nombre_archivo)
        retorno = False
    
    return retorno

def cargar_lista(lista, nombre_archivo):
    lista_a_cargar = ["pos,nombre,puntos,tiempo\n"]
    i = 1

    for jugador in lista:

        jugador = str(i)+","+jugador[1]+","+str(jugador[2]).zfill(4)+","+jugador[3]+"\n"
        lista_a_cargar.append(jugador)
        i+= 1

    lista_a_cargar = "".join(lista_a_cargar)
    retorno = guardar_archivo(nombre_archivo, lista_a_cargar)
    
    return retorno

