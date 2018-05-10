import threading
from time import sleep

from lxml import html
import re
import requests


def get_html(link):
    print(link)
    response = requests.Session().get(link)
    response.encoding = 'gbk'
    return response.text


class manager():

    def __init__(self, host, url):
        self.url = host + url
        self.host = host



    def getLink(self):

        sel = html.fromstring(get_html(self.url))

        # texts = sel.xpath('//div[@class="text-list"]/div[@class="wrap"]/dl/dd/a/h2/text()')
        links = sel.xpath('//div[@class="text-list"]/div[@class="wrap"]/dl/dd/a/@href')
        return links

    def beginDownload(self, link):
        # print(self.host + link)
        htmlstr = get_html(self.host + link)
        sel = html.fromstring(htmlstr)
        links = sel.xpath('//div[@class="picture"]/div[@class="wrap"]/div/img/@src')


        title = sel.xpath('//div[@class="picture"]/div[@class="wrap"]/h1/text()')
        print(title, links)
        # for a in alist:
        #     print(a.xpath(''))
        #     print(a.xpath('@href'))

m = manager("http://seniu11.com", "/tupian/wangyouzipai/")
text_link_arr = m.getLink()


for i in range(0, len(text_link_arr)):

    # t = threading.Thread(target=m.beginDownload, args=(text_link_arr[0][i], text_link_arr[1][i]))
    #
    # t.setDaemon(True)
    #
    # t.start()

    m.beginDownload(text_link_arr[i])

    break
    # while True:
    #     # 判断正在运行的线程数量,如果小于5则退出while循环,
    #     # 进入for循环启动新的进程.否则就一直在while循环进入死循环
    #     if (threading.active_count()< 100):
    #         break