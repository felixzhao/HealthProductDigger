#encoding:UTF-8
import requests
import time
import datetime
import sys
from bs4 import BeautifulSoup
import re
from GetProductDetailInfo import GetTitle

url_root = 'https://swisse.com'
url_path = "https://swisse.com/cn-au/products/"

try:
    print('开始处理。')
    response = requests.get(url_path)
    if response.status_code != 200:
        print("\n!!! 网络访问返回异常，异常代码：" + str(response.status_code) + " !!!\n")
    else:
        print('获取内容信息完成。')
    soup = BeautifulSoup(response.text)
    items = soup.findAll('div',{'class':'product-item '})
    for item in items:
        url = item.find('a', href=True)
        arr = url['href'].split('/')
        print(arr[len(arr) - 1].replace('-',' '))
        #print(GetTitle(url_root + url['href']))
except Exception:
    print('get Exception.')
    print(sys.exc_info())
    pass
