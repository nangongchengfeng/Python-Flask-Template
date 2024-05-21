# -*- coding: utf-8 -*-
# @Time    : 2024/5/2 12:05
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : result.py
# @Software: PyCharm
from flask import jsonify


class Result:
    def __init__(self, code, msg, data=None):
        self.code = code
        self.msg = msg
        self.data = data if data is not None else {}

    @staticmethod  # 添加这个装饰器
    def success(data=None):
        """成功响应"""
        return jsonify(Result(200, "操作成功", data).__dict__).get_json()

    @staticmethod  # 添加这个装饰器
    def failed(code, message):
        """失败响应"""
        return jsonify(Result(code, message).__dict__).get_json()

# if __name__ == "__main__":
# with app.app_context():
#     success_response = Result.success({'some_key': 'some_value'})
#     failed_response = Result.failed(501, "操作失败")
#
#     print(success_response)  # 获取 JSON 数据
#     print(failed_response)  # 获取 JSON 数据
