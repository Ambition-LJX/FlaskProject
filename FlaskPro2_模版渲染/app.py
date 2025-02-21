from flask import Flask, render_template,jsonify

# 创建Flask应用对象
app2= Flask(__name__)


# 路由route+视图函数
@app2.route('/')
def home():
    return 'Flask Home'

@app2.route('/index/')
def index():

    return render_template('index.html',name='123')
    # 返回JSON
    # return jsonify({'name':'123'})

if __name__ == '__main__':
    # 启动服务器
    app2.run(host='127.0.0.1', port=8080, debug=True)
