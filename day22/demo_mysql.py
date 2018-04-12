#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import mysql.connector


conn = mysql.connector.connect(user='root', password='root', database='test', port=8889)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) PRIMARY KEY , NAME VARCHAR(20))')
cursor.execute('insert into user (id, name) VALUES (%s, %s)', ['1', 'Michael'])
cursor.rowcount
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values
[('1', 'Michael')]
cursor.close()
conn.close()