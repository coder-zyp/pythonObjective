
# coding=utf-8
import requests
import shutil,os

from bs4 import BeautifulSoup



def getVideoUrl():
    print('aa')


def main():
    url = r'http://www.meipai.com/media/980134824'
    srcfile = r'/Users/yunpengzhang/Desktop/meipai/'

    heder = {

        'Host': 'www.meipai.com',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure - Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://www.meipai.com/square/474',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q=0.9',
        'Cookie': 'CNZZDATA1256786412=1030513690-1523520276-https%253A%252F%252Fwww.baidu.com%252F%7C1523585646; UM_distinctid=162b8f51e3d1b-0a6ac440581b5a-3f616c4d-240000-162b8f51e3e731; MUSID=egt12ajefoqjgafv86q9jr38b0; pvid=XawU%2B%2BJiovQXjSn5iEDJMQJhF%2BorL3xR; sid=egt12ajefoqjgafv86q9jr38b0; virtual_device_id=aa0c2a3232e4bcd9ba5b5e783ab754d8',
        'Connection':'keep-alive'
    }
    response = requests.Session().get(url, headers= heder)
    response.encoding = 'utf8'

    soup = BeautifulSoup(response.text, 'lxml')
    # soup.select('video #video41yYgBmdW2Ne19mu')
    src = soup.find('div', class_='MP6uZaD5TlYM9X0G8V')
    name = soup.select('h1 #detail-description break')
    open()

if __name__ == '__main__':
    main()