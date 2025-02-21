from App import create_app

app3=create_app()



if __name__ == '__main__':
    app3.run(host="127.0.0.1",port=8000,debug=True)