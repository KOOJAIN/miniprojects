# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\source\miniprojects\part1\miniprojects\part1\study4jo\sandwich.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 720)
        Form.setMinimumSize(QtCore.QSize(470, 720))
        Form.setMaximumSize(QtCore.QSize(470, 720))
        Form.setStyleSheet("background: rgb(0, 151, 67);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 30, 470, 90))
        self.label.setMinimumSize(QtCore.QSize(470, 90))
        self.label.setMaximumSize(QtCore.QSize(470, 90))
        self.label.setStyleSheet("background: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.img1 = QtWidgets.QLabel(Form)
        self.img1.setGeometry(QtCore.QRect(70, 200, 120, 120))
        self.img1.setMinimumSize(QtCore.QSize(120, 120))
        self.img1.setStyleSheet("background: rgb(255, 255, 255);")
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QLabel(Form)
        self.img2.setGeometry(QtCore.QRect(270, 200, 120, 120))
        self.img2.setMinimumSize(QtCore.QSize(120, 120))
        self.img2.setStyleSheet("background: rgb(255, 255, 255);")
        self.img2.setObjectName("img2")
        self.img3 = QtWidgets.QLabel(Form)
        self.img3.setGeometry(QtCore.QRect(70, 360, 120, 120))
        self.img3.setMinimumSize(QtCore.QSize(120, 120))
        self.img3.setStyleSheet("background: rgb(255, 255, 255);")
        self.img3.setObjectName("img3")
        self.img4 = QtWidgets.QLabel(Form)
        self.img4.setGeometry(QtCore.QRect(270, 360, 120, 120))
        self.img4.setMinimumSize(QtCore.QSize(120, 120))
        self.img4.setStyleSheet("background: rgb(255, 255, 255);")
        self.img4.setObjectName("img4")
        self.img5 = QtWidgets.QLabel(Form)
        self.img5.setGeometry(QtCore.QRect(70, 520, 120, 120))
        self.img5.setMinimumSize(QtCore.QSize(120, 120))
        self.img5.setStyleSheet("background: rgb(255, 255, 255);")
        self.img5.setObjectName("img5")
        self.img6 = QtWidgets.QLabel(Form)
        self.img6.setGeometry(QtCore.QRect(270, 520, 120, 120))
        self.img6.setMinimumSize(QtCore.QSize(120, 120))
        self.img6.setStyleSheet("background: rgb(255, 255, 255);")
        self.img6.setObjectName("img6")
        self.name1 = QtWidgets.QLabel(Form)
        self.name1.setGeometry(QtCore.QRect(90, 330, 81, 16))
        self.name1.setObjectName("name1")
        self.name2 = QtWidgets.QLabel(Form)
        self.name2.setGeometry(QtCore.QRect(290, 330, 81, 16))
        self.name2.setObjectName("name2")
        self.name3 = QtWidgets.QLabel(Form)
        self.name3.setGeometry(QtCore.QRect(90, 490, 81, 16))
        self.name3.setObjectName("name3")
        self.name4 = QtWidgets.QLabel(Form)
        self.name4.setGeometry(QtCore.QRect(290, 490, 81, 16))
        self.name4.setObjectName("name4")
        self.name5 = QtWidgets.QLabel(Form)
        self.name5.setGeometry(QtCore.QRect(90, 650, 81, 16))
        self.name5.setObjectName("name5")
        self.name6 = QtWidgets.QLabel(Form)
        self.name6.setGeometry(QtCore.QRect(290, 650, 81, 16))
        self.name6.setObjectName("name6")
        self.menubar = QtWidgets.QLabel(Form)
        self.menubar.setGeometry(QtCore.QRect(20, 150, 431, 21))
        self.menubar.setStyleSheet("background: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "sandwich"))
        self.img1.setText(_translate("Form", "메뉴1"))
        self.img2.setText(_translate("Form", "메뉴1"))
        self.img3.setText(_translate("Form", "메뉴1"))
        self.img4.setText(_translate("Form", "메뉴1"))
        self.img5.setText(_translate("Form", "메뉴1"))
        self.img6.setText(_translate("Form", "메뉴1"))
        self.name1.setText(_translate("Form", "메뉴이름"))
        self.name2.setText(_translate("Form", "메뉴이름"))
        self.name3.setText(_translate("Form", "메뉴이름"))
        self.name4.setText(_translate("Form", "메뉴이름"))
        self.name5.setText(_translate("Form", "메뉴이름"))
        self.name6.setText(_translate("Form", "메뉴이름"))
        self.menubar.setText(_translate("Form", "메뉴를 선택해 주세요"))