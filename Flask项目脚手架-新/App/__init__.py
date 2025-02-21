# __init__ 初始化文件

from flask import Flask
# # 让view.py执行 .从当前包导入 相对
from .views import blue
from .exts import init_exts
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR:',BASE_DIR) # 项目目录

def create_app():

    # 配置静态文件和模版文件目录
    # static_folder = '../static'
    # template_folder = '../templates'
    static_folder = os.path.join(BASE_DIR, 'static')
    template_folder = os.path.join(BASE_DIR, 'templates')
    app3=Flask(__name__,static_folder=static_folder,template_folder=template_folder)

    # 注册蓝图
    app3.register_blueprint(blueprint=blue)

    # 配置数据库
    # 创建数据库的连接
    # db_uri='sqlite:///sqlite3.db' # sqlite
    db_uri='mysql+pymysql://root:123456@localhost:3306/flaskdb3' # mysql
    app3.config['SQLALCHEMY_DATABASE_URI']=db_uri
    app3.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # 禁止对象追踪修改

    # 初始化插件
    init_exts(app=app3)

    return app3

