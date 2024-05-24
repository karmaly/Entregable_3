import mysql.connector
import json

class BaseMySQL():
    def __init__(self, host, username, password, database):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database = database
        self.__connection = None


        except mysql.connector.ProgrammingError:
            return 'No posee las credenciales para acceder a la base de datos\n'
        except mysql.connector.DatabaseError:
            return 'No hay conexión con el servidor'
    
    def validarPac():
        while True:
            id_ = input('Ingrese documento de identidad: ')
            id_val = validarnumero(id_)
            if id_val == True:
                break
            elif id_val == False:
                continue
        buscar = 'SELECT * FROM pacientes WHERE id_ = "%s"' % id_
        cursor.execute(buscar)
        results = cursor.fetchall()
        if len(results) == 0:
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido : ')
            nacimiento = input('Ingrese fecha de nacimiento: ')
            while True:
                generoi = input('Ingrese género: M (Masculino) o F(Femenino): ')
                generoj = generoi.upper()
                if (generoj == 'F') or (generoj == 'M'):
                    genero = generoj
                    break
                else:
                    print('Ingrese F o M: ')
            direccion = input('Ingrese dirección: ')
            telefono = input('Ingrese teléfono: ')
            pc = {
            'id_' : id_,
            'nombre' : nombre,
            'apellido' : apellido,
            'nacimiento' : nacimiento,
            'genero' : genero,
            'direccion' : direccion,
            'telefono' : telefono
            }
            query = 'INSERT INTO pacientes (id_, nombre, apellido, nacimiento, genero, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            values = (pc['id_'], pc['nombre'], pc['apellido'], pc['nacimiento'], pc['genero'], pc['direccion'], pc['telefono'])
            cursor.execute(query,values)
            cnx.commit()
            print('Paciente ingresado exitosamente')
        else:
            print('El paciente ya se encuentra en la base de datos')
    def ingresarPac():
        pass
    def buscarPac():
        pass
    def eliminarPac():
        pass

    def conectar(self):
        try:
            self.__connection = mysql.connector.connect(
                host=self.__host,
                user=self.__username,
                password=self.__password,
                database=self.__database
            )
            print("Conexión establecida correctamente")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def desconectar(self):
        if self.__connection:
            self.__connection.close()
            print("Conexión cerrada correctamente")
        else:
            print("No hay conexión activa para cerrar")

    def execute_query(self, query):
        self.__connect()  # Llama al método privado para establecer la conexión
        if self.__connection:
            try:
                cursor = self.__connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                self.__disconnect()  # Llama al método privado para cerrar la conexión
                return result
            except mysql.connector.Error as err:
                print(f"Error al ejecutar la consulta: {err}")
                return None
        else:
            print("No hay conexión activa")

class MySQLConnection:
    def __init__(self, host, username, password, database):
        self._host = host
        self._username = username
        self._password = password
        self._database = database
        self._connection = None

    def connect(self):
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database=self._database
            )
            print("Conexión establecida correctamente")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def disconnect(self):
        if self._connection:
            self._connection.close()
            print("Conexión cerrada correctamente")
        else:
            print("No hay conexión activa para cerrar")

    def execute_query(self, query):
        if self._connection:
            try:
                cursor = self._connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except mysql.connector.Error as err:
                print(f"Error al ejecutar la consulta: {err}")
                return None
        else:
            print("No hay conexión activa")

# Ejemplo de uso
if __name__ == "__main__":
    # Crea una instancia de la clase MySQLConnection
    conexion = MySQLConnection(host="localhost", username="tu_usuario", password="tu_contraseña", database="tu_base_de_datos")
    
    # Conéctate a la base de datos
    conexion.connect()
    
    # Ejecuta una consulta
    resultado = conexion.execute_query("SELECT * FROM tabla_ejemplo")
    print(resultado)
    
    # Cierra la conexión
    conexion.disconnect()