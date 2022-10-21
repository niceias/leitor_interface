import sys
import PyQt5.QtWidgets as qtw  # biblioteca de labels
import PyQt5.QtGui as qtg  # biblioteca de fontes
from janela import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QToolTip, QLineEdit, QLabel
from PyQt5 import QtGui
#from PyQt5 import uic, QtWidgets
from programa import caminho_arq, gabarito_regular, regular_adaptado, olimpiada, olimpiada_adaptada, linguagens



class App(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.executar.clicked.connect(lambda: self.funcao_principal())



    def funcao_principal(self):

        if self.regular.isChecked():

            caminho = self.caminho.text()
            dados = []
            file = []
            deletar = []
            caminho, dados, file, deletar = caminho_arq(caminho, dados, file, deletar)
            gabarito_regular(caminho, dados, file, deletar)

        elif self.reg_adap.isChecked():

            caminho = self.caminho.text()
            dados = []
            file = []
            deletar = []
            caminho, dados, file, deletar = caminho_arq(caminho, dados, file, deletar)
            regular_adaptado(caminho, dados, file, deletar)

        elif self.olimpiada.isChecked():

            caminho = self.caminho.text()
            dados = []
            file = []
            deletar = []
            caminho, dados, file, deletar = caminho_arq(caminho, dados, file, deletar)
            olimpiada(caminho, dados, file, deletar)

        elif self.olim_adap.isChecked():

            caminho = self.caminho.text()
            dados = []
            file = []
            deletar = []
            caminho, dados, file, deletar = caminho_arq(caminho, dados, file, deletar)
            olimpiada_adaptada(caminho, dados, file, deletar)

        elif self.linguagem.isChecked():

            caminho = self.caminho.text()
            dados = []
            file = []
            deletar = []
            caminho, dados, file, deletar = caminho_arq(caminho, dados, file, deletar)
            linguagens(caminho, dados, file, deletar)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()


