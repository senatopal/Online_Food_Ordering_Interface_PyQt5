from PyQt5.QtWidgets import *
from corbalar_python import Ui_MainWindowC
from icecek import İcecek
from tercih import Tercih

class Corba(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.corbalar=Ui_MainWindowC()
        self.corbalar.setupUi(self)
        self.icecek=İcecek()
        self.tercih=Tercih()
        self.corbalar.pushButton_DOMATES.clicked.connect(self.domates)
        self.corbalar.pushButton_EZOGELIN.clicked.connect(self.ezogelin)
        self.corbalar.pushButton_MANTAR.clicked.connect(self.mantar)
        self.corbalar.pushButton_MERCIMEK.clicked.connect(self.mercimek)
        self.corbalar.pushButton_SEBZE.clicked.connect(self.sebze)
        self.corbalar.pushButton_TARHANA.clicked.connect(self.tarhana)
        self.corbalar.pushButton_YAYLA.clicked.connect(self.yayla)

    def domates(self):
        para="30"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    def ezogelin(self):
        para="30"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    def mantar(self):
        para="40"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    def mercimek(self):
        para="30"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    def sebze(self):
        para="30"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    def tarhana(self):
        para="30"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    def yayla(self):
        para="35"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()


