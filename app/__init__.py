# -*- coding: utf-8 -*-
# @Time    : 2024-05-21 09:41
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : __init__.py.py
# @Software: PyCharm

from apscheduler.schedulers.background import BackgroundScheduler
from flasgger import Swagger
from flask_cors import CORS
from flask_migrate import Migrate

from app.config import config
from app.extension import db

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger_template = {
    "securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}},
    "info": {
        "description": "Python Flask Template API 文档",
        "version": "1.0.0",
        "title": "API 文档",
        "termsOfService": "https://github.com/nangongchengfeng/Python-Flask-Template.git",
        "contact": {
            "email": "1794748404@qq.com",
            "name": "南宫乘风",
            "url": "https://github.com/nangongchengfeng"
        },
        "license": {
            "name": "MIT",
            "url": "https://github.com/nangongchengfeng/Python-Flask-Template.git"
        }
    }
}


def create_app(DevelopmentConfig=None):
    if DevelopmentConfig is None:
        DevelopmentConfig = 'development'
    from flask import Flask

    app = Flask(__name__)
    from app.extension import config_extensions

    # 加载配置项
    app.config.from_object(config.get(DevelopmentConfig))
    from app.api import config_blueprint
    config_blueprint(app)
    config_extensions(app)

    migrate = Migrate(app, db)
    Swagger(app, config=swagger_config, template=swagger_template)

    # 非nginx调试，解决跨域CORS问题，一种为全局使用, supports_credentials=True
    CORS(app, rresources={r'/*': {'origins': '*'}}, supports_credentials=True)
    # socket 的信息
    # 创建一个后台调度器
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(func=send_alert, trigger="interval", seconds=20)
    # 启动调度器
    scheduler.start()
    return app
