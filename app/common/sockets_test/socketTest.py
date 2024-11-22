
from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdef"
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


def background_task():
    """后台任务：每5秒查询一次数据并发送给前端"""
    while True:
        # 模拟数据查询 {'register_count': 791, 'last_register_time': '2024-11-22 09:14:00', 'last_login_time': '2024-11-22 09:13:49', 'last_realname_time': '2024-11-22 09:13:31', 'last_ocr_time': '2024-11-22 09:13:31', 'last_apply_time': '2024-11-22 09:13:33', 'last_withdraw_time': '2024-11-22 09:12:04', 'last_wechatpay_time': '2024-11-22 09:10:05', 'last_repayment_time': '2024-11-22 09:11:57', 'bing_card_time': '2024-11-22 09:09:35'}

        combined_data = {}
        print(f"数据库查询结果返回：{combined_data}")
        socketio.emit("response_data", {"data": combined_data}, namespace="/ws")
        socketio.sleep(5)  # 每5秒推送一次数据

# 主动推送模拟的实时数据
@socketio.on("connect", namespace="/ws")
def connect():
    print("客户端已连接")
    socketio.emit("connect_response", {"data": "连接成功，欢迎使用 WebSocket 技术！"}, namespace="/ws")

@socketio.on("disconnect", namespace="/ws")
def disconnect():
    print("客户端已断开连接")
@socketio.on("request_data", namespace="/ws")
def send_combined_data():
    # while True:
        # 从数据库中获取数据
    combined_data = {'register_count': 791, 'last_register_time': '2024-11-22 09:14:00', 'last_login_time': '2024-11-22 09:13:49', 'last_realname_time': '2024-11-22 09:13:31', 'last_ocr_time': '2024-11-22 09:13:31', 'last_apply_time': '2024-11-22 09:13:33', 'last_withdraw_time': '2024-11-22 09:12:04', 'last_wechatpay_time': '2024-11-22 09:10:05', 'last_repayment_time': '2024-11-22 09:11:57', 'bing_card_time': '2024-11-22 09:09:35'}

    print(f"数据库查询结果返回：{combined_data}")
    # 使用 WebSocket 向前端发送数据
    emit("response_data", {"data": combined_data}, namespace="/ws")
    # socketio.sleep(30)  # 每5秒推送一次数据


if __name__ == '__main__':
    socketio.run(app, debug=True)
