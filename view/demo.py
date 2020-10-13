#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/10/13 18:41
# Filename:demo.py
# Function:
# ====#====#====#====
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
import sys

#DateDailog窗口类先定义好
class DateDialog(QDialog):
    signal=pyqtSignal(str)

    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle("QDateDialog")

        layout=QVBoxLayout()
        self.datetime=QDateTimeEdit()
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        self.datetime1 = QDateTimeEdit()
        self.datetime1.setCalendarPopup(True)
        self.datetime1.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)
        layout.addWidget(self.datetime1)

        button=QDialogButtonBox(QDialogButtonBox.Ok |QDialogButtonBox.Cancel)
        button.accepted.connect(self.accept)    #关联系统接受方法
        button.rejected.connect(self.reject)    #关联系统拒绝方法

        self.datetime1.dateTimeChanged.connect(self.emit1)
        layout.addWidget(button)
        self.setLayout(layout)

    def dateTime(self):
        return self.datetime.dateTime()  #获取到当前的日期和时间

   #触发信号函数
    def emit1(self):
        d=self.datetime1.dateTime().toString()
        self.signal.emit(d)

    #定义一个静态方法
    @staticmethod
    def getdatetime(parent=None):
        dailog=DateDialog(parent)
        #显示这个窗口
        result=dailog.exec() #显示窗口的状态，接收或者不接受
        date=dailog.dateTime()
        return (date.date(),date.time(),result==QDialog.Accepted)

class Mulwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("多窗口交互：不使用信号与槽函数")

        self.line=QLineEdit(self)
        self.b1=QPushButton("弹出对话框1")
        self.b1.clicked.connect(self.onb1)
        self.b2=QPushButton("弹出对话框2")
        self.b2.clicked.connect(self.onb2)

        g=QGridLayout()
        g.addWidget(self.line)
        g.addWidget(self.b1)
        g.addWidget(self.b2)
        self.setLayout(g)

    def onb1(self):
        dialog=DateDialog(self)
        result=dialog.exec() #先要显示第一个窗口
        date=dialog.dateTime()
        self.line.setText(date.date().toString())  #显示出来日期,转为字符串
        dialog.destroy()  #销毁窗口

    def onb2(self):

        date,time,result=DateDialog.getdatetime()
        self.line.setText(date.toString())

        if result==QDialog.Accepted:   #如果点击接受方法
            print("点击确定按钮")
        else:                          #如果点击拒绝方法
            print("点击取消按钮")

if __name__=="__main__":
    app=QApplication(sys.argv)
    p=Mulwindow()
    p.show()
    sys.exit(app.exec_())