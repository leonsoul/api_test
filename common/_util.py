#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/25 17:54
# Filename:_util.py
# Function: 基础配置等
# ====#====#====#====
import hashlib

from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtGui

import frozen_dir
SUPER_DIR = frozen_dir.app_path()
Home = SUPER_DIR + '\img\home.ico'
Responses = SUPER_DIR + '\img\\result.ico'
History_LOG = SUPER_DIR + '\img\\txt_log.ico'
toast_logo = SUPER_DIR + '\img\\tips.ico'
start_bj = SUPER_DIR + '\img\\bg.jpg'
log_txt = SUPER_DIR + '\log\log.txt'
toKEN = SUPER_DIR + '\log\\toKEN.txt'
# print(log_txt)


def get_md5(data):
    """
    获取md5加密密文
    :param data: 明文
    :return: 加密后的密文
    """
    m = hashlib.md5()
    b = data.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()
def get_phone(data):
    """
    校验手机号
    :param data: 手机号
    :return: 手机号长度正确
    """
    try:
        if len(data) == 11:
            return data
        else:
            return None
    except:
        return None
def args_map(user,data):
    """
    前端数据转换josn
    :param name:
    :param data:
    :return:
    """
    name = get_phone(user)
    pwd = get_md5(data)
    try:
        return {
            "name": name,
            "pwd": pwd
        }
    except:
        return None
def msg_box(title, msg):
    """提示框 """
    QMessageBox.warning(title, msg,QMessageBox.Yes)
    QMessageBox.setWindowIcon(QtGui.QIcon(toast_logo))