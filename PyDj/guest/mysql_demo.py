#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 16:18
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from pymysql import cursors, connect

# 连接数据库
conn = connect(host = '127.0.0.1',
               user = 'root',
               password = '',
               db = 'guest',
               charset = 'utf8mb4',
               cursorclass = cursors.DictCursor
               )

try:
    with conn.cursor() as cursor:
        # 创建嘉数据
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time) VALUES ("tom", 18800110002, "tom@mail.com", 0, 1, NOW());'
        cursor.execute(sql)
    conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = 'SELECT realname, phone, email, sign FROM sign_guest WHERE phone = %s'
        cursor.execute(sql, ('18800110002',))
        result = cursor.fetchone()
        print(result)

finally:
    conn.close()