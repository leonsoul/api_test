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
from common.enter_client import Http_Client


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
            TEXT_data = self.get_text()
            print(TEXT_data)
            if TEXT_data == None:
                self.msg_box('提示','输入信息不完整')
            else:
                self.get_count()
        elif tag == 'clEAr':
            self.Purge()
            self.msg_box('提示', '清除完成。。。')
    def _comboxdemo(self,i):
        """
        下拉列表設置默認值展示
        :return: guituu
        """
        self.comboBox.setCurrentIndex(i)  #設置默認值
    def Purge(self):
        '''
        输入框清除
        '''
        self.url.clear()
        self.args_map.clear()
        self.apiCount.clear()
        self.enMsg.clear()
        self.thread_Count.clear()
    def get_text(self):
        url = self.url.text()
        if url == '':
            return None
        msg = self.args_map.toPlainText()
        if msg == '':
            return None
        else:
            try:
                msg_data = msg.replace('\n', '').replace(' ', '')
                data = json.loads(msg_data)
            except:
                return None
        token = self.gettoken.text()
        if token == '':
            return None
        # return 'ok'
        return self.api_request(url,data,token)
    def get_count(self):
        """
        获取前端线程数，循环数
        :return:
        """
        api = self.apiCount.text()
        thread = self.thread_Count.text()
        if api == '':
            if thread == '':
                self.more(1,1)
            else:
                self.more(int(thread),1)
        else:
            if thread == '':
                self.more(1,int(api))
            else:
                self.more(int(thread),int(api))
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
        print("===============压测结果===================")
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM,"=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", error_NUM)
        print("成功数量:", win_NUM)
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
            self.get_text()
            time.sleep(0.1)
    def api_request(self,get_host,data,token):
        """
        接口发送请求
        """
        global win_NUM,error_NUM
        try:
            HTTP_METHOD = "POST"
            source = '0'
            api_v = '0'
            req, url = Http_Client().request_url(HTTP_METHOD, source, token, api_v, get_host, data)
            res_txt = req.text
            verify = self.get_enMsg(req)
            if req.status_code() == 200:
                win_NUM += 1
                # return 'ok'
            else:
                error_NUM += 1
                # return None
        except:
            error_NUM +=1
            # return None
    def msg_box(self,title, msg):
        """提示框 """
        QMessageBox.warning(self,title, msg, QMessageBox.Yes)
    def get_enMsg(self,emsg):
        """
        获取校验enmsg
        :return:
        """
        try:
            msg = self.enMsg.text()
            if msg == '':
                return 'null'
            else:
                enmsg = emsg.json()
                if enmsg['enMsg'] == msg:
                    return 'ok'
                else:
                    return 'out'
        except:
            return None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = run_window()
    win.show()
    sys.exit(app.exec_())
    # {
    #     "name":"15191333567",
    #     "pwd":"25d55ad283aa400af464c76d713c07ad"
    # }