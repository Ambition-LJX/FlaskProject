import requests

res=requests.get("http://127.0.0.1:8001/user4/",
                    json={'name':'lisi'},
                    headers={"Content-Type":"application/json",'Cookie':'key=sadafafa'})
print(res.text)