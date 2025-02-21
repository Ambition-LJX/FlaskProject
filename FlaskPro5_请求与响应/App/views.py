# 路由 + 视图函数

from flask import Blueprint, request, render_template, make_response,Response,redirect
from .models import *

# 蓝图
# user 蓝图名称
# __name__ 表示当前模块
blue=Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'

# 请求与响应
# http一次前后端交互: 先请求,后响应
@blue.route('/request/',methods=['GET','POST'])
def get_request():
    # print(request)

    # 重要属性
    print(request.method) # 请求方式 GET或POST

    # GET请求的参数
    print(request.args)
    print(request.args['name'],request.args['age'])
    print(request.args.get('name'))
    # 如果类字典对象中有多个key值相等 用下面的代码实现
    print(request.args.getlist('name'))

    #POST请求的参数
    print(request.form)
    print(request.form.get('name'))
    print(request.form.getlist('name'))

    #cookie
    print(request.cookies)

    # 路径
    print(request.path)  # /request/
    print(request.url)   # http://127.0.0.1:8081/request/?name=lisi&age=23
    print(request.base_url) # http://127.0.0.1:8081/request/
    print(request.host_url) # http://127.0.0.1:8081/
    print(request.remote_addr) # 127.0.0.1
    print(request.files) # 文件内容
    print(request.headers) # 请求头
    print(request.user_agent) # 用户代理，包括浏览器和操作系统的信息  反爬

    return 'request ok!'
# Response: 服务器端向客户端发送的响应
@blue.route('/response/',methods=['GET','POST'])
def get_response():

    # 响应的几种方式
    # 1.返回字符串 不常用
    # return 'response ok!'

    # 2.模版渲染（比较多） 前后端不分离
    # return render_template('index.html',name='张三',age=23)

    # 3.返回json数据 用于前后端分离
    # data={'name':'李四','age':23}
    # return data
    # jsonify序列化 字典转换成字符串
    # return jsonify(data)

    # 4.自定义响应response对象
    html=render_template('index.html',name='张三',age=23)
    print(html,type(html))

    # res=make_response(html,200)
    # 等价于下面的内容
    res=Response(html)
    return res

# Redirect: 重定向
@blue.route('/redirect/',methods=['GET','POST'])
def get_redirect():
    # 重定向的几种方式

    # 1.直接写网址
    return redirect("https://www.baidu.com/")

    # 2.路径
    return redirect("/response/")

    # 3.url_for('蓝图名称.视图函数') 反向解析 （可以传参给所给的视图函数的路由路径后面加上所给的参数）通过视图函数名找到所给的路由
    ret=url_for('user.get_request',name='李四',age=23)
    print('ret:',ret)
    return redirect(ret)
