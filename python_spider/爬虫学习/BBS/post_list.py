#!/usr/bin/python3
#-*-coding:utf-8 -*-
import requests
from lxml import etree
import re
import html 
import time
import global_var


    #获取每一个帖子的内容
class PostsCrawler:
    domain = 'https://www.newsmth.net'
    pattern = re.compile('<.*?>')

    def get_content(self,topic_url,page):
        querystring = {"ajax":"","p":str(page)}
        url = self.domain + topic_url
        r = requests.get(url, params=querystring)
        self.html = r.text
        self.tree = etree.HTML(r.text)
        
        time.sleep(global_var.crawl_interval)
        # return self.html,self.tree
    def get_max_page(self):
        pages = self.tree.xpath('//ol[@class="page-main"][1]/li')

        if len(pages) == 1:
            return 1

        last_page_text = pages[len(pages)-1].xpath('a')[0].text

        if last_page_text == '>>':
            return int(pages[len(pages)-2].xpath('a')[0].text)
        
        return int(last_page_text)
    def get_posts(self):
            #显示每一个楼层用户的信息
        # users_eles = tree.xpath('//td[@class="a-left"]')
            #显示帖子每一个楼层内容
        c_eles = self.tree.xpath('//td[@class="a-content"]')
        posts = []
        for c_ele in c_eles:
            post = c_ele.xpath('p')[0]
            post = etree.tostring(post)
                #使用html 转义显示
            post = html.unescape(self.pattern.sub('',post.decode('GBK')))
                #换行显示
            post = post.replace('<br/>', '\n')
            # post = html.unescape(self.pattern.sub('', post))
            posts.append(post)

        return posts

if __name__ == "__main__":
    url = '/nForum/article/AutoWorld/1942271666'

    post_crawler = PostsCrawler()
    post_crawler.get_content(url, 1)
    posts = post_crawler.get_posts()

    page_count = post_crawler.get_max_page()

    if page_count > 1:
        for i in range(2, page_count + 1):
            post_crawler.get_content(url, i)
            posts += post_crawler.get_posts()
                #抓取3页
            if i >= 3:
                break
    i = 1
    for p in posts:
        print("=============================", i, "=============================")
        print(p)
        print("")
        i += 1