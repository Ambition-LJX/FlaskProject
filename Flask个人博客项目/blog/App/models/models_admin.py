# 模型 数据库
from ..exts import db

# 用户表
class AdminUserModel(db.Model):
    __tablename__ = 'tb_adminuser'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    password=db.Column(db.Integer,default=1)