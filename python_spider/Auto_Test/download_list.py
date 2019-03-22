#!/usr/bin/python
# -*-coding=utf-8 -*-
import re 
import requests
from bs4 import BeautifulSoup
from lxml import etree


with open('list.html','r',encoding='utf8') as f:
    response = f.read()
    tree = etree.HTML(response)
    learn_list = tree.xpath('//*[@class= "course-lesson"]')
    # lesson_list = learn_list.text
    print(len(learn_list))
    for lesson in learn_list:
        lessons = lesson.text
        print(lessons)
    f.close()



# html = response.text
# html = BeautifulSoup(html,'lxml')
# print(html)
# period_list = html.find_all('li',class_='course-lesson')
# print(period_list)

# str_content = str(content[0])
# show_txt =str_content.replace('<br/>','\n')
# print(show_txt)


