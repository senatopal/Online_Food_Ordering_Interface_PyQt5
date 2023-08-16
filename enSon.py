from PyQt5.QtWidgets import *
from enson_python import Ui_MainWindow

class EnSon(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.son=Ui_MainWindow()
        self.son.setupUi(self)
        