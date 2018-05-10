# from PyQt5.QtGui import QContextMenuEvent
# # from PyQt5.QtTest import QTest

import sys
import os

# from logging import debug
# from PyQt5.QtGui import QIcon
from distutils import log, config
from distutils.log import debug

# from PyQt5 import Qt
from lxml import html
import re
import requests
import time

from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QMenu, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtCore import QUrl, QEvent, QPoint, QObject
from PyQt5.uic.properties import QtGui, QtCore


def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers


# 图片链接列表， 标题
# url是详情页链接
def getPiclink(url):
    sel = html.fromstring(requests.get(url).content)
    # 图片总数
    total = sel.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]
    # 标题
    title = sel.xpath('//h2[@class="main-title"]/text()')[0]
    # 文件夹格式
    dirName = u"【{}P】{}".format(total, title)
    # 新建文件夹
    os.mkdir(dirName)

    n = 1
    for i in range(int(total)):
        # 每一页
        try:
            link = '{}/{}'.format(url, i + 1)

            s = html.fromstring(requests.get(link).content)
            # 图片地址在src标签中
            jpgLink = s.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
            # print(jpgLink)
            # 文件写入的名称：当前路径／文件夹／文件名
            filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, n)
            print(u'开始下载图片:%s 第%s张' % (dirName, n))
            with open(filename, "wb+") as jpg:
                jpg.write(requests.get(jpgLink, headers=header(jpgLink)).content)
            n += 1
        except:
            pass


a = 1


class WebEngineView(QWebEngineView):
    a = 1

    def __init__(self):

        super(WebEngineView, self).__init__()
        self.settings().setAttribute(
            QWebEngineSettings.LocalStorageEnabled,
            True
        )
        self.load(QUrl("http://www.mzitu.com"))
        self.urlChanged.connect(self.onLinkClick)

    def onLinkClick(self, url):
        print(url)

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = WebEngineView()
            webView.setAttribute(Qt.WA_DeleteOnClose, True)
            return webView

        return super(WebEngineView, self).createWindow(windowType)

    def callable(self, data):
        print(self.url())
        view.load(self.url())

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        for action in [
            QWebEnginePage.Back, QWebEnginePage.Forward,
            QWebEnginePage.Reload, QWebEnginePage.Stop,
            QWebEnginePage.CopyLinkToClipboard
        ]:
            action = self.pageAction(action)
            if action.isEnabled():
                menu.addAction(action)
        menu.exec_(event.globalPos())


def chageCopyLink(type):
    print(type)
    link = app.clipboard().text()
    if re.match(r'^https?:/{2}\w.+$', link):
        getPiclink(link)


#   app.clipboard().setText("")

app = QApplication([])
app.clipboard().changed.connect(chageCopyLink)
view = WebEngineView()
view.show()
app.exec_()
