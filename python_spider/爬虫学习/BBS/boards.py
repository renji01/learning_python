#!/usr/bin/python3
#-*-coding:utf-8 -*-
import requests
from lxml import etree
import re 
import global_var
import time 

from mysql_manager import MysqlManager
    #表示4个线程
mysql_mgr = MysqlManager(4)


#     抓取版本列表
# class BoardsListCrawler:
    
#     domian = "http://www.newsmth.net"
#     base_url = domian + '/nForum/section/{}?ajax'
    
#     def __init__(self, interval = 1):
#         self.interval = interval

#         获取版本内容
#     def get_content(self,page_num):
#         url = self.base_url.format(page_num)
#         response = requests.get(url, headers=global_var.headers)
#             #休息一下
#         time.sleep(self.interval)
#         self.content = response.text
#         self.tree = etree.HTML(self.content)
#         return self.content,self.tree

#         获取版面列表
#     def get_board_list(self,content):
#         tree = etree.HTML(content)
#             #定义版面的列中版面名称
#         rows = tree.xpath("//table[@class='board-list corner']/tbody/tr")
#         #print (rows[0])
#         boards =[]

#         for row in rows:
#             board = {}
#             columns = row.xpath('td')
#                 #获取版面的url
#             board['url'] =columns[0].xpath('a')[0].attrib['href'] 
#                 #获取版面的主题
#             board['titles'] =columns[0].xpath('a')[0].text
#                 #使用递归函数的方式获取版面的主题数
#             if len(columns[1].xpath('a')) == 0:
#                 url = self.domian + board['url']
#                 r = requests.get(url,headers = global_var.headers)
#                 children_boards = self.get_board_list(r.text)
#                 boards += children_boards

#             board['num_topics'] =columns[5].text
#                 #获取版本的文章数
#             board['num_posts'] =columns[6].text
#                 #递归查找子版面信息
            
#             boards.append(board)

#             mysql_mgr.insert_board(board)
#         return boards

#     #直接运行方法，测试打印除第一页中所有版面名称信息。
# if __name__ == "__main__":
#     blc = BoardsListCrawler()
#     c   = blc.get_content(6)
#     boards = blc.get_board_list(c)
#     print (boards)


#整合后的代码：
class BoardsCrawler:
    domain = 'http://www.newsmth.net/'

    base_url = domain + '/nForum/section/{}?ajax'

    def __init__(self, interval = 1):
        self.interval = interval

    def get_board_of_section(self, section_idx):
        url = self.base_url.format(section_idx)
        response = requests.get(url, headers = global_var.headers)
        time.sleep(self.interval)
        self.content = response.text
        self.tree = etree.HTML(self.content)

    def get_board_list(self, etr_obj = None ):
        if etr_obj is None:
            etr_obj = self.tree
        elements = etr_obj.xpath('//table[@class="board-list corner"]/tbody/tr')
        boards = []
        for element in elements:
            board = {}
            columns = element.xpath('td')
            if len(columns) == 1:
                break
            board['board_url'] = columns[0].xpath('a')[0].attrib['href']
            board['board_name'] = columns[0].xpath('a')[0].text

            if len(columns[1].xpath('a')) == 0:
                url = self.domain + board['board_url']
                response = requests.get(url, headers = global_var.headers)
                child_board_etree = etree.HTML(response.text)
                boards.append(self.get_board_list(child_board_etree))
                continue

            board['manager_url'] = columns[1].xpath('a')[0].attrib['href']
            board['manager_id'] = columns[1].xpath('a')[0].text
            board['num_topics'] = columns[5].text
            board['num_posts'] = columns[6].text
            boards.append(board)
            mysql_mgr.insert_board(board)
            
        return boards

if __name__ == '__main__':
    bc = BoardsCrawler()
    
    for i in range(0,10):
        print("Get board of section: ", i)
        bc.get_board_of_section(i)
        boards = bc.get_board_list()