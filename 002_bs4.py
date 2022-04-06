from bs4 import BeautifulSoup
import requests

"""
將 html 原始碼轉換成 bs4 的 object 進行解析
. 取得標籤
[] 取得屬性

prettify() 做自動排版

find() 找到第一個
find_all() 找到所有的
"""

# 發出請求，攔截回應，用 BeautifulSoup 進行解析
url = 'https://sample.v123582.repl.co/'
r = requests.get(url)
response = r.text
soup = BeautifulSoup(r.text)
print(soup)

# 找出第一個 id = title 的 p 標籤
print(soup.find('p', id='title').text)

# 找所有的 a 標籤，利用 strip 消除空白和換行
for d in soup.find_all('a'):
    print(d.text.strip())

