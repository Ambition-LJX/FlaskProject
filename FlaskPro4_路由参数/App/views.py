# 路由 + 视图函数

from flask import Blueprint
from .models import *

# 蓝图
# user 蓝图名称
# __name__ 表示当前模块
blue=Blueprint('user',__name__)
# blue2=Blueprint('product',__name__)

@blue.route('/')
def index():
    return 'index'

# 路由参数
# string
@blue.route('/string/<string:name>/')  #或者直接写<name>
def get_string(name):
    print(type(name))
    return name

@blue.route('/int/<int:id>/')  #或者直接写<name>
def get_int(id):
    print(type(id))
    return str(id)

@blue.route('/float/<float:money>/')
def get_float(money):
    print(type(money))
    return str(money)

# path: 支持/的字符串
@blue.route('/path/<path:name>/')
def get_path(name):
    print(type(name))
    return str(name)

# uuid 需要传uuid格式的变量值
@blue.route('/uuid/<uuid:id>/')
def get_uuid(id):
    print(type(id))
    return str(id)

# 生成一个uuid类型的随机数
@blue.route('/getuuid/')
def get_uuid2():
    import uuid
    return str(uuid.uuid4())

#any: 从列出的项目中选择一个
@blue.route('/any/<any(apple,orange,banana):fruit>/')
def get_any(fruit):
    print(type(fruit))
    return str(fruit)

# methods:请求方式
@blue.route('/methods/',methods=['GET','POST'])
def get_methods():
    return str('methods')

# @blue2.route('/goods/')
# def index():
#     return 'index'
