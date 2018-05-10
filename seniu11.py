import threading
from time import sleep

from lxml import html
import re
import requests

class manager():
    url = ""
    def __init__(self, url):
        self.url = url

    @classmethod
    def Download(cls):
        print(cls.url, 'asdfasdf')

    def getLink(self):
        response = requests.Session().get(self.url)
        response.encoding = 'gbk'

        sel = html.fromstring(response.text)
        # print(response.text)
        # 图片总数
        texts = sel.xpath('//div[@class="text-list"]/div[@class="wrap"]/dl/dd/a/h2/text()')
        links = sel.xpath('//div[@class="text-list"]/div[@class="wrap"]/dl/dd/a/@href')
        return texts, links

    def beginDownload(self, text, link):
        print(link, threading.active_count())
        sleep(1)


        # for a in alist:
        #     print(a.xpath(''))
        #     print(a.xpath('@href'))

threads = []
m = manager("http://seniu11.com/tupian/wangyouzipai/")
text_link_arr = m.getLink()


for i in range(0, len(text_link_arr[0])):

    t = threading.Thread(target=m.beginDownload, args=(text_link_arr[0][i], text_link_arr[1][i]))

    t.setDaemon(True)

    t.start()
    while True:
        # 判断正在运行的线程数量,如果小于5则退出while循环,
        # 进入for循环启动新的进程.否则就一直在while循环进入死循环
        if (threading.active_count()< 100):
            break