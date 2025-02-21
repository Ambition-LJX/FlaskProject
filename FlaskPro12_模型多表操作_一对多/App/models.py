# 模型 数据库

from .exts import db

# 模型 数据库
# 类   ==> 表结构 表的一条数据
# 类属性 ==> 表字段
# 对象  ==> 表的一行数据

# 多表关系
# 一对多

# 班级:学生=1:N
# 班级表
class Grade(db.Model):
    __tablename__ = 'grade' # 表明
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    # 建立关联
    students=db.relationship('Student',backref='grade',lazy='dynamic') # 参数('关联的模型名(类名)','反向引用的名称grade对象，让Student去反过来得到grade对象的名称','延迟关联(节省资源)')

# 学生表
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    age=db.Column(db.Integer)
    # 外键: 跟Grade表中的id字段关联
    gradeId=db.Column(db.Integer,db.ForeignKey(Grade.id))

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


