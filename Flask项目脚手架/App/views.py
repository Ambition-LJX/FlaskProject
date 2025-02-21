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


