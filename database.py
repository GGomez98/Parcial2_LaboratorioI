import sqlite3

def insert_datos(nombre, puntuacion, db):
    with sqlite3.connect(db) as conexion:
        try:
            conexion.execute("insert into puntuaciones(nombre,puntuacion)values (?,?)", (nombre, puntuacion))
            conexion.commit()
        except:
            print("Error")

def get_datos(db):
    with sqlite3.connect(db) as conexion:
        cursor=conexion.execute("SELECT * FROM puntuaciones")
        for fila in cursor:
            print(fila)

def crear_tabla(db, nombre_tabla):
    with sqlite3.connect(db) as conexion:
        try:
            sentencia = f''' create table {nombre_tabla}
            (
            id integer primary key autoincrement,
            nombre text,
            puntuacion integer
            )
            '''
            conexion.execute(sentencia)
            print(f"Se creo la tabla {nombre_tabla}")
        except sqlite3.OperationalError:
            print(f"La tabla {nombre_tabla} ya existe")

def borrar_tabla(db, tabla):
    with sqlite3.connect(db) as conexion:
        sentencia = f"DELETE FROM {tabla}"
        conexion.execute(sentencia)

#crear_tabla("bd_btf.db", "puntuaciones")
#insert_datos("Gaston", 3000, "bd_btf.db")
#get_datos("bd_btf.db")
#borrar_tabla("bd_btf.db", "puntuaciones")