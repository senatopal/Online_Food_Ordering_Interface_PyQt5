from PyQt5.QtWidgets import *
from tercih_python import Ui_MainWindow
from icecek import İcecek
from enSon import EnSon

class Tercih(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tercih=Ui_MainWindow()
        self.tercih.setupUi(self)
        self.icecek=İcecek()
        self.son=EnSon()
        self.tercih.pushButtonE.clicked.connect(self.git)
        self.tercih.pushButton_2.clicked.connect(self.gitme)

    def git(self):
        self.hide()
        self.icecek.show()
    
    def gitme(self):
        self.hide()
        with open("sembol.txt","r") as dosya:
            fiyats=dosya.readline()
            fiyati=int(fiyats)
            toplam=fiyati
            print("Ödemeniz gereken ücret: {}".format(toplam))
        self.son.show()
        