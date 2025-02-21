# 路由 + 视图函数
import datetime

from flask import Blueprint, request, render_template, make_response,Response,redirect,session
from .models import *

# 蓝图
# user 蓝图名称
# __name__ 表示当前模块
blue=Blueprint('user',__name__)

# 路由可以写多个
@blue.route('/')
@blue.route('/home/')
def home():
    # # 4.获取cookie
    # username=request.cookies.get('user')

    # 获取session
    username=session.get('user')

    return render_template('home.html',username=username)

# 会话技术
# 登录
@blue.route('/login/',methods=['GET','POST'])
def login():
    # GET:访问登录页面
    if request.method == 'GET':
        return render_template('login.html')
    # POST:实现登录功能
    elif request.method == 'POST':
        # 1.获取前端提交过来的数据
        username=request.form.get('username')
        password=request.form.get('password')
        # 2.模拟登录功能
        if username == 'admin1' and password == '123':
            # 登录成功
            response=redirect('/home/')
            # 设置session
            session['user']=username
            # 设置有效性
            session.permanent = True
            return response
        else:
            return '用户名或密码错误'
# 注销
@blue.route('/logout/')
def logout():

    response=redirect('/home/')

    # 删除session 谨慎使用 因为他会删除服务器下的所有session
    session.clear()

    # session.pop('user') # 删除单个链接

    return response



