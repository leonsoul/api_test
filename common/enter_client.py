#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/17 12:23
# Filename:login_client.py
# Function:
# ====#====#====#====
import requests
import time
from hashlib import md5
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Http_Client:
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate,br",
        "Accept-Language": "zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7",
        'cache-control': 'no-cache',
        "Content-type": "application/x-www-form-urlencoded",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    }
    @classmethod
    def report(cls,HTTP_METHOD,re_url,args_map):
        session = requests.session()
        session.headers = cls.header
        # args_map = json.dumps(args_map).encode("utf-8")
        if HTTP_METHOD == "POST":
            r =session.post(re_url,args_map)
        elif HTTP_METHOD =="GET":
            r = session.get(url=re_url)
        else:
            return
        return r
    @classmethod
    def sign_url(clazz,source,token,api_v,args_map):
        # timestamp = '1597564049772'
        timestamp = str(int(time.time() * 1000))  # 请求发起时间戳
        std_args_map = {"from": source, "timestamp": timestamp, "token": token, "version": api_v}
        # 把标准的四个参数组成的map和非标准参数args_map合并成一个map, 用来进行签名
        if args_map is None:
            validate_map = dict(std_args_map)
        else:
            validate_map = dict(std_args_map,**args_map)
        # 把所有参数按照参数名称进行字典序升序排序
        items = sorted(validate_map.items())
        validate_string_array = [value for key, value in items]
        # 把排好序的参数用 / 进行链接，并且在开始加上一个 "/"
        string_to_be_signatured = "/"
        string_to_be_signatured += "/".join(validate_string_array)
        # print(string_to_be_signatured)
        # 对签名字符串进行md5签名
        md5_generator = md5()
        md5_generator.update(string_to_be_signatured.encode('utf-8'))
        signature_generate = md5_generator.hexdigest()
        # print('线上：4849b5c4e1c0af37936fc83109ba5bfa')
        # print("测试："+signature_generate)
        signature_string = "v%s-%s-%s-%s-%s" % (source, timestamp, token, api_v, signature_generate)
        return signature_string
    @classmethod
    def request_url(cls,host,args_map):
        HTTP_METHOD = "POST"
        source ='0'
        token ='0'
        api_v ='0'
        bady = cls.sign_url(source,token,api_v,args_map)
        re_url = host + '/' + bady
        return cls.report(HTTP_METHOD=HTTP_METHOD,re_url=re_url,args_map=args_map),re_url