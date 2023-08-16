from PyQt5.QtWidgets import *
from giris_python import Ui_MainWindow
from corbalar import Corba
from evyemek import Evy
from hamburger import Hamburger
from pizza import Pizza
from tatli import Tatli
from icecek_ikinci import İcecek_iki

class Giris(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.giris=Ui_MainWindow()
        self.giris.setupUi(self)
        self.corbalar=Corba()
        self.ev=Evy()
        self.hamburger=Hamburger()
        self.pizza=Pizza()
        self.tatli=Tatli()
        self.icecek=İcecek_iki()
        self.giris.pushButton_CORBA.clicked.connect(self.corba)
        self.giris.pushButton_EV.clicked.connect(self.Ev)
        self.giris.pushButton_HAMBURGER.clicked.connect(self.burger)
        self.giris.pushButton_PIZZA.clicked.connect(self.piz)
        self.giris.pushButton_TATLILAR.clicked.connect(self.tatlilar)
        self.giris.pushButton_ICECEKLER.clicked.connect(self.icecekler)
        
    def corba(self):
        self.hide()
        self.corbalar.show()

    def Ev(self):
        self.hide()
        self.ev.show()

    def burger(self):
        self.hide()
        self.hamburger.show()

    def piz(self):
        self.hide()
        self.pizza.show()

    def tatlilar(self):
        self.hide()
        self.tatli.show()   
    
    def icecekler(self):
        self.hide()
        self.icecek.show()