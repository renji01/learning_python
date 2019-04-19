# -*- coding: utf-8 -*-


import requests
from lxml import etree
from bs4 import BeautifulSoup 
import sys

class Novels():
    def __init__(self):

        self.headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
    def novel_list_url(self):
        url = "http://www.xbiquge.la/15/15409/"
        res = requests.get(url,headers = self.headers)
        noves_list_html = etree.HTML(res.text)

        chapter_urls = noves_list_html.xpath('//div[@id="list"]/dl/dd/a/@href')
        # print(chapter_urls)
        
        for chapter_url in chapter_urls:
            chapter_url = "http://www.xbiquge.la{}".format(chapter_url)
            # print(chapter_url)
           
            respone = requests.get(chapter_url)
            noves_content_html = etree.HTML(respone.text)
            content = noves_content_html.xpath('//*[@id="content"]')
            print (content)



            # text = respone.text
            # noves_content_html = BeautifulSoup(text,'lxml')
            # content = noves_content_html.find_all('div',id='content')
            # print (content)
            # str_content = content
            # show_txt =str_content.replace('<br/>','\n')
            # print(show_txt)
        


if __name__ == '__main__':
    novel = Novels()
    novel.novel_list_url()
  


