#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/25 16:29
# Filename:test_db.py
# Function:acc数据库连接操作
# ====#====#====#====
import pyodbc
import pyodbc

DBfile = r"test.mdb"  # 数据库文件
conn = pyodbc.connect(r"Driver={Driver do Microsoft Access (*.mdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")

cursor = conn.cursor()
SQL = "SELECT * from MFRProcess;"
for row in cursor.execute(SQL):
    print( row  )
cursor.close()
conn.close()
