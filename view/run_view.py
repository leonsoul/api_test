#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/10/12 17:27
# Filename:run_view.py
# Function: 操作功能页面
# ====#====#====#====
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.operation import Ui_MainWindow

class run_window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        """
        启动页类构造函数,初始化类属性等.
        """
        super(run_window,self).__init__()
        self.setupUi(self)
        self.init_solf()
    def init_solf(self):
        """
        初始化信号槽
        :return: 发送请求,清除数据
        """
        self.send.clicked.connect(lambda :self.on_click('send'))
        self.clEAr.clicked.connect(lambda :self.on_click('clEAr'))
    def on_click(self,tag):
        """
        操作提示
        :param tag: 按钮类型
        """
        if tag == 'send':
            pass
        elif tag == 'clEAr':
            self.Purge()
    def _comboxdemo(self):
        """
        下拉列表設置默認值展示
        :return: guituu
        """
        self.comboBox.setCurrentIndex(1)  #設置默認值
    def Purge(self):
        self.url.clear()
        self.args_map.clear()
        self.apiCount.clear()
        self.enMsg.clear()
        self.thread_Count.clear()
    def get_count(self):
        api = self.apiCount.text()
        thread = self.thread_Count.text()
        if api == '':
            if thread == '':
                return 1,1
            else:
                return 1,thread
        else:
            if thread == '':
                return api,1
            else:
                return api,thread
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = run_window()
    win.show()
    sys.exit(app.exec_())