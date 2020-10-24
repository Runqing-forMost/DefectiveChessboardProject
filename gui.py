# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

# 由.ui文件自动生成

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_Bn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_Bn.setGeometry(QtCore.QRect(564, 273, 93, 28))
        self.generate_Bn.setObjectName("generate_Bn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 117, 141, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 167, 120, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 217, 120, 16))
        self.label_3.setObjectName("label_3")
        self.spinBox_level = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_level.setGeometry(QtCore.QRect(570, 117, 81, 21))
        self.spinBox_level.setObjectName("spinBox_level")
        self.spinBox_dr = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_dr.setGeometry(QtCore.QRect(570, 167, 81, 21))
        self.spinBox_dr.setObjectName("spinBox_dr")
        self.spinBox_dc = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_dc.setGeometry(QtCore.QRect(570, 215, 81, 21))
        self.spinBox_dc.setObjectName("spinBox_dc")
        self.clear_Bn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_Bn.setGeometry(QtCore.QRect(444, 273, 93, 28))
        self.clear_Bn.setObjectName("clear_Bn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Defective_Board"))
        self.generate_Bn.setText(_translate("MainWindow", "生成"))
        self.label.setText(_translate("MainWindow", "棋盘级别："))
        self.label_2.setText(_translate("MainWindow", "缺陷的横坐标："))
        self.label_3.setText(_translate("MainWindow", "缺陷的纵坐标："))
        self.clear_Bn.setText(_translate("MainWindow", "清空"))

