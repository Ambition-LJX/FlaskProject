import requests

# GET请求
res=requests.post("http://127.0.0.1:8001/hello/")
print(res.text)

