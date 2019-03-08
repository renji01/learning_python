# !/usr/bin/pyhton3
# -*- coding:utf-8 -*-
import re

# s = 'Total income is around $131,000, ended with 1000'

# re.findall('[\\d,]+',s)


# s = '<a href="https://www.baidu.com">Baidu</a><p>百度</p>'

# print(re.findall('.*?>(.*?)<',s)[0])
# print(re.findall('.*?>(.*)?<',s)[0])
# print (re.findall('.*?>(.*)<',s)[0])

# s = '<a href="https://www.baidu.com">Baidu</a>'
# print(re.findall('.*>(.*)<',s)[0])

#下面两行代码取值一样 
# s = "<h1 id='title'>辛亥革命<h1>"
# print(re.findall('>(.*?)<',s))

# pattern = re.compile('>(.*?)<')
# print(pattern.findall(s))

#测试
s = 'www.chinahadoop.cn'
# print(re.match('cn',s))
# print(re.match('www',s))
print(re.fullmatch('chinahadoop',s))
print(re.fullmatch('www.chinahadoop.cn',s))