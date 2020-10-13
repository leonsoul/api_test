#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/25 17:14
# Filename:start_window.py
# Function:启动页逻辑
# ====#====#====#====
import sys

from PyQt5.QtCore import Qt

from UI.start_page import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication

from view._login_view import login_window
from view.run_view import run_window


class staRT_PAGE(Ui_Form,QWidget):
    def __init__(self):
        """
        启动页类构造函数,初始化类属性等.
        """
        super(staRT_PAGE,self).__init__()
        self.setupUi(self)
        self._init_slot()
    def _init_slot(self):
        """
        初始化信号槽连接
        """
        self.login.clicked.connect(lambda: self.on_button_Click('register'))
        self.nologin.clicked.connect(lambda: self.on_button_Click('unenlist'))
    def on_button_Click(self,tag):
        """
        按钮点击事件槽函数
        :param tag: 点击的按钮的TAG
        :return: 出错返回,不执行后续操作逻辑
        """
        # 登录获取token
        # print(tag)
        if tag == 'register':
            # print('登录')
            self.log_main = login_window()
            self.log_main.show()
            self.shut()
        # 不需要登录直接操作
        if tag == 'unenlist':
            self.no_login = run_window()
            self.no_login.show()
            self.shut()
    def keyPressEvent(self, QKeyEvent):
        """
        监听键盘触发事件,通过判断是否按下的按键为Enter或者Return键
        :param QKeyEvent: 键盘触发事件
        """
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.login.click()
    def shut(self):   #被调用的类需要再编写一个close函数
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = staRT_PAGE()
    win.show()
    sys.exit(app.exec_())