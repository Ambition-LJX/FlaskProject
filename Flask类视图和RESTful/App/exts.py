# exts.py: 插件管理
# 扩展的第三方插件

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_restful import Api

# 2.初始化
db = SQLAlchemy() # ORM
migrate = Migrate() # 数据迁移
cache = Cache(config={
    'CACHE_TYPE': 'simple' # 缓存类型
})
api = Api()


# 3.和app对象绑定
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app=app)
