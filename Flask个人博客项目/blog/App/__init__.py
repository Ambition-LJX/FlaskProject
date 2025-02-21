# __init__ 初始化文件

from flask import Flask
# # 让view.py执行 .从当前包导入 相对
from .views.views import blog
from .views.views_admin import admin
from .exts import *

def create_app():
    app = Flask(__name__)
    # 注册蓝图
    app.register_blueprint(blueprint=blog)  # 博客的前端页面
    app.register_blueprint(blueprint=admin) # 后台管理系统

    # 配置数据库
    # 创建数据库的连接
    db_uri='mysql+pymysql://root:123456@localhost:3306/blogdb' # mysql
    app.config['SQLALCHEMY_DATABASE_URI']=db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # 禁止对象追踪修改

    # 初始化插件
    init_exts(app=app)

    return app
