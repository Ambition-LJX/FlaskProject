# 路由文件

from .exts import api
from .apis import *

# 路由
api.add_resource(HelloResource, '/hello/')
api.add_resource(UserResource, '/user/')
api.add_resource(UserResource2, '/user2/',endpoint='id')
api.add_resource(UserResource3, '/user3/')
api.add_resource(UserResource4, '/user4/')

