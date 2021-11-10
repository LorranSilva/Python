import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Clique aqui!')

        #  adicionando botao na grid (linha, coluna, linhas ocupacao, colunas ocupacao)
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()  # instancia da classe
    app.show()
    qt.exec_()
