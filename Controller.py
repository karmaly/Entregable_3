from Model import *
from View import VentanaPpal
from PyQt5.QtWidgets import QApplication
import sys 

#Como el coordindor enlaza el modelo con la vista debe tener acceso a objetos de ambas clases,
#La idea es que la vista pase los datos que quiere guardar en el modelo, este metodo se encarga de verificar que si se puedan
#guardar y en caso de que si se pueda se guardan

class Coordinador():
    def __init__(self, vista, modelo):
        self.__miVista = vista
        self.__miModelo = modelo


# Código cliente
def main():
    app = QApplication(sys.argv) #Aplicación cargada una sola vez
    mi_vista = VentanaPpal() #caga de mi ventana principal
    mi_modelo = Sistema()
    mi_controlador = Coordinador(mi_vista, mi_modelo) #Enlace de la vista con el modelo
    mi_vista.setControlador(mi_controlador) #Entrega de la vi
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()