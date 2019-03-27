# !/usr/bin/pyhton3
# -*- coding:utf-8 -*-
# import re

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
# s = 'www.chinahadoop.cn'
# # print(re.match('cn',s))
# # print(re.match('www',s))
# print(re.fullmatch('chinahadoop',s))
# print(re.fullmatch('www.chinahadoop.cn',s))


# from lxml import etree
# import re
# with open('test.html', 'r',encoding='utf-8') as f:
#     c = f.read()

# s = re.sub('\n', '',c)
# tree = etree.HTML(s)

# ret1 = tree.xpath('/html/body/div/p')     #只在当前节点的子节点匹配值，不匹配孙子节点、从孙节点
# ret2 = tree.xpath('/html/body/div//p')     #匹配节点下所有子孙节点
# ret3 = tree.xpath('/html/body/div[1]//p')  #虽然匹配所有子孙，但只找第一个子节点下div包含的p值
# # print(len(ret1))
# # print(len(ret2))
# # print(ret1[3].text)
# #print(ret2[6].text)
# print(ret3[1].text)


# from lxml import etree

# import re

# with open('test.html', 'r', encoding='utf8') as f:

#     c = f.read()

# s = re.sub('\n', '',c)

# tree = etree.HTML(s)

# ret = tree.xpath('//*[@class= "ref"] ')[0]
# print(ret.attrib['class'])    #ref 

# ret2 = tree.xpath('//*[@id= "title"] ')[0]
# print(ret2.text)

# ret3 = tree.xpath('//p | //h1')
# print(len(ret3))
# retor = tree.xpath('//*[self::p or self::h1] ')
# print(len(retor))

# ret4 = tree.xpath('//*[contains(@class,"ref")]')
# print(ret4[0].attrib['class'])
# print(ret4[1].text)


# line = "我自横刀向天笑b笑完我就去睡觉b睡什么睡起来嗨"
# print (line.split('b'))
# print (line.split("b''"))


list1 =['i','like','machine','learning']

print (list1.index("like"))

del (list1[list1.index('like')])
print (list1)