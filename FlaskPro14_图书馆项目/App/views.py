# 路由 + 视图函数

from flask import Blueprint, render_template
from .models import *

# 蓝图
# user 蓝图名称
# __name__ 表示当前模块
blue=Blueprint('book',__name__)
# blue2=Blueprint('product',__name__)

@blue.route('/')
@blue.route('/bookindex/')
def book_index():
    return render_template('book_index.html')

@blue.route('/booklist/')
def book_list():
    books=Book.query.all()
    return render_template('book_list.html',books=books)

@blue.route('/bookdetail/<int:bid>/')
def book_detail(bid):
    book=Book.query.get(bid)
    return render_template('book_detail.html',book=book)

# 作者详情
@blue.route('/authordetail/<int:aid>/')
def author_detail(aid):
    author=Autor.query.get(aid)
    return render_template('author_detail.html',author=author)

# 出版社详情
@blue.route('/publisherdetail/<int:pid>/')
def publisher_detail(pid):
    publisher=Publisher.query.get(pid)
    return render_template('publisher_detail.html',publisher=publisher)
