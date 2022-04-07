"""
練習從 yahoo 商城爬回資料
這個練習用來爬取商城 iPhone12 手機資料以及價錢
屬性標籤後面的亂碼可能會因為每次網站更新不同，導致抓取失敗
這樣就要重新設定
"""

import requests
from bs4 import BeautifulSoup
import re


url = 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-12-128G-6-1%E5%90%8B%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F-9524956.html'
r = requests.get(url)
response = r.text
soup = BeautifulSoup(r.text)

# Example 1: 取得商品名稱，利用樹狀結構一層一層挑選
product_name = soup.find('div', class_='HeroInfo__heroInfo___1V1O8') \
    .find('div', class_='HeroInfo__infoCols___jJIhc') \
    .find('h1', class_='HeroInfo__title___57Yfg HeroInfo__textTooLong___BXk8j')
print(product_name)

# Example 2: 直接挑選到想要的物件, class為避免重複內建python變數，故增加底線
product_name = soup.find('h1', class_='HeroInfo__title___57Yfg HeroInfo__textTooLong___BXk8j')
print(product_name)

# 處理隨機的 class 命名
# 利用 CSS selector 做篩選
product_name = soup.select('h1[class*="HeroInfo__title__"]')
print(product_name)

# 利用 Regex (正規表達式) 做篩選
reg = re.compile('HeroInfo__title__')
product_name = soup.find('h1', class_=reg)
print(product_name)

# 商品價格
d = soup.find('div', class_='HeroInfo__mainPrice__1xP9H')
print(d)
print(d.text)

# 將價格字串轉成純數字
d_price = float(d.text[1:].replace(',', ''))
