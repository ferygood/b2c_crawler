from urllib import request
import requests
import json

"""
示範最基本的發送請求，取得回應 (GET, POST)
"""


# 1. 發送請求，取得回應
r = requests.get('https://github.com/timeline.json')
response = r.text
print(response)
print(type(response)) 

# 2. response 實際上是一個長得很像 json/字典 的字串，所以我們需要轉換格式來做解析
d = json.loads(response) # 轉成真正字典，這樣才能做解析
print(d)
print(type(d))

# 3. Request 傳輸資料範例: 直接把參數加在網址後面
url = "http://httpbin.org/get?key1=value1&key2=value2"
r = requests.get(url)
print(r.url)
print(r.text)

# 4. Request 傳輸資料範例: 用 requests.get(...) 內建參數
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
print(r.text)

# 5. 補充 Request 用 POST 的方式，參數用 data，資料在封包 "form"
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.url)
print(r.text)