#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/25 18:45
# Filename:_login_view.py
# Function: 选择登录获取token
# ====#====#====#====
import sys
import time

from PyQt5.QtCore import Qt

from UI.login_page import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from common._util import args_map, log_txt,toKEN
from common.enter_client import Http_Client
from view.run_view import run_window




class login_window(Ui_Form,QWidget):
    def __init__(self):
        """
        启动页类构造函数,初始化类属性等.
        """
        super(login_window,self).__init__()
        self.setupUi(self)
        self.init_slot()
        self.guituu.setChecked(True)
    def init_slot(self):
        """
        初始化信号槽
        """
        self.pushButton.clicked.connect(lambda:self.click_on('send'))
    def click_on(self,tag):
        """
        操作提示
        :param tag: 按钮类型
        """
        if tag == 'send':
            mold = self.get_text()
            if mold == None:
                self.msg_box('提示','输入信息不完整。。。')
            elif mold == 'req_out':
                self.msg_box('提示','输入有误,请求失败。。。')
            else:
                i = self.get_host()
                self.data_main = run_window()
                self.data_main.show()
                self.shut()
                self.data_main.gettoken.setText(mold)
                self.data_main._comboxdemo(int(i))
    def get_host(self):
        try:
            if self.guituu.isChecked() == True:
                return '1'
                # host = 'https://m.guituu.com/rest/v3/login'
            elif self.alltuu.isChecked() == True:
                # host = 'https://am.alltuu.com/rest/v3/login'
                return '2'
        except:
            return None
    def get_text(self):
        try:
            host = self.get_host()
            if host == '1':
                url = 'https://m.guituu.com/rest/v3/login'
            elif host == '2':
                url = 'https://am.alltuu.com/rest/v3/login'
            get_phone = self.phone.text()
            get_pwd = self.pasw.text()
            if get_phone == '' or get_pwd == '' :
                return None
            else:
                try:
                    data = args_map(get_phone,get_pwd)
                    req = self._url_report(url,data)
                    if req == None:
                        return 'req_out'
                    else:
                        return req
                except:
                    pass
                return 'ok'
        except Exception as e:
            return None
    def keyPressEvent(self, QKeyEvent):
        """
        监听键盘触发事件,通过判断是否按下的按键为Enter或者Return键
        :param QKeyEvent: 键盘触发事件
        """
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.pushButton.click()
    def _url_report(self,get_host, data):
        """
        發送請求
        :param get_host: url
        :param data: 请求数据josn
        :return: ok、None
        """
        data_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        try:
            HTTP_METHOD = "POST"
            source = '0'
            token = '0'
            api_v = '0'
            req,url = Http_Client().request_url(HTTP_METHOD,source,token,api_v,get_host, data)
            YH_token = req.json()
            url_token = YH_token['data']['token']
            # print(url_token)
            pc_token = YH_token['data']['obj']['pcToken']
            # print(pc_token)
            write_txt = {
                "time": data_time,
                "token": url_token,
                "PCtoken": pc_token,
                "URL":url
            }
            with open(log_txt, "a+") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                    file.write(str(write_txt) + "\n")
            return url_token
        except:
            return None
    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()
    def shut(self):   #被调用的类需要再编写一个close函数
        self.close()

    def msg_box(self,title, msg):
        """提示框 """
        QMessageBox.warning(self,title, msg, QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = login_window()
    win.show()
    sys.exit(app.exec_())
