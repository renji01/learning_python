#!/usr/bin/python3
#-*-coding:utf-8 -*-
import requests
from lxml import etree
import re 

    #抓取版本列表
class BoardListCrawler:
    headers = {
        'Host': "www.newsmth.net",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Language': "en-US,en;q=0.5",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "http://www.newsmth.net/nForum/",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'cache-control': "no-cache"
    }
    domian = "http://www.newsmth.net"
    base_url = domian + '/nForum/section/{}?ajax'

        #获取版本内容
    def get_content(self,page_num):
        url = self.base_url.format(page_num)
        response = requests.get(url, headers=self.headers)
        return response.text
        #获取版面列表
    def get_board_list(self,content):
        tree = etree.HTML(content)
            #定义版面的列中版面名称
        rows = tree.xpath("//table[@class='board-list corner']/tbody/tr")
        #print (rows[0])
        
        boards =[]

        for row in rows:
            board = {}
            columns = row.xpath('td')
                #获取版面的url
            board['url'] =columns[0].xpath('a')[0].attrib['href'] 
                #获取版面的主题
            board['titles'] =columns[0].xpath('a')[0].text
                #使用递归函数的方式获取版面的主题数
            if len(columns[1].xpath('a')) == 0:
                url = self.domian + board['url']
                r = requests.get(url,headers = self.headers)
                children_boards = self.get_board_list(r.text)
                boards += children_boards

            board['num_topics'] =columns[5].text
                #获取版本的文章数
            board['num_posts'] =columns[6].text
                #递归查找子版面信息
            
            
            boards.append(board)
        return boards

    #直接运行方法，测试打印除第一页中所有版面名称信息。
if __name__ == "__main__":
    blc = BoardListCrawler()
    c   = blc.get_content(6)
    boards = blc.get_board_list(c)
    print (boards)


    