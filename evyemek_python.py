# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evyemek.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 804)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/men/Menu-PNG-File.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonPIRINC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPIRINC.setGeometry(QtCore.QRect(90, 270, 161, 51))
        self.pushButtonPIRINC.setObjectName("pushButtonPIRINC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 330, 55, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_PILAV_USTU = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PILAV_USTU.setGeometry(QtCore.QRect(90, 360, 161, 51))
        self.pushButton_PILAV_USTU.setObjectName("pushButton_PILAV_USTU")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 420, 55, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_MAKARNA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MAKARNA.setGeometry(QtCore.QRect(90, 450, 161, 51))
        self.pushButton_MAKARNA.setObjectName("pushButton_MAKARNA")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 510, 55, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_KORILI_MAK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_KORILI_MAK.setGeometry(QtCore.QRect(90, 540, 161, 51))
        self.pushButton_KORILI_MAK.setObjectName("pushButton_KORILI_MAK")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 600, 55, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_KRE_MAK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_KRE_MAK.setGeometry(QtCore.QRect(380, 270, 161, 51))
        self.pushButton_KRE_MAK.setObjectName("pushButton_KRE_MAK")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 330, 55, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_PILAV_CACIK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PILAV_CACIK.setGeometry(QtCore.QRect(380, 360, 161, 51))
        self.pushButton_PILAV_CACIK.setObjectName("pushButton_PILAV_CACIK")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 420, 55, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.pushButton_BULGUR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_BULGUR.setGeometry(QtCore.QRect(380, 450, 161, 51))
        self.pushButton_BULGUR.setObjectName("pushButton_BULGUR")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 510, 55, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.pushButton_SARMA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SARMA.setGeometry(QtCore.QRect(380, 540, 161, 51))
        self.pushButton_SARMA.setObjectName("pushButton_SARMA")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 600, 55, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonPIRINC.setText(_translate("MainWindow", "PİRİNÇ PİLAVI"))
        self.label.setText(_translate("MainWindow", "(50 TL)"))
        self.pushButton_PILAV_USTU.setText(_translate("MainWindow", "PİRİNÇ PİLAV ÜSTÜ TAVUK"))
        self.label_2.setText(_translate("MainWindow", "(70 TL)"))
        self.pushButton_MAKARNA.setText(_translate("MainWindow", "MAKARNA"))
        self.label_3.setText(_translate("MainWindow", "(50 TL)"))
        self.pushButton_KORILI_MAK.setText(_translate("MainWindow", "KÖRİLİ MAKARNA"))
        self.label_4.setText(_translate("MainWindow", "(70 TL)"))
        self.pushButton_KRE_MAK.setText(_translate("MainWindow", "KREMALI MAKARNA"))
        self.label_5.setText(_translate("MainWindow", "(80 TL)"))
        self.pushButton_PILAV_CACIK.setText(_translate("MainWindow", "PİRİNÇ PİLAVI+CACIK"))
        self.label_6.setText(_translate("MainWindow", "(85 TL)"))
        self.pushButton_BULGUR.setText(_translate("MainWindow", "BULGUR PİLAVI"))
        self.label_7.setText(_translate("MainWindow", "(50 TL)"))
        self.pushButton_SARMA.setText(_translate("MainWindow", "YAPRAK SARMA"))
        self.label_8.setText(_translate("MainWindow", "(70 TL)"))
import sembol_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())