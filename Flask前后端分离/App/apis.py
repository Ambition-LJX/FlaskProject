from flask import jsonify
from flask_restful import Resource,fields,marshal_with,reqparse
from fontTools.designspaceLib.types import locationInRegion

from .models import *
# 类视图: CBV class Based View
# 视图函数: FBV Function Based View

class HelloResource(Resource):
    def get(self):
        return jsonify({'msg':'get请求'})

    def post(self):
        return jsonify({'msg':'post请求'})


# -----------------字段格式化--------------------------
# Flask-RESTful
# 字段格式化:定义返回给前端的数据格式
ret_fields={
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.String,
    'like': fields.String(default='ball'),
    'like2': fields.String(),
    'data2': fields.String(attribute='data') # 使用data的值
}
class UserResource(Resource):
    @marshal_with(ret_fields)
    def get(self):
        return {
            'status': 1,
            'msg': 'ok',
            'data': '123'
        }





user_fields={
    # 'id':fields.Integer,
    'name':fields.String,
    'age':fields.Integer,

    'url':fields.Url(endpoint='id',absolute=True) # 绝对路径
}
ret_fields2={
    'status': fields.Integer,
    'msg': fields.String,
    # user对象
    'data': fields.Nested(user_fields)
}
class UserResource2(Resource):
    @marshal_with(ret_fields2)
    def get(self):
        user=User.query.first()
        return {
            'status': 1,
            'msg': 'ok',
            'data': user
        }

# -----------------字段格式化--------------------------
user_fields2={
    # 'id':fields.Integer,
    'name':fields.String,
    'age':fields.Integer,

    'url':fields.Url(endpoint='id',absolute=True) # 绝对路径
}
ret_fields3={
    'status': fields.Integer,
    'msg': fields.String,
    # user对象
    'data': fields.List(fields.Nested(user_fields2))
}
class UserResource3(Resource):
    @marshal_with(ret_fields3)
    def get(self):
        users=User.query.all()
        return {
            'status': 1,
            'msg': 'ok',
            'data': users
        }

# -----------------参数解析--------------------------
# 参数解析: 解析前端发送过来的数据
parser=reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help='name是必需的参数')
parser.add_argument('age',type=int,action='append') # 可以有多个age
parser.add_argument('key',type=str,location='cookies')

class UserResource4(Resource):
    def get(self):
        # 获取参数
        args=parser.parse_args()
        name=args.get('name')
        age=args.get('age')
        key=args.get('key')

        return jsonify({'name':name,'age':age,'key':key})