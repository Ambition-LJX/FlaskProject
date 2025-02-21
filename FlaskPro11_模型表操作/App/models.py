# 模型 数据库

from .exts import db

# 模型 数据库
# 类   ==> 表结构 表的一条数据
# 类属性 ==> 表字段
# 对象  ==> 表的一行数据

# 模型Model: 类
# 必须继承 db.Model
class User(db.Model):

    # 表名
    __tablename__ = 'user' # 表的名字

    # 定义表字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True,index=True)
    age=db.Column(db.Integer,default=1)

    # db.Column: 表示字段
    # db.Integer: 表示整数
    # primary_key=True: 主键
    # autoincrement=True : 自动递增
    # unique=True: 唯一约束
    # index=True 创建一个索引 提升查询效率
    # default 为这列定义默认值
    # nullable=False 是否允许为空

    # 将查询的结果 以列表的形式写出
    def __repr__(self):
        return self.name






