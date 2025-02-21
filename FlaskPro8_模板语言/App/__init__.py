# __init__ 初始化文件
import datetime

from flask import Flask
# # 让view.py执行 .从当前包导入 相对
from .views import blue

def create_app():

    app3=Flask(__name__)

    # 注册蓝图
    app3.register_blueprint(blueprint=blue)

    # session配置
    print(app3.config) # flask配置信息
    '''
    
    '''
    app3.config['SECRET_KEY'] = 'abc123'
    # 设置session过期时间
    app3.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=31)
    return app3
