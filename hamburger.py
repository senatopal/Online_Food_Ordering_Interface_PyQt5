from PyQt5.QtWidgets import *
from hamburger_python import Ui_MainWindow
from tercih import Tercih

class Hamburger(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hamburger=Ui_MainWindow()
        self.hamburger.setupUi(self)
        self.tercih=Tercih()
        self.hamburger.pushButton_ET.clicked.connect(self.et)
        self.hamburger.pushButton_TAVUK.clicked.connect(self.tavuk)
    
    def et(self):
        para="150"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def tavuk(self):
        para="105"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()