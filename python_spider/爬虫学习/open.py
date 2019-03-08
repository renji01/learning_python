# !/usr/bin/pyhton3
# -*- coding:utf-8 -*-
import requests
url = 'https://new.qq.com/omn/20190306/20190306A03BLK.html'   # 这是win下的网址，编码方式是gbk的

response = requests.get(url)  
#response.encoding = 'utf-8'
f = open('xxxxxxxxx.html','w+',encoding='utf8')  
#当把gbk网页下的内容写道文本文件里面的时候，意味着把unicode字符序列写到一个编码为gbk的文件。
#所以在打开的文件的时候，要指定文件的编码就ok了
f.write(response.text)
f.close()

