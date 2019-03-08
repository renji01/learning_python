#!/usr/bin/python3
#-*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup 
import sys
import lxml
# #爬取小说具体内容
# url = 'https://www.biqukan.com/25_25074/8764947.html'
# response = requests.get(url)
# text  = response.text
# #print (text)
# html = BeautifulSoup(text,'lxml')
# content = html.find_all('div',class_='showtxt')
# #print(content)
# str_content = str(content[0])
# show_txt =str_content.replace('<br/>','\n')
# print(show_txt)

# #爬取小说目录：
# biqukan ='https://www.biqukan.com'
# url_cata = 'https://www.biqukan.com/25_25074/'
# response_listmain=requests.get(url_cata)
# list_main = response_listmain.text
# html_list = BeautifulSoup(list_main,'lxml')
# div = html_list.find_all('div',class_='listmain')
# a_bf = BeautifulSoup(str(div[0]))
# a = a_bf.find_all('a')
# for each in a :
#     print(each.string,biqukan + each.get('href'))

class download(object):
    def __init__(self):
        self.server ='http://www.biqukan.com/'          #笔趣网的主页面
        self.target='https://www.biqukan.com/25_25074/'   #笔趣网的小说目录
        self.names = []          #用来记录小说章节名字
        self.urls = []           #记录下载地址
        self.nums  = 0           #章节数
    
    def get_download_url(self):            #定义小说目录下载地址
        req = requests.get(url = self.target)   
        html = req.text
        div_bf = BeautifulSoup(html,'lxml')
        div = div_bf.find_all('div',class_='listmain')        #找到页面元素。 
        a_bf = BeautifulSoup(str(div[0]))        
        a = a_bf.find_all('a')                               #a标签标识
        self.nums = len(a)                    #查看一共有多少章节
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self,target):       #每一个章节的内容
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,'lxml')
        texts = bf.find_all('div',class_ ='showtxt')
        show_txt = texts[0].text.replace('<br/>','\n\n')
        return show_txt
    
    def writer(self,name,path,text):                            #定义write函数，
        with open(path,'w+',encoding='utf8') as f:
            f.write(name + '\n')
            f.write(text)
            f.write('\n\n')

if __name__ =='__main__':
    dl = download()
    dl.get_download_url()
    print('----开始下载小说----')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '鬼吹灯.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write('已下载：%.3f%%' % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('----小说下载完成----')