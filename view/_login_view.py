#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/25 18:45
# Filename:_login_view.py
# Function: 选择登录获取token
# ====#====#====#====
import sys
from UI.login_page import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget


class login_window(Ui_Form,QWidget):
    def __init__(self):
        """
        启动页类构造函数,初始化类属性等.
        """
        super(login_window,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = login_window()
    win.show()
    sys.exit(app.exec_())
