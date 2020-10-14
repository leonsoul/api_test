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
import threading
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

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
<<<<<<< HEAD
            res = self.get_count()
            if res == None:
                self.msg_box('提示', '输入有误、请求失败。。。')
            else:
                pass        elif tag == 'clEAr':
=======
            res = self.api_request()
            if res == None:
                print('out')
        elif tag == 'clEAr':
>>>>>>> 8c30151366d88bef21ca7ea2a189629cce382852
            self.Purge()
            self.msg_box('提示', '清除完成。。。')
    def _comboxdemo(self,i):
        """
        下拉列表設置默認值展示
        :return: guituu
        """
        self.comboBox.setCurrentIndex(i)  #設置默認值
    def Purge(self):
        self.url.clear()
        self.args_map.clear()
        self.apiCount.clear()
        self.enMsg.clear()
        self.thread_Count.clear()
    def get_count(self):
        """
        获取前端线程数，循环数
        :return:
        """
        api = self.apiCount.text()
        thread = self.thread_Count.text()
        if api == '':
            if thread == '':
<<<<<<< HEAD
                self.more(1,1)
            else:
                self.more(thread,1)
        else:
            if thread == '':
                self.more(1,api)
            else:
                self.more(thread,api)
    def more(self,THREAD_NUM,ONE_WORKER_NUM):
        """
        线程运行
        :param THREAD_NUM: 线程数
        :param ONE_WORKER_NUM: 每个线程运行时间
        :return:
        """
        t1 = time.time()
        Threads = []
        for i in range(THREAD_NUM):
            t = threading.Thread(target=self.working(ONE_WORKER_NUM), name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)
        for t in Threads:
            t.start()
        for t in Threads:
            t.join()
        t2 = time.time()
    def working(self,ONE_WORKER_NUM):
        """
        每个线程循环数
        :param ONE_WORKER_NUM:  循环数
        :return:
        """
        t = threading.currentThread()
        i = 0
        while i < ONE_WORKER_NUM:
            i +=1
            self.api_request()
            time.sleep(0.1)
    def get_mag(self):
        """
        参数格式json
        :return:str转化为json
        """
        try:
            msg = self.args_map.toPlainText()
            # msg = {
            #     "orderIdN": "4050eaa958dd087f",
            #     "schemeIdN": "a6032be88d26a11f",
            #     "type": '0'
            # }
            msg_json = json.dumps(msg)
            return msg_json
        except:
            return None
    def get_enMsg(self,emsg):
        """
        获取校验enmsg
        """
        try:
            msg = self.enMsg.text()
            if msg == '':
                return 'null'
            else:
                return msg
        except:
            return None
    def api_request(self):
        """
        接口发送请求
        """
        global win_NUM, ERROR_NUM
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
            print(res_txt)
            verify = self.get_enMsg(res)
            if verify == 'null':
                return 'null'
            else:
                enmsg = res.json()
                if enmsg['enMsg'] == verify:
                    return 'ok'
                    win_NUM += 1
                else:
                    return 'out'
                    ERROR_NUM += 1
        except:
            return None
    def msg_box(self,title, msg):
        """提示框 """
        QMessageBox.warning(self,title, msg, QMessageBox.Yes)



=======
                return '1','1'
            else:
                return '1',thread
        else:
            if thread == '':
                return api,'1'
            else:
                return api,thread
>>>>>>> 8c30151366d88bef21ca7ea2a189629cce382852
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
    # win.get_mag()