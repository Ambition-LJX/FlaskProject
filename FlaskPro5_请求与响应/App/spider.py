import requests

# GET请求
res=requests.get("http://127.0.0.1:8081/request/?name=lisi&age=23",cookies={'name':'hello'})
print(res.text)

# # POST请求
# res=requests.post("http://127.0.0.1:8081/request/",data={'name':'lucy','age':'33'})
# print(res.text)
