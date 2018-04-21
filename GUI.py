
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from tkinter import *
import os
from meizitu import meizituClass

class GUIDemo():
    def __init__(self):
        window = Tk()
        window.title('title')
        width, height = 800, 600
        window.geometry('%dx%d+%d+%d' % (width, height, (window.winfo_screenwidth() - width) / 2, (window.winfo_screenheight() - height) / 2))

        Label(window, text="First").grid(row=0)
        Label(window, text="Second").grid(row=1)

        e1 = Button(window, command=self.btnclick())
        e2 = Entry(window)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        window.mainloop()

    def btnclick(self):
        url = 'http://www.mmjpg.com/tag/xiaoqingxin'
        scr = ''
        meizituClass(url, scr)


    print(int(round(time.time() * 1000)))    # 毫秒级时间戳
    print(os.path.abspath('.'))


GUIDemo()