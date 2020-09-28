# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from common._util import start_bj, Home


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 220)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(30, 150, 90, 40))
        self.login.setObjectName("login")
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.login.setFont(font)
        self.nologin = QtWidgets.QPushButton(Form)
        self.nologin.setGeometry(QtCore.QRect(180, 150, 90, 40))
        self.nologin.setObjectName("nologin")
        self.nologin.setFont(font)
        self.tips = QtWidgets.QLabel(Form)
        self.tips.setGeometry(QtCore.QRect(30, 20, 270, 60))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tips.setFont(font)
        self.tips.setObjectName("tips")
        self.logintxt = QtWidgets.QLabel(Form)
        self.logintxt.setGeometry(QtCore.QRect(40, 80, 240, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.logintxt.setFont(font)
        self.logintxt.setObjectName("logintxt")
        self.notxt = QtWidgets.QLabel(Form)
        self.notxt.setGeometry(QtCore.QRect(40, 110, 240, 30))
        self.notxt.setFont(font)
        self.notxt.setObjectName("notxt")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 220))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(start_bj))
        self.label.setObjectName("label")
        self.label.raise_()
        self.login.raise_()
        self.nologin.raise_()
        self.tips.raise_()
        self.logintxt.raise_()
        self.notxt.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "启动页"))
        Form.setWindowIcon(QtGui.QIcon(Home))  # 设置icon
        self.login.setText(_translate("Form", "登  陆"))
        self.nologin.setText(_translate("Form", "不用登陆"))
        self.tips.setText(_translate("Form", "接口测试工具"))
        self.logintxt.setText(_translate("Form", "登    陆：没token，需要获取；"))
        self.notxt.setText(_translate("Form", "不用登陆：有token，直接操作；"))
