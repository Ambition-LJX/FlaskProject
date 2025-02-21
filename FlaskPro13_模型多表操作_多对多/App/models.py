# 模型 数据库

from .exts import db

# 模型 数据库
# 类   ==> 表结构 表的一条数据
# 类属性 ==> 表字段
# 对象  ==> 表的一行数据

# 多表关系
#--------------多对多-----------------
# 用户收藏电影
# 用户: 电影=N:M
# 中间表:收藏表
collect=db.Table(
    'collects',
    db.Column('user_id',db.Integer,db.ForeignKey('usermodel.id'),primary_key=True),
    db.Column('movie_id',db.Integer,db.ForeignKey('movie.id'),primary_key=True)

)
# 用户表
class UserModel(db.Model):
    __tablename__ = 'usermodel'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)

# 电影表
class MovieModel(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    # 关联
    users=db.relationship('UserModel',backref='movies',lazy='dynamic',secondary=collect)

