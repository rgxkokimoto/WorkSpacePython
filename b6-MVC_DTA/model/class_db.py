import psycopg2
import configparser

class ConDB:
    def __init__(self):
       

        config = configparser.ConfigParser()
        config.read("MVC_DTA/config.ini")
        self.dbname = config['BBDD']['dbname']
        self.user = config['BBDD']['user']
        self.password = config['BBDD']['password']
        self.host = config['BBDD']['host']
        self.port = config['BBDD']['port']
        self.client_encoding = config['BBDD']['client_encoding']

        #! forma 1
        ''' self.dbname = "PRUEBA_DB"
        self.user = "postgres"
        self.password = "reguri34marwrt"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.client_encoding = "UTF8"'''
    

    # Contructor independizar el momento de la contrucción con los datos.
    def getConexion(self):
        con = None
        try:
            con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port, client_encoding=self.client_encoding)
            print("### conexión establecida")
        except Exception as ex:
            print('No se ha podido conectar con la Base de Datos')
            print(type(ex))
            print(ex)

        return con
    
    