import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QRegularExpressionValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaPpal(QMainWindow):
    def __init__(self, ppal = None):
        super().__init__(ppal)
        loadUi("ventana_acceso.ui",self)
        self.setup()

    def setup(self):
        #Creación de una calidador con una expresión regular que permite solo caracteres alfanuméricos
        regex = r'^[a-zA-Z0-9]+$'
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(regex)
        self.usuario.setValidator(QRegExpValidator(validator))
        self.clave.setValidator(QRegExpValidator(validator))
        self.botonIngreso.accepted.connect(self.opcionIngresar)
        self.botonIngreso.rejected.connect(self.opcionSalir)
    
    def setControlador(self,c):
        self.__miControlador = c

    def recibir_info(self, u, c):
        self.__miControlador.recibir_info(u, c)

    def opcionIngresar(self):
        u = self.usuario.text()
        c = self.clave.text()
        return u, c
        
    def opcionSalir(self):
        self.close()

class VentanaOpc(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_actualizar.ui",self)
        self.__ventanaPadre=ppal
        # self.setup()
        
