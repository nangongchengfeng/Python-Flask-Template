# -*- coding: utf-8 -*-
# @Time    : 2024/5/3 10:22
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : authMiddleware.py
# @Software: PyCharm
import itsdangerous
from flask import g, request
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer

from app.common.result.code import get_message
from app.common.result.result import Result
from app.common.util.LogHandler import log
from app.config import secret_key
from app.api.dao.sysUser import GetSysUserName

s = TimedJSONWebSignatureSerializer(secret_key, expires_in=28800)
auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token):
    # 从请求头中获取 Authorization 字段
    auth_header = request.headers.get('Authorization')

    # 如果没有 Authorization 头字段，则 token 为 None
    if not auth_header:
        log.error("【login】 token 参数不存在！")
        return False
    # 提取 token 部分
    token = auth_header.split(' ')[1]
    if token:
        try:
            data = s.loads(token)
        except itsdangerous.SignatureExpired:
            log.error("认证异常: 令牌已过期")
            return False
        except itsdangerous.BadSignature:
            log.error("认证异常: 令牌签名无效")
            return False
        except Exception as e:
            log.error(f"认证异常: {e}")
            return False
        g.username = data
        user = GetSysUserName(data)
        g.namespace = user.namespace
        g.user = user
        g.userid = user.id
        return True


@auth.error_handler
def unauthorized():
    # 获取客户端 IP
    client_ip = request.remote_addr
    # 获取 User-Agent
    user_agent = request.headers.get('User-Agent', 'Unknown User-Agent')
    # 获取请求路径
    request_path = request.path
    # 获取请求方法（GET, POST, ...）
    request_method = request.method
    log.error(f"【login】 {client_ip} - {user_agent} - {request_method} - {request_path} - 403：认证异常，请重新登录！")
    return Result.failed(407, get_message(407))
