#!/usr/bin/python3
#-*-coding:utf-8 -*-
import requests
from lxml import etree
import re
#获取主题 内容

class TopicsCrawler:
    domain = 'https://www.newsmth.net'

    def get_content(self, board_url, page):
        querystring = {"ajax":"","p":str(page)}
        url = self.domain + board_url
        r = requests.get(url, params=querystring)
        # return r.text
        self.html = r.text
        self.tree = etree.HTML(r.text)

        return self.html,self.tree

    # def init_etree(self,html):
    #     if self.tree == None:
    #         self.tree = etree.HTML(html)

        #获取最大主题下内容的最大页码
    def get_max_page(self):

            #定义有多少个分页元素
        pages = self.tree.xpath('//ol[@class="page-main"][1]/li')
            #如果只有一页，那就返回一页
        if len(pages) ==1:
            return 1
            #找到顶栏分页中最后一页
        last_page_text = pages[len(pages)-1].xpath('a')[0].text

            #通过观察发现>>前的元素就是最后的页码
        if last_page_text == '>>':
                #这里注意页码以整数形式表示
            return int(pages[len(pages)-2].xpath('a')[0].text) 
        
        return int(last_page_text)

            #获取版面标题和url 地址
    def extract_tag_a(self, columns, index):
        title = columns[index].xpath('a')[0].text
        url = columns[index].xpath('a')[0].attrib['href']
        return title, url
    
            #解决某些字段为空的情况，当返回为None时显示为0.
    def extract_text(self, columns, index):
        tt = columns[index].text
        return tt if tt is not None else 0
            #获取版面中标题、发版时间、作者、like、回复数，最新回复列信息。
    def get_post_list(self):
        rows = self.tree.xpath("//table[@class='board-list tiz']/tbody/tr")
        posts = []
        for row in rows:
            post = {}
            columns = row.xpath('td')
            post['title'], post['url'] = self.extract_tag_a(columns, 1)
            post['publish_time'] = self.extract_text(columns, 2)
            
            post['author_id'], post['author_url'] = self.extract_tag_a(columns, 3)
            post['rating'] = self.extract_text(columns, 4)
            post['num_likes'] = self.extract_text(columns, 5)
            post['num_replies'] = self.extract_text(columns, 6)
            
            posts.append(post)
        return posts

#这个函数表示运行上面类
if __name__ =='__main__':
    plc = TopicsCrawler()
        #打印出第一页中所有主题的内容
    content = plc.get_content('/nForum/board/AutoWorld',1)
    print (plc.get_max_page())
    for post in plc.get_post_list():
        print(post)



