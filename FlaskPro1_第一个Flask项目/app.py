from flask import Flask

# 创建Flask应用对象
app1 = Flask(__name__)


# 路由route+视图函数
@app1.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app1.route('/index/')
def index():
    return 'index 首页'

if __name__ == '__main__':
    # 启动服务器
    app1.run(host='127.0.0.1', port=8080, debug=True)
