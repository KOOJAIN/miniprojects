# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\source\miniprojects\part1\miniprojects\part1\miniprojects\part1\studyPyQt\addressBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        MainWindow.setFont(font)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupbox.setObjectName("groupbox")
        self.btnNew = QtWidgets.QPushButton(self.groupbox)
        self.btnNew.setGeometry(QtCore.QRect(410, 110, 80, 30))
        self.btnNew.setObjectName("btnNew")
        self.btnSave = QtWidgets.QPushButton(self.groupbox)
        self.btnSave.setGeometry(QtCore.QRect(490, 110, 80, 30))
        self.btnSave.setObjectName("btnSave")
        self.label = QtWidgets.QLabel(self.groupbox)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QLineEdit(self.groupbox)
        self.txtName.setGeometry(QtCore.QRect(90, 30, 181, 20))
        self.txtName.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txtName.setObjectName("txtName")
        self.txtPhone = QtWidgets.QLineEdit(self.groupbox)
        self.txtPhone.setGeometry(QtCore.QRect(90, 60, 181, 20))
        self.txtPhone.setObjectName("txtPhone")
        self.label_3 = QtWidgets.QLabel(self.groupbox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 56, 12))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtEmail = QtWidgets.QLineEdit(self.groupbox)
        self.txtEmail.setGeometry(QtCore.QRect(90, 90, 181, 20))
        self.txtEmail.setObjectName("txtEmail")
        self.label_4 = QtWidgets.QLabel(self.groupbox)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 56, 12))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.txtAddress = QtWidgets.QLineEdit(self.groupbox)
        self.txtAddress.setGeometry(QtCore.QRect(90, 120, 181, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.label_6 = QtWidgets.QLabel(self.groupbox)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 56, 12))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.btnDel = QtWidgets.QPushButton(self.groupbox)
        self.btnDel.setGeometry(QtCore.QRect(490, 80, 80, 30))
        self.btnDel.setStyleSheet("background: rgb(255, 100, 100)")
        self.btnDel.setObjectName("btnDel")
        self.verticalLayout.addWidget(self.groupbox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 581, 210))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tblAddress = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tblAddress.setObjectName("tblAddress")
        self.tblAddress.setColumnCount(0)
        self.tblAddress.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tblAddress)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stbCurrent = QtWidgets.QStatusBar(MainWindow)
        self.stbCurrent.setObjectName("stbCurrent")
        MainWindow.setStatusBar(self.stbCurrent)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupbox.setTitle(_translate("MainWindow", "정보입력"))
        self.btnNew.setText(_translate("MainWindow", "신규"))
        self.btnSave.setText(_translate("MainWindow", "저장"))
        self.label.setText(_translate("MainWindow", "이       름 :"))
        self.label_3.setText(_translate("MainWindow", "전화번호 :"))
        self.label_4.setText(_translate("MainWindow", " 이  메  일 :"))
        self.label_6.setText(_translate("MainWindow", "주       소 :"))
        self.btnDel.setText(_translate("MainWindow", "삭제"))
