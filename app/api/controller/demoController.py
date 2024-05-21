# -*- coding: utf-8 -*-
# @Time    : 2024-05-21 10:21
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : demoController.py
# @Software: PyCharm
from flasgger import swag_from
from flask import Blueprint, request

from app.common.result.result import Result

app = Blueprint('app', __name__)


@swag_from({
    'tags': ['首页管理'],
    'description': '获取首页数据接口。',
    'parameters': [],
    'responses': {
        200: {
            'description': '操作成功',
            'examples': {
                'application/json': {
                    "code": 200,
                    "msg": "操作成功",
                    "data": {}
                }
            }
        },
    },
    'security': [
        {
            'APIKeyHeader': []
        }
    ]
})
@app.route("/get", methods=['GET'])
def index():

    return  Result.success()

@app.route("/post", methods=['POST'])
@swag_from({
    'tags': ['首页管理'],
    'description': '示例 POST 请求接口。',
    'parameters': [
        {
            'name': 'param1',
            'in': 'formData',
            'description': '参数1',
            'type': 'string',
            'required': True
        },
        {
            'name': 'param2',
            'in': 'formData',
            'description': '参数2',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': '操作成功',
            'examples': {
                'application/json': {
                    "code": 200,
                    "msg": "操作成功",
                    "data": {}
                }
            }
        },
    },
    'security': [
        {
            'APIKeyHeader': []
        }
    ]
})
def post_example():
    param1 = request.form.get('param1')
    param2 = int(request.form.get('param2'))
    # 处理 POST 请求的逻辑
    return  Result.success({"param1": param1, "param2": param2})


@app.route("/put", methods=['PUT'])
@swag_from({
    'tags': ['首页管理'],
    'description': '示例 PUT 请求接口。',
    'parameters': [
        {
            'name': 'param1',
            'in': 'formData',
            'description': '参数1',
            'type': 'string',
            'required': True
        },
        {
            'name': 'param2',
            'in': 'formData',
            'description': '参数2',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': '操作成功',
            'examples': {
                'application/json': {
                    "code": 200,
                    "msg": "操作成功",
                    "data": {}
                }
            }
        },
    },
    'security': [
        {
            'APIKeyHeader': []
        }
    ]
})
def put_example():
    param1 = request.form.get('param1')
    param2 = int(request.form.get('param2'))
    # 处理 PUT 请求的逻辑
    return Result.success({"param1": param1, "param2": param2})


@app.route("/delete", methods=['DELETE'])
@swag_from({
    'tags': ['首页管理'],
    'description': '示例 DELETE 请求接口。',
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'description': 'ID',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': '操作成功',
            'examples': {
                'application/json': {
                    "code": 200,
                    "msg": "操作成功",
                    "data": {}
                }
            }
        },
    },
    'security': [
        {
            'APIKeyHeader': []
        }
    ]
})
def delete_example():
    id = int(request.args.get('id'))
    # 处理 DELETE 请求的逻辑

    return Result.success({"id": id})