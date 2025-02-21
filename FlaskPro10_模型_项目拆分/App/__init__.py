# __init__ 初始化文件
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# # 让view.py执行 .从当前包导入 相对
from .views import blue
from .exts import init_exts

def create_app():

    app3=Flask(__name__)

    # 注册蓝图
    app3.register_blueprint(blueprint=blue)

    # 配置数据库
    # 创建数据库的连接
    db_uri='sqlite:///sqlite3.db' # sqlite
    # db_uri='mysql+pymysql://root:123456@localhost:3306/flaskdb' # mysql
    app3.config['SQLALCHEMY_DATABASE_URI']=db_uri
    app3.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # 禁止对象追踪修改

    # 初始化插件
    init_exts(app=app3)

    return app3
