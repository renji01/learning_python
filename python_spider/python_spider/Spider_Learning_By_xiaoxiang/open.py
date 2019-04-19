# # !/usr/bin/pyhton3
# # -*- coding:utf-8 -*-
# import requests
# url = 'https://new.qq.com/omn/20190306/20190306A03BLK.html'   # 这是win下的网址，编码方式是gbk的

# response = requests.get(url)  
# #response.encoding = 'utf-8'
# f = open('xxxxxxxxx.html','w+',encoding='utf8')  
# #当把gbk网页下的内容写道文本文件里面的时候，意味着把unicode字符序列写到一个编码为gbk的文件。
# #所以在打开的文件的时候，要指定文件的编码就ok了
# f.write(response.text)
# f.close()


import requests
from lxml import etree

class Novels():
    def __init__(self):

        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
    def novel_list_url(self):

        url = "http://www.xbiquge.la/15/15409/"
        res = requests.get(url,headers = self.headers)
        noves_list_html = etree.HTML(res.text)
        # print(noves_list_html)

        chapters_urls = noves_list_html.xpath('//div[@id="list"]/dl/dd/a/@href')
        print(chapters_urls)
        # chapters_names = noves_list_html.xpath('//div[@id="list"]/dl/dd[1]/a/text()')
        # print(chapters_names)

if __name__ == '__main__':

    novel = Novels()
    novel.novel_list_url()