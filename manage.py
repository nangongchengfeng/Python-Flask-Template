# -*- coding: utf-8 -*-
# @Time    : 2024/5/2 12:01
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : manage.py
# @Software: PyCharm

import os
import sys

from apscheduler.schedulers.background import BackgroundScheduler

from app import create_app

# 默认为开发环境，按需求修改
config_name = 'development'

app = create_app(config_name)


# 数据库迁移

def start_scheduler():
    # 创建一个后台调度器
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(func=send_alert, trigger="interval", seconds=20)
    # 启动调度器
    scheduler.start()


if __name__ == '__main__':
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    base_dir = os.path.dirname(current_file)
    # 将项目目录添加到 sys.path
    if base_dir not in sys.path:
        sys.path.append(base_dir)

    # 启动定时任务
    if not app.debug or app.testing:
        start_scheduler()
    app.run(
        debug=True,  # 启用调试模式（仅限开发环境使用），支持热加载和详细的错误页面
        host='0.0.0.0',  # 监听所有网络接口，使局域网中的其他设备可以访问服务
        port=5000  # 设置服务运行的端口号为 5000
        # use_reloader=False,    # 禁用自动重载功能（默认启用自动重载） 会导致 scheduler 调度重复启动
        # threaded=True          # 启用多线程模式，支持并发处理多个请求
    )
