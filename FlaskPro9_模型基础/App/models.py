# 模型 数据库

from .exts import db

# 模型 数据库
# 类   ==> 表结构
# 类属性 ==> 表字段
# 对象  ==> 表的一行数据

# 模型Model: 类
# 必须继承 db.Model
class User(db.Model):

    # 表名
    __tablename__ = 'tb_user'

    # 定义表字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True,index=True)
    age=db.Column(db.Integer,default=1)
    sex=db.Column(db.Boolean,default=True)
    salary=db.Column(db.Float,default=100000,nullable=False)
    salary2=db.Column(db.Float,default=100000,nullable=False)

    # db.Column: 表示字段
    # db.Integer: 表示整数
    # primary_key=True: 主键
    # autoincrement=True : 自动递增
    # unique=True: 唯一约束
    # index=True 创建一个索引 提升查询效率
    # default 为这列定义默认值
    # nullable=False 是否允许为空
