#encoding:UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import time
import datetime
import sys
from bs4 import BeautifulSoup
import re
from GetProductDetailInfo import GetTitle

def SaveResult(f_out, result, page_number):
    f_out.write('page:' + str(page_number) + '\n')
    if not result:
        return
    for item in result:
        f_out.write(item)
        f_out.write('\n')
    return

def GetTitles(page_content):
    titles = []
    if not page_content:
        return ''
    soup = BeautifulSoup(page_content)
    items = soup.findAll('div',{'class':'product-item '})
    if not items:
        return ''
    for item in items:
        url = item.find('a', href=True)
        arr = url['href'].split('/')
        title = arr[len(arr) - 1].replace('-',' ')
        print(title)
        titles.append(title)
    return titles

def GetPage(url, page_number):
    cur_url = url + str(page_number)
    print(cur_url)
    try:
        print('开始处理。')
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        #payload = (('page', str(page_number))
        response = requests.get(cur_url, headers=headers)#, params=payload)

        #print('request url: \n')
        #print(response.json)

        if response.status_code != 200:
            print("\n!!! 网络访问返回异常，异常代码：" + str(response.status_code) + " !!!\n")
        else:
            print('获取内容信息完成。')

        trace_log = open('./page' + str(page_number) + '.txt','w+')
        trace_log.write(response.text)
        trace_log.close()

        return response.text
    except Exception:
        print('get Exception.')
        print(sys.exc_info())
        pass

if __name__ == '__main__':
    url_path = "https://swisse.com/cn-au/products?page="
    f_out = open('./products_name.txt','w+')
    page_number = 1
    while True:
        page_content = GetPage(url_path, page_number)
        result = GetTitles(page_content)
        if not result:
            break
        SaveResult(f_out, result, page_number)
        page_number += 1

        if page_number > 20:
            break
        pass
    f_out.close()
