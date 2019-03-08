# !/usr/bin/pyhton3
# -*- coding:utf-8 -*-
import re
# str ='Total income is around $750,000,ended with 3000'
# 如果使用单斜杠，python把他作为转义字符，然而实际没有转义字符，所以会保警告提示
# 通过再加一个\反斜杠，来讲反斜杠转义，就ok。
# 也可以在 字符串前加上r'\s'表示按字面意思解释该字符串。

# print (re.findall('\\$[\\d,]+',str))     # 输出 ['$750,000,']
# b = re.findall('\\$[\\d,]+',str)[0]
# print(b)                         #输出 $750,000,
# c = re.findall('\\s[\\d,]',str)
# print(c)                         #输出 [' 3']
# d = re.findall('\\s[\\d,]+',str)
# print(d)                         #输出  [' 3000']
# e = re.findall('[\\d,]+',str)
# print(e)                         #输出 ['750,000,', '3000']


s1 = "Boeing is a USA company. USA has many giant companies, including Boeing."
s2 = 'Total income is around $750,000 , pretty good income'

# print (re.findall('\\$750,000',s2))      # ['$750,000']

# print (re.findall('\\d+',s2))            # ['750', '000']

# print(re.findall('\\$\\d\\d\\d?',s2))    # ['$750']
# print(re.findall('\\d?',s2)) 

# print(re.findall('\\d{3,5}',s2))       #找到的数字的第三个--第五个字符值。
# print(re.findall('\\d{0,}',s2))        #匹配到的数据从下标0开始，输出来。
# print(re.findall('\\d{3,}',s2))

# http='<a href="http://www.baidu.com"></a>'
# print(re.findall('href=\".*\"',http))       #匹配内链地址
# print(re.findall('href=\"(.*?)\"',http))[0]   #小括号表示匹配搜索结果中展示出来。

# print(re.findall('[a-z,A-Z,0-9]',s2))       #利用集合的方式匹配所有字母
# print(re.findall('[a-z,A-Z,0-9]+',s2))      #匹配显示所有单词
# print(re.findall('[^0-9]+',s2))           #这里的尖括号表示匹配 非0-9的值


# s = '<a href="https://www.baidu.com">Baidu</a>'
# print(re.findall('href=\"(.*)\"',s)[0])

# print(re.findall('href=\".*\"',s))

s = "<h1 id='title'>辛亥革命<h1>"
