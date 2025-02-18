import psycopg2
from model.class_db import ConDB

NOMBRE_TABLA = "LISTA_COMPRA"

NOM_COL_PROD = "NOM_PRODUCTO"
NOM_COL_CANT = "CANTIDAD"

class ListaCompra:
    def __init__(self):
        self.con = None

    def crear_tabla(self):
        
        con = None
        cur = None

        try:
            con = ConDB().getConexion()

            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS LISTA_COMPRA" + NOMBRE_TABLA) 
            cur.execute("CREATE TABLE " + NOM_TABLA +  "(ID integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (INCREMENT 1 START 1 CHACHE 4), " + NOM_COL_PROD + " TEXT NOT NULL, " + NOM_COL_CANT + " text")
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

    def insertar_producto(self, producto, cantidad):
        con = None
        cur = None
        try:
            con = ConDB().getConexion()

            cur = con.cursor()
            cur.execute("INSERT INTO " + NOMBRE_TABLA + " (" + NOM_COL_PROD + ", " + NOM_COL_CANT + ") VALUES (?, ?)", lista_valores)

            con.commit()

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

    def consultar_productos(self):