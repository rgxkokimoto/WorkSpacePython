import psycopg2

con = None
cur = None

# Establecer la conexión con la Base de Datos que creamos en postgres
try:
    con = psycopg2.connect(dbname="PRUEBA_DB", user="postgres", password="reguri34marwrt", host="127.0.0.1", port="5432", client_encoding="utf-8")
    print("### conexión establecida")

    cur = con.cursor()
    print("### cursor preparado")

    cur.execute('DROP TABLE IF EXISTS "TABLA_PRUEBAS"')
    print("### tabla eliminada")

    '''
    #!El problema radica en la sensibilidad a mayúsculas y minúsculas de los nombres de las tablas en PostgreSQL. 
    Al crear la tabla sin comillas dobles, PostgreSQL la almacena en minúsculas (tabla_pruebas), 
    pero al consultarla con "TABLA_PRUEBAS" (usando comillas dobles y mayúsculas), no se encuentra.
    '''
    cur.execute('CREATE TABLE "TABLA_PRUEBAS" (ID Integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (INCREMENT 1 START 1 CACHE 4), DESCRIPCION text NOT NULL)')
    print("### tabla creada")

    cur.execute('INSERT INTO "TABLA_PRUEBAS" (DESCRIPCION) VALUES (%s)', ('Prueba a',))
    cur.execute('INSERT INTO "TABLA_PRUEBAS" (DESCRIPCION) VALUES (%s)', ('Prueba c',))

    #! No olvidar hacer commit para que los cambios se guarden en la Base de Datos
    con.commit()

except Exception as ex:
    print('No se ha podido conectar con la Base de Datos')
    print(type(ex))
    print(ex)

finally:
    #* Buena práctica cerrar la conexión y el cursor
    if cur != None:
        cur.close()
    if con != None:
        con.close()
    print("### conexión cerrada")

