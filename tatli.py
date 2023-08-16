from PyQt5.QtWidgets import *
from tatli_python import Ui_MainWindow
from tercih import Tercih

class Tatli(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tatli=Ui_MainWindow()
        self.tatli.setupUi(self)
        self.tercih=Tercih()
        self.tatli.pushButton_KREHAVUC.clicked.connect(self.krehavuc)
        self.tatli.pushButton_KUNEFE.clicked.connect(self.kunefe)
        self.tatli.pushButton_PASTA.clicked.connect(self.pasta)
        self.tatli.pushButton_SUFLE.clicked.connect(self.sufle)
        self.tatli.pushButton_WAFFLE.clicked.connect(self.waffle)
    
    def krehavuc(self):
        para="45"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def kunefe(self):
        para="50"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def pasta(self):
        para="60"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def sufle(self):
        para="60"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def waffle(self):
        para="70"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    