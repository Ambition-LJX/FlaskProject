# 路由 + 视图函数
import datetime
import random

from flask import Blueprint, request, render_template, make_response,Response,redirect,session
from sqlalchemy import desc,and_,not_,or_,asc

from .models import *

# 蓝图
# user 蓝图名称
# __name__ 表示当前模块
blue=Blueprint('user',__name__)

# 路由可以写多个
@blue.route('/')
def index():
    return 'index'

# 多表操作

# 一对多
# 增加数据
@blue.route('/addgrade/')
def add_grade():
    # 添加班级
    grades=[]
    for i in range(10):
        grade=Grade()
        grade.name = f'Jay{i}-{str(random.randint(10,99))}'
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()
    return '班级创建成功!'

@blue.route('/addstu/')
def add_stu():
    # 添加学生
    students = []
    for i in range(10,20):
        stu = Student()
        stu.name = f'Lucy{i}'                   # 设置名字
        stu.age=i                               # 设置年龄
        stu.gradeId=random.randint(11,12)  # 设置gradeId
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()
    return '学生创建成功!'

# 修改
@blue.route('/updatestu/')
def update_stu():
    stu=Student.query.first()
    stu.age=100
    db.session.commit()

    return '修改成功!'

# 删除操作
@blue.route('/delstu/')
def del_stu():
    stu=Student.query.first()
    db.session.delete(stu)
    db.session.commit()

    return '删除成功!'

# 查询
@blue.route('/getstu/')
def get_stu():
    # 查询某个学生所在的班级 反向引用grade
    stu=Student.query.get(16)
    print(stu.name,stu.age)
    # 获取学生表对应的班级表的名称和编号
    print(stu.gradeId,stu.grade,stu.grade.name,stu.grade.id)

    # 查询某班级下的所有学生
    grade=Grade.query.get(11)
    print(grade.name)
    # print(grade.students)  # 所有学生
    for stu in grade.students:
        print(stu.name,stu.age)
    return '查询成功!'



