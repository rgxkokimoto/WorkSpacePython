# Esta es una plantilla para la conexión a una Base de Datos PostgreSQL
# Se debe tener en cuenta que se debe instalar psycopg2

import psycopg2

con = None
cur = None

# Establecer la conexión con la Base de Datos
try:
    con = psycopg2.connect(dbname="postgres", user="postgres", password="reguri34marwrt", host="127.0.0.1", port="5432", client_encoding="utf-8")
    print("### conexión establecida")

    cur = con.cursor()
    print("### cursor preparado")

    cur.execute('SELECT version()')
    version = cur.fetchone()
    print(f"Versión de PostgreSQL: {version}")
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