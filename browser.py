# from PyQt5 import Qt
from PyQt5.QtGui import QContextMenuEvent
# from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QEvent, QPoint
from PyQt5.QtWebEngine import QtWebEngine

class WebEngineView(QWebEngineView):

    def createWindow(self, types):
        # print("aaaa", self.url())
        # self.page().toHtml(self.callable)

        self.forward()
        # return self


    def callable(self, data):
        print(data)



    def contextMenuEvent(self, event):
        # test = QContextMenuEvent()
        print("event", event)
        super().contextMenuEvent(event)

        # self.actionExit = menu.addAction("Exit")
        # self.actionExit.triggered.connect(self.exit_requested)
        # menu.exec_(self.mapToGlobal(QPoint(event.x(), event.y())))

    # def connectNotify(self, method):
    #     print(self.url(),)
    #     print(method)
    def iconUrlChanged(self, ur):
        print('iconUrlChanged', ur)

    def urlChanged(self, ur):
        print('urlChanged', ur)

class webView(QWebView):
    def rrr(self):
        print('')
app = QApplication([])
view = webView()
view.load(QUrl("http://www.mzitu.com"))
view.show()
app.exec_()
