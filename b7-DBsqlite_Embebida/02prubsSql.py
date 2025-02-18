import sqlite3

# PRUEBAS DE CONSULTA

# Crear la conexión con la Base de Datos
con = None
cur = None

try:
    
    con = sqlite3.connect("b7-DBsqlite_Embebida\\db\\prueba.db")
    print("Conexión establecida con la Base de Datos")

    cur = con.cursor()

    res = cur.execute("SELECT ID, DESCRIPCION FROM TABLA_PRUEBA")

    registros = res.fetchall()

    for registro in registros:
        print(registro)

    print('')
    res = cur.execute("SELECT * FROM TABLA_PRUEBA")

    continuar = True
    while continuar:
        reg = res.fetchone()
        if id == None:
            continuar = False
        else:
            print(f"{reg[0]}, {reg[1]}")

    con.commit()

except Exception as ex:
    print("Error en la conexión: ", ex)
    exit()

finally:
    if cur:
        cur.close()
    if con:
        con.close()
