# 路由 + 视图函数


from flask import Blueprint, request, render_template, g, current_app
from .exts import cache
import time

# 蓝图
# user 蓝图名称
# __name__ 表示当前模块
blue=Blueprint('user',__name__)
# blue2=Blueprint('product',__name__)

# 使用缓存
@blue.route('/')
@cache.cached(timeout=20) # 给视图函数加一个缓存20s
def index():
    print('index2')
    print('index视图函数中:',g.star)
    time.sleep(5)
    return 'index2'

# AOP: 切面编程
# 钩子函数
# 也叫中间件
# 在每一次请求之前访问
@blue.before_request
def before():
    print('before_request')
    # request
    # print(request.path)
    # print(request.method)
    # print(request.remote_addr) # 客户端ip地址

    # --------------------------------
    # # 简单的反爬
    # print(request.user_agent) # python-requests/2.32.3
    #
    # if "python" in request.user_agent.string:
    #     return '您正在使用python爬虫,再见！'
    # --------------------------------

    #--------------------------------
    # 针对IP做反爬(简单)
    # ip=request.remote_addr
    # cache.get()
    # cache.set()
    # cache.set(ip,'value',timeout=1)
    # if cache.get(ip):
    #     # 做了拦截,不会进入视图函数
    #     return '小伙子,别爬了！'
    # else:
    #     # 对每个IP设置一个缓存,1秒内不让重复访问
    #     cache.set(ip,'value',timeout=1)
    # --------------------------------

    #-------------------------------
    # Flask内置对象
    # request 请求对象
    # session 会话
    # g global全局对象
    # current_app: Flask应用对象
    g.star='杰伦'
    print(g.star)
    print(current_app)  # <Flask 'App'>
    print(current_app.config) # <Config {'DEBUG': True, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None,
    # --------------------------------

# static和templates
@blue.route('/template/')
def templates():
    return render_template('template.html')



