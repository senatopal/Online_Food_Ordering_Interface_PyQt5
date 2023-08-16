from PyQt5.QtWidgets import *
from evyemek_python import Ui_MainWindow
from tercih import Tercih

class Evy(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.evy=Ui_MainWindow()
        self.evy.setupUi(self)
        self.tercih=Tercih()
        self.evy.pushButton_BULGUR.clicked.connect(self.bulgur)
        self.evy.pushButton_KORILI_MAK.clicked.connect(self.kori)
        self.evy.pushButton_KRE_MAK.clicked.connect(self.kre)
        self.evy.pushButton_MAKARNA.clicked.connect(self.makarna)
        self.evy.pushButton_PILAV_CACIK.clicked.connect(self.pilav)
        self.evy.pushButton_PILAV_USTU.clicked.connect(self.pUst)
        self.evy.pushButton_SARMA.clicked.connect(self.sarma)
        self.evy.pushButtonPIRINC.clicked.connect(self.pirinc)
    
    def bulgur(self):
        para="50"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()

    def kori(self):
        para="70"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()

    def kre(self):
        para="80"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def makarna(self):
        para="50"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()

    def pilav(self):
        para="85"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def pUst(self):
        para="70"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()

    def sarma(self):
        para="70"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()

    def pirinc(self):
        para="50"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
