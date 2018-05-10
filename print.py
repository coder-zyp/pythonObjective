
#!usr/bin/env python
# encoding:utf-8
def strReverse(str):
  return str[::-1]
print('Beautiful is better than ugly'[::-1])


# portion = os.path.splitext(filename)#分离文件名字和后缀


class Tst:
    name = 'tst'

    data = 'this is data'

    # 普通方法
    def normalMethod(self, name):
        print(self.data, name)

    # 类方法,可以访问类属性
    @classmethod
    def classMethod(cls, name):
        print(cls.data, name)

    # 静态方法,不可以访问类属性
    @staticmethod
    def staticMethod(name):
        print(name)


tst = Tst()
tst.data = 'this is new'
tst.normalMethod('name')
tst.classMethod('name')
tst.staticMethod('name')