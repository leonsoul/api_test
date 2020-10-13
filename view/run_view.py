#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/10/12 17:27
# Filename:run_view.py
# Function: 操作功能页面
# ====#====#====#====
import json
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.operation import Ui_MainWindow
from common._util import toKEN


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
            res = self.api_request()
            if res == None:
                print('out')
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
                return '1','1'
            else:
                return '1',thread
        else:
            if thread == '':
                return api,'1'
            else:
                return api,thread
    def get_mag(self):
        """
        参数格式json
        :return:str转化为json
        """
        try:
            msg = self.args_map.toPlainText()
            msg_json = json.dumps(msg)
            return msg_json
        except:
            return None
    def get_enMsg(self,emsg):
        """
        获取校验enmsg
        :return:
        """
        try:
            msg = self.enMsg.text()
            if msg == '':
                return None
            else:
                enmsg = emsg.json()
                if enmsg['enMsg'] == msg:
                    return 'ok'
                else:
                    return 'out'
        except:
            return None
    def api_request(self):
        """
        接口发送请求
        """
        HTTP_METHOD = 'POST'
        api_v = '0'
        source = '1'
        try:
            url = self.url.text()
            if url == '':
                return None
            args_map = self.get_mag()
            if args_map == None:
                return None
            token = self.gettoken.text()
            if token == '':
                return None
            res = self.client.request_url(HTTP_METHOD, source, url, token, api_v, args_map)
            res_txt = res.text()
            verify = self.get_enMsg(res)
            if verify == None:
                return None
            else:
                return verify
        except:
            return None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = run_window()
    win.show()
    sys.exit(app.exec_())