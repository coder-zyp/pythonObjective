#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

import xlwt




def opp():

    wb = xlwt.Workbook()
    sh = wb.add_sheet('A Test Sheet')
    page = 10
    i = 0
    while True:
        page += 1

        url = 'http://www.gsdata.cn/rank/ajax_wxrank?type=month&post_time=2018-03-01_2018-03-31&page=' + str(
            page) + '&types=all&industry=all&proName=&dataType=json'
        print(url)
        # url = 'http://www.gsdata.cn/rank/wxrank?type=month'
        srcfile = r'/Users/yunpengzhang/Desktop/data/'

        heder = {
            'Host': 'www.gsdata.cn',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-with': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'http://www.gsdata.cn/rank/wxrank?type=month',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'acw_tc=AQAAAJx/uG3fYgsANlN3d/4m6tJYbz4N; _csrf-frontend=c2a12ab1b4218ccccec323735f302ab84836975e9e24f9ea30573d5bd47792eba%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22o38-oOH30-U6_l1fwf9-nbXG8Sho08g6%22%3B%7D; bdshare_firstime=1523607626893; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1523607627; _gsdataCL=WzEyMzcxOCwiMTg2MjQ1NjA1NjIiLCIyMDE4MDQxMzE2MjA0NSIsIjYwYmQwYmUwMDJkZWY2ZTQ4MGJkYmJiOTljMmYyODZkIiwiMTAwNDMwIl0%3D; PHPSESSID=1n73soqb1a8bb3idc17fecd4f4; _identity-frontend=54f9c1a12f903648d68bf8ebae84f212d8135dbbcbd3c7e2e87f65ab010ef173a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A27%3A%22%5B123718%2C%22test+key%22%2C2592000%5D%22%3B%7D; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=1523611609'
        }
        response = requests.Session().get(url, headers=heder)
        # response.encoding = 'utf8'

        html_str = json.loads(response.text)['data']
        html_str.replace('\r', '').replace('\n', '').replace('\t', '')
        soup = BeautifulSoup(html_str, 'lxml')
        # soup.select('video #video41yYgBmdW2Ne19mu')

        trs = soup.find_all('tr')

        for user in trs:
            a = user.contents
            number = user.contents[1].text

            name = user.contents[3].contents[1].contents[1].contents[3]

            # 按位置添加数据
            sh.write(i, 0, number)
            sh.write(i, 1, name.contents[1].text + " " + name.contents[3].text)
            sh.write(i, 2, user.contents[5].text)
            sh.write(i, 3, user.contents[7].text)
            sh.write(i, 4, user.contents[9].text)
            sh.write(i, 5, user.contents[11].text)
            sh.write(i, 6, user.contents[13].text)
            sh.write(i, 7, user.contents[15].text)
            # 保存文件

            i += 1
        print(page, "--------------------", i)
        if page > 8:
            break

    wb.save('example.xls')


opp()
