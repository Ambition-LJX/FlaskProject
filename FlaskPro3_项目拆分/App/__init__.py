# __init__ 初始化文件

from flask import Flask
# # 让view.py执行 .从当前包导入 相对
from .views import blue

def create_app():

    app3=Flask(__name__)

    # 注册蓝图
    app3.register_blueprint(blueprint=blue)

    return app3
