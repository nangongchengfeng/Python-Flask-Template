# -*- coding: utf-8 -*-
# @Time    : 2024/5/2 12:03
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : extension.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 初始化拓展
def config_extensions(app):
    db.init_app(app)



