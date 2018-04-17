# coding=utf-8
import requests
import shutil,os
import json
from bs4 import BeautifulSoup

import xlwt


def opp():
    wb = xlwt.Workbook()
    sh = wb.add_sheet('A Test Sheet')
    page = 1
    i = 0
    while True:
        page += 1

        url = 'http://weixin.sogou.com/weixin?query=a&_sug_type_=&s_from=input&_sug_=y&type=1&page=' + str(page) + '&ie=utf8'
        print(url)
        heder = {
            'Host': 'weixin.sogou.com',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-with': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Referer': 'http://www.gsdata.cn/rank/wxrank?type=month',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'IPLOC=CN2101; SUID=365377772E08990A000000005AD1A48F; SUV=1523688591648499; ABTEST=6|1523688598|v1; SNUID=83E5C2C1B5B3DF7CD0103D5AB664565A; weixinIndexVisited=1; JSESSIONID=aaaUAiuQQGxeQ7-andXiw'
        }

        response = requests.Session().get(url, headers= heder)
        response.encoding = 'utf8'

        # html_str = json.loads(response.text)['data']
        # html_str.replace('\r', '').replace('\n', '').replace('\t', '')
        soup = BeautifulSoup(response.text, 'lxml')
        # soup.select('video #video41yYgBmdW2Ne19mu')

        lis = soup.find('ul', class_= 'news-list2').find_all('li')

        for li in lis:
            textTag1 = li.contents[1].contents[3].contents[1].text.replace('\n', '')
            textTag2 = li.contents[1].contents[3].contents[3].text.replace('\n', '')
            textTag3 = li.contents[3].contents[3].text
            print(i, textTag1, textTag2, textTag3)

            # 按位置添加数据
            # sh.write(i, 0, number)
            # sh.write(i, 1, name.contents[1].text + " " + name.contents[3].text)
            # sh.write(i, 2, user.contents[5].text)
            # sh.write(i, 3, user.contents[7].text)
            # sh.write(i, 4, user.contents[9].text)
            # sh.write(i, 5, user.contents[11].text)
            # sh.write(i, 6, user.contents[13].text)
            # sh.write(i, 7, user.contents[15].text)
            # 保存文件

            i += 1
        print(page, "--------------------", i)
        if page > 8:
            break

    wb.save('sougou.xls')


opp()