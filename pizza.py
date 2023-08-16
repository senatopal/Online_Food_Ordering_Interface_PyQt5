from PyQt5.QtWidgets import *
from pizzalar_python import Ui_MainWindow
from tercih import Tercih

class Pizza(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.pizza=Ui_MainWindow()
        self.pizza.setupUi(self)
        self.tercih=Tercih()
        self.pizza.pushButton_KARISIK.clicked.connect(self.karisik)
        self.pizza.pushButton_KASARLI.clicked.connect(self.kasarli)
        self.pizza.pushButton_KAVURMALI.clicked.connect(self.kavurmali)
        self.pizza.pushButton_MARGARITA.clicked.connect(self.margarita)
        self.pizza.pushButton_TERRA.clicked.connect(self.terra)
    
    def karisik(self):
        para="120"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def kasarli(self):
        para="100"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def kavurmali(self):
        para="180"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()

    def margarita(self):
        para="130"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()
    
    def terra(self):
        para="140"
        with open("sembol.txt","w") as dosya:
            dosya.write(para)
        self.hide()
        self.tercih.show()