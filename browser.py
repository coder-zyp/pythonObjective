
import os

from PyQt5.uic.properties import QtCore
from lxml import html
import re
import requests

from PyQt5.QtWidgets import QApplication, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtCore import QUrl



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

    path = u"{}/{} {}p".format(os.path.dirname(__file__), title, total)
    print(os.path.dirname(__file__))
    if not os.path.exists(path):
        os.makedirs(path)
        n = 1
        for i in range(int(total)):
            # 每一页
            try:
                link = '{}/{}'.format(url, i+1)
                s = html.fromstring(requests.get(link).content)
                # 图片地址在src标签中
                jpgLink = s.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
                # print(jpgLink)
                # 文件写入的名称：当前路径／文件夹／文件名
                filename = '%s/%s.jpg' % (path, n)
                print(filename)
                print(u'开始下载图片:%s 第%s张' % (title, n))
                with open(filename, "wb") as jpg:
                    jpg.write(requests.get(jpgLink, headers=header(jpgLink)).content)
                n += 1
            except:
                pass



class WebEngineView(QWebEngineView):

    def __init__(self):
        super(WebEngineView, self).__init__()
        self.settings().setAttribute(
            QWebEngineSettings.LocalStorageEnabled,
            True
        )

        self.urlChanged.connect(self.onLinkClick)
    def onLinkClick(self, url):
        print(url)

    def createWindow(self, types):
        new = WebEngineView()
        # new.load(QUrl("http://www.mzitu.com"))
        return new

        # print(QApplication.clipboard().text())
        # app.clipboard().setText("")
    #     print(self.url())
        # print(self.page().url(), self.page().requestedUrl())
        # self.page().toHtml(self.callable)
        #
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

def chageCopyLink():
    print(app.clipboard().text())
    link = app.clipboard().text()

    if re.match(r'^https?:/{2}\w.+$', link):
        getPiclink(link)
        # with ThreadPool(4) as pool:




app = QApplication([])
app.clipboard().changed.connect(chageCopyLink)
view = WebEngineView()

view.load(QUrl("http://www.mzitu.com"))
view.show()
app.exec_()
