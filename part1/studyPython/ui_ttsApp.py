# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\source\miniprojects\part1\miniprojects\part1\studyPython\ttsApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(320, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(320, 100))
        Form.setMaximumSize(QtCore.QSize(320, 100))
        self.txtQrData = QtWidgets.QLineEdit(Form)
        self.txtQrData.setEnabled(True)
        self.txtQrData.setGeometry(QtCore.QRect(10, 10, 301, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtQrData.sizePolicy().hasHeightForWidth())
        self.txtQrData.setSizePolicy(sizePolicy)
        self.txtQrData.setObjectName("txtQrData")
        self.btnQrGen = QtWidgets.QPushButton(Form)
        self.btnQrGen.setGeometry(QtCore.QRect(230, 60, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQrGen.sizePolicy().hasHeightForWidth())
        self.btnQrGen.setSizePolicy(sizePolicy)
        self.btnQrGen.setObjectName("btnQrGen")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QRCODE App"))
        self.btnQrGen.setText(_translate("Form", "Generate"))
