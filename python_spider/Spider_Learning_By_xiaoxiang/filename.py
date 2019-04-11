# -*- coding: utf-8 -*-
import requests
import time
url = 'https://news.sina.com.cn/c/2018-12-10/doc-ihprknvu0188659.shtml'
response = requests.get(url )

response.encode='utf-8'
filename = url[url.rfind('/')+1:]      #rfind是从末尾开始查找。
print('filename是：',filename)

startpos = url.find('//')+2
print ('起始位置为：',startpos)
endpos = url.find('/',startpos)
print('结束位置：',endpos)
domain = url[startpos:endpos]
print(domain)
filename = domain + '_' + filename  
print(filename)
