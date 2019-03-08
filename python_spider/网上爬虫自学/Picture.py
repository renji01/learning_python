#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
import json

# url = 'https://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD&from=home#%E5%85%A8%E9%83%A8%269'
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'lxml')

# print(soup.select('img'))

def getSouGouImg(category,length,path):
    len = length
    cate = category
    imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' + cate + '&tag=%E5%85%A8%E9%83%A8&start=0&len=' + str(len) + '&width=1920&height=1080' )
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        #imgs_url.append(j['bthumbUrl'])             #下载缩略图
        imgs_url.append(j['pic_url'])                #下载大图
    m =0
    for img_url in imgs_url:
        print('****' + str(m)  + '.jpg****' + '  Downloading....')  #下载过程中打在屏幕中的提示语
        urllib.request.urlretrieve(img_url,path+str(m) + '.jpg')    #下载下来的文件命名
        m=m+1
    print('Download complete')

getSouGouImg('壁纸',20,'d:/download/壁纸/')            #调用函数，输入三个参数


