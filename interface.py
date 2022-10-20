import sys
import PyQt5.QtWidgets as qtw  # biblioteca de labels
import PyQt5.QtGui as qtg  # biblioteca de fontes
from janela import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QToolTip, QLineEdit, QLabel
from PyQt5 import QtGui
# from PyQt5 import uic, QtWidgets
from programa import caminho_arq, gabarito_regular



class App(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.executar.clicked.connect(lambda: self.funcao_principal())



    def funcao_principal(self):

        if self.regular.isChecked():
            var = self.caminho.text()
            print(var)





if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()


