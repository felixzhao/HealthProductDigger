#encoding:UTF-8
import requests
import time
import datetime
import sys
from bs4 import BeautifulSoup
import re

url_path = "https://swisse.com/cn-au/products/vitamins-supplements/womens-health/swisse-womens-ultivite-tablets"

try:
    print('开始处理。')
    response = requests.get(url_path)
    if response.status_code != 200:
        print("\n!!! 网络访问返回异常，异常代码：" + str(response.status_code) + " !!!\n")
    else:
        print('获取内容信息完成。')

    soup = BeautifulSoup(response.text)

    title = soup.select('.product-detail-short-desc > h2:nth-of-type(1)')
    print(title)

    #benefit = soup.find('div',{'id':'p_lt_ctl04_childPagePlaceholder_p_lt_ctl03_ProductGroupTabs_rptTabDetails_ctl00_pnlContent'})
    #directions = soup.find('div',{'id':'p_lt_ctl04_childPagePlaceholder_p_lt_ctl03_ProductGroupTabs_rptTabDetails_ctl02_pnlContent'})

    #print(benefit)
    #print(directions)

except Exception:
    print('get Exception.')
    print(sys.exc_info())
    pass

def GetTitle(url):
    print(url)
    try:
        print('开始处理。')
        response = requests.get(url_path)
        if response.status_code != 200:
            print("\n!!! 网络访问返回异常，异常代码：" + str(response.status_code) + " !!!\n")
        else:
            print('获取内容信息完成。')
        soup = BeautifulSoup(response.text)
        title = soup.find('div',{'class':'product-detail-short-desc'}) #> h2:nth-of-type(1)')
        return title
    except Exception:
        print('get Exception.')
        print(sys.exc_info())
        pass
