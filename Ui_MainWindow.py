# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python-Youtube2Mp3\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 68)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(520, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.urlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(10, 10, 501, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.urlEdit.setFont(font)
        self.urlEdit.setObjectName("urlEdit")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(10, 50, 581, 16))
        self.statusLabel.setObjectName("statusLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.convertButton.setText(_translate("MainWindow", "轉換"))
        self.urlEdit.setPlaceholderText(_translate("MainWindow", "Youtube 網址"))
        self.statusLabel.setText(_translate("MainWindow", "resultLabel"))
