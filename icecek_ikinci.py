from PyQt5.QtWidgets import *
from icecek_python import Ui_MainWindow
from enSon import EnSon

class İcecek_iki(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.icecek=Ui_MainWindow()
        self.icecek.setupUi(self)
        self.son=EnSon()
        self.icecek.pushButton_CAY.clicked.connect(self.cay)
        self.icecek.pushButton_ICETEA.clicked.connect(self.ice)
        self.icecek.pushButton_KOLA.clicked.connect(self.kola)
        self.icecek.pushButton_LIMONATA.clicked.connect(self.limonata)
        self.icecek.pushButton_SU.clicked.connect(self.su)
    def cay(self):
        para=15
        print("Ödemeniz gereken ücret: {}".format(para))
        self.hide()
        self.son.show()
    def ice(self):
        para=35
        print("Ödemeniz gereken ücret: {}".format(para))
        self.hide()
        self.son.show()
    def kola(self):
        para=20
        print("Ödemeniz gereken ücret: {}".format(para))
        self.hide()
        self.son.show()
    
    def limonata(self):
        para=45
        print("Ödemeniz gereken ücret: {}".format(para))
        self.hide()
        self.son.show()
    def su(self):
        para=10
        print("Ödemeniz gereken ücret: {}".format(para))
        self.hide()
        self.son.show()