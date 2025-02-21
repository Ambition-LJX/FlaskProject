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
def home():
    pass

    data={
        'name':'ikun ikun ikun',
        'age':22,
        'likes':['ball','sing','dance','code']
    }

    # return render_template('home.html',**data)
    # return render_template('home.html',name='ikun',age=22,like=['ball','sing','dance','code'])
    # return render_template('base.html')
    return render_template('child2.html',**data)




