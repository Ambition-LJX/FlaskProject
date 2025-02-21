# 模型 数据库

from .exts import db

# 模型 数据库
# 类   ==> 表结构 表的一条数据
# 类属性 ==> 表字段
# 对象  ==> 表的一行数据

# 作者
class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    age = db.Column(db.Integer,default=18)
    sex=db.Column(db.Boolean,default=True)
    email = db.Column(db.String(200))

    # 关系
    books=db.relationship('Book',backref='author',lazy='dynamic')

# 书籍
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),unique=True)
    date=db.Column(db.DateTime)
    # 1对多,外键
    author_id=db.Column(db.Integer,db.ForeignKey('autor.id'))

# 中间表(书籍-出版社)
book_publisher=db.Table(
    'book_publisher',
    db.Column('book_id',db.Integer, db.ForeignKey('book.id'),primary_key=True),
    db.Column('publisher_id',db.Integer, db.ForeignKey('publisher.id'),primary_key=True)
)

# 出版社
class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    website = db.Column(db.String(200))

    # 多对多，关联book表
    books=db.relationship('Book',backref='publishers',secondary=book_publisher,lazy='dynamic')
