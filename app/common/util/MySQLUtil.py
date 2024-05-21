# -*- coding: utf-8 -*-
# @Time    : 2024-05-08 18:32
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : MySQLUtil.py
# @Software: PyCharm

import pymysql
from pymysql import OperationalError, InterfaceError


class DBUtil:
    def __init__(self, host, user_name, password, db_name):
        self.host = host
        self.user_name = user_name
        self.password = password
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()  # 在初始化时就连接数据库

    def connect(self):
        # 连接数据库
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user_name,
                password=self.password,
                database=self.db_name
            )
        except OperationalError as e:
            print(f"无法连接到数据库: {e}")

    def get_cursor(self):
        # 获取游标
        try:
            self.cursor = self.connection.cursor()
            return self.cursor
        except (AttributeError, OperationalError, InterfaceError) as e:
            self.reconnect()  # 重新连接
            self.cursor = self.connection.cursor()
            return self.cursor

    def reconnect(self):
        # 重新连接数据库
        try:
            self.connection.close()  # 关闭旧连接
        except:
            pass  # 忽略异常，避免连接已关闭时抛出异常
        self.connect()  # 重新连接

    def execute_sql(self, sql, params=None):
        # 执行SQL语句
        cursor = self.get_cursor()  # 获取游标
        try:
            cursor.execute(sql, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            self.connection.rollback()
            return False

    def fetch_all(self, sql):
        # 获取所有查询结果
        cursor = self.get_cursor()  # 获取游标
        try:
            cursor.execute(sql)
            self.close()  # 关闭连接，避免连接过多
            return cursor.fetchall()
        except (OperationalError, InterfaceError) as e:
            # print(f"连接断开，正在重新连接: {e}")
            self.reconnect()
            cursor = self.get_cursor()
            cursor.execute(sql)
            self.close()
            return cursor.fetchall()

    def close(self):
        # 关闭连接
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


# 使用示例
if __name__ == '__main__':
    db_util = DBUtil('192.168.102.20', 'root', '123456', 'auto_dev_hub')
    users = db_util.fetch_all("select * from sys_user")
    print(users)
    # db_util.close()
