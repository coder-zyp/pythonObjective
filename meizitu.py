#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import shutil, os
from lxml import html
from bs4 import BeautifulSoup


class meizituClass():

    def __init__(self, url, srcfile):
        super(meizituClass, self).__init__()
        response = requests.Session().get(url)
        response.encoding = 'utf8'
        Soup = BeautifulSoup(response.text, 'lxml')

        aList = Soup.find('div', class_='pic').find_all('span', class_='title')
        # for a in aList:
        #     print(a["href"])
        i = 2
        i -= 1
        self.url = aList[i].contents[0]["href"]
        self.path = os.path.abspath('..') + "/" + aList[i].contents[0].text
        if srcfile:
            self.path = srcfile + "/" + aList[i].contents[0].text
        self.downloadImg()

    def downloadImg(self):

        print('begin')
        if not os.path.exists(self.path):
            os.makedirs(self.path)


        page_max = "1"
        i = 1
        while True:
            if i > int(page_max):
                break
            imagePage = self.url + '/' + str(i)
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
                'Vary': 'Accept-Encoding',
                'Upgrade-Insecure-Requests': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
                'Referer': 'http://www.mmjpg.com/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9'
            }
            image = open(str(i) + '.jpg', 'wb')
            pic = requests.get(image_src, headers=get_headers)
            image.write(pic.content)
            image.close()

            old_path = os.getcwd() + '/' + str(i) + '.jpg'
            shutil.move(old_path, self.path)

            i += 1


