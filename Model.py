import mysql.connector
import json

class BaseD():
    def __init__(self):
        try:
            cnx = mysql.connector.connect(user = 'admin' , password = 'bio4100' , host = 'localhost' , database = 'general_hospital')
            cursor = cnx.cursor()
            return cursor
        except mysql.connector.ProgrammingError:
            return 'No posee las credenciales para acceder a la base de datos\n'
        except mysql.connector.DatabaseError:
            return 'No hay conexión con el servidor'