# -*- coding: utf-8 -*-
# @Time    : 2024-11-15 10:36
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : SocketOps.py
# @Software: PyCharm
from flask import request
from flask_socketio import leave_room

from app import socketio

name_space = '/dcenter'
client_threads = {}
connected_clients = {}  # 用于存储连接到房间的客户端信息

def emit_realtime_log(log, room, event_name='dcenter'):
    """
    通过 Socket.IO 发送实时日志
    :param log:  日志内容
    :param room:  房间名
    :param event_name:  事件名
    :return:
    """
    socketio.emit(event_name, {'data': log}, room=room)
@socketio.on('connect')
def connected_msg():
    """
    连接成功后的处理
    :return:
    """
    print('client connected.')
    return "Connected"

@socketio.on('disconnect')
def disconnect_msg():
    """
    断开连接后的处理
    :return:
    """
    print('client disconnected.')

    # 获取当前 Socket.IO 连接的唯一标识符（sid）
    sid = request.sid

    # 检查连接是否在 connected_clients 字典中
    if sid in connected_clients:
        room = connected_clients[sid]['room']

        # 离开房间
        leave_room(room)

        # 清理相关信息
        del connected_clients[sid]

        print('Left room:', room)

    # 设置标志为 False，通知线程终止
    if sid in client_threads:
        client_threads[sid]['active'] = False
        client_threads[sid]['thread'].join()  # 等待线程结束
        del client_threads[sid]
    return "client disconnected"