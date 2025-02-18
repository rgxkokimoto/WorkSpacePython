import psycopg2

cur = None
cur = None

try: 
    con = psycopg2.connect(dbname="PRUEBA_DB", user="postgres", password="reguri34marwrt", host="127.0.0.1", port="5432", client_encoding="utf-8")

    cur = con.cursor()
    cur.execute("SELECT * FROM TABLA_PRUEBAS")
    
    registros = cur.fetchall() #* fetchall() devuelve una lista de tuplas

    for registro in registros:
        print(registro)

    print("### Consulta con fetchone")
    cur.execute("SELECT * FROM TABLA_PRUEBAS WHERE ID = 1")

    continuar = True
    while continuar:
        registro = cur.fetchone()
        if registro == None:
            continuar = False
        else:
            print(f"{registro[0]}, {registro[1]}")

except Exception as ex:
    print('No se ha podido conectar con la Base de Datos')
    print(type(ex))
    print(ex)

finally:
    if cur != None:
        cur.close()
    if con != None:
        con.close()
    print("### conexión cerrada")
