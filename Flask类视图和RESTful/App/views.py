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
def index():
    return 'index'




