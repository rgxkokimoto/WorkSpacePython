import sqlite3

# Crear la conexión con la Base de Datos
con = None
cur = None

try:
    
    con = sqlite3.connect("b7-DBsqlite_Embebida\\db\\prueba.db")
    print("Conexión establecida con la Base de Datos")

    cur = con.cursor()

    #cur.execute("CREATE TABLE TABLA_PRUEBA (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, DESCRIPCION TEXT NOT NULL)")
    #print("Tabla creada con éxito")
    
    cur.execute("INSERT INTO TABLA_PRUEBA (NOMBRE, DESCRIPCION) VALUES ('PRUEBA1', 'DESCRIPCION1')")
    print("Registro1 insertado con éxito")

    datos = [("PRUEBA2", "DESCRIPCION2"), ("PRUEBA3", "DESCRIPCION3"), ("PRUEBA4", "DESCRIPCION4")]
    print("Registros2 insertados con éxito")

    cur.executemany("INSERT INTO TABLA_PRUEBA (NOMBRE,DESCRIPCION) VALUES (?,?)", datos)
    print("Registros3 insertados con éxito")

    # forma con diccionarios

    dic = ({"desc": 'Descripción del registro 4'},
    {"desc": 'Descripción del registro 5'},)
    cur.executemany("INSERT INTO TABLA_PRUEBA (DESCRIPCION) VALUES (:desc)", dic)

    con.commit()

except Exception as ex:
    print("Error en la conexión: ", ex)
    exit()

finally:
    if cur:
        cur.close()
    if con:
        con.close()
