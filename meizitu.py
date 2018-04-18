#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import shutil , os
from lxml import html
from bs4 import BeautifulSoup

def downloadImg(path, url):

    page_max = "1"
    i = 1
    while True:
        if i > int(page_max):
            break

        imagePage = url + '/' + str(i)
        print(imagePage)

        response = requests.get(imagePage)
        response.encoding = 'utf8'
        Soup = BeautifulSoup(response.text, 'lxml')
        # pages_index = soup.find('div', class_='page').find('em').text

        image_src = Soup.find('div', class_='content').find('img')['data-img']
        print(image_src)


        page_max = Soup.find('div', class_='page').find_all('a')[-2].text

        get_headers = {
            'Content-Type': 'text/html',
            'Vary':'Accept-Encoding',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Referer': 'http://www.mmjpg.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        image = open(str(i) + '.jpg', 'wb')
        pic = requests.get(image_src, headers= get_headers)
        image.write(pic.content)
        image.close()

        old_path = os.getcwd() + '/' + str(i) + '.jpg'

        shutil.move(old_path, path)

        i += 1

def main():
    srcfile = r'/Users/yunpengzhang/Desktop/mm/'

    url = "http://www.mmjpg.com/tag/xiaoqingxin"
    response = requests.Session().get(url)
    response.encoding = 'utf8'

    Soup = BeautifulSoup(response.text, 'lxml')

    aList = Soup.find('div', class_='pic').find_all('span', class_='title')
    # for a in aList:
    #     print(a["href"])
    i = 2
    i -= 1
    url = aList[i].contents[0]["href"]
    path = srcfile + aList[i].contents[0].text
    # path = srcfile + Soup.find('div', class_='pic').find_all('img')[3]['alt']
    if not os.path.exists(path):
        os.makedirs(path)
        downloadImg(path, url)



if __name__ == '__main__':
    main()
