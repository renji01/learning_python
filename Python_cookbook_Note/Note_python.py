#问题1：现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]

# def do_foo(x, y):
#     print('foo',x,y)
# def do_bar(s):
#     print('bar',s)

# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         #编译器报错。可以执行
#         do_bar(*args)


# def sum(items):
#     head,*tail =items
#     return head + sum(tail) if tail else head

# items = [1,10,7,4,5,9]
# print (sum(items))


# 问题 ：从集合中查询最大/最小 几个值。
#heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题
# import heapq
# nums =[1,8,2,23,7,-4,18,23,42,37,2]
# print (heapq.nlargest(3,nums))
# print(heapq.nsmallest(3,nums))

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
# expensive = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
# print(cheap,expensive)
    #输出的内容
    #[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
    #[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]

# nums =[1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# import heapq
# heap = list(nums)
# heapq.heapify(heap)
# print (heap)


# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# nums.reverse()
# print(nums)

# print(max(nums))

# 问题：字典的中求最大最小值。 zip函数
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
   #使用zip去调换key和values的位置，values是可以比较的。
# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# print(min_price,max_price)


# list =[1,4,-5,10,-7,2,3,-1]
# list_new=[]
# for i in list:
#     if i >0:
#         print (i)
#         list_new.append(i)
# print (list_new)

   #推导式
# print ([n for n in list if n > 0])
# pos = [n for n in list if n > 0]
# print(pos)
# for i in pos :
#     print(i)


    #过滤列表中的整数
# values = ['1','2','-3','4','5','-','N/A','#']
# def is_int(val):
#     try:
#         x = int(val)
#         return True     
#     except ValueError:     
#         return False
# ivals = list(filter(is_int,values))
# print(ivals)


    #将不满足条件的值统一替换成另一个值。
# mylist =[1,2,3,4,5,-5,-4,-3,-2,-1]
# list_01=[n if n >0  else 6   for n in mylist]
# list_02=[n if n <0  else -6  for n in mylist]
# print(list_01,list_02)


    #在字典中取字典的子集，或从字典中取一类值。
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
# p1 ={key:value for key,value in prices.items() if value >200}
# print(p1)

# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key:value for key,value in prices.items()if key in tech_names}
# p2 ={key:prices[key] for key in prices.keys() & tech_names}
# print(p2)


    # ChainMap函数从字典中查找值
# a = {'x': 1, 'z': 3 }
# b = {'y': 2, 'z': 4 }
# from collections import ChainMap
# c = ChainMap(a,b)
# print(c['x'])
# print(c['y'])
# print(c['z'])


    #使用正则的方式对字典进行切割
# line = 'asdf fjdk; afed, fjek,asdf, foo'
# import re
# a = re.split(r'[ ;,\s]\s*',line)
# b = re.split(r'(?:,|;|\s)\s*',line)
# print(a)
# print(b)

    #忽略大小写的方式查找或替换文本字符串
# import re
# text = 'UPPER PYTHON, lower python, Mixed Python'
#     #不区分大小写
# text01 = re.findall('python',text,flags =re.IGNORECASE)
# print(text01)
# text02 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
# print(text02)
#     #返回的值是没有区别大小写的替换的
#     #这个方法是为了让大写替换后显示为大写，小写显示为小写
# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word
#     return replace       
# text03 = re.sub('python',matchcase('java'),text,flags=re.IGNORECASE)
# print(text03)

# import re
#     #贪婪匹配与 非贪婪匹配
# text1 = 'Computer says "no.",Phone says "yes."'
# str_pat = re.compile(r'"(.*)"')       #贪婪
# str_pat.findall(text1)
# print(str_pat.findall(text1))
# text2 = 'Computer says "no.",Phone says "yes."'
# str_pat =re.compile(r'"(.*?)"')            #非贪婪
# a = str_pat.findall(text2)
# print(a)

    #删除字符串中开头、中间、结尾不需要的字符
# s = 'hello world \n'
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# str01 = '====----hello----========'
# print(str01.rstrip("="))    #从右删除
# print(str01.lstrip('='))    #从左删除
# print(str01.strip('='))        #删除开始或结束的字符

    #字符串对齐，
# text = 'Hello World'
# print(text.ljust(20))            #左对齐
# print(text.rjust(20))            #右对齐

# print(text.ljust(20,'-'))
# print(text.rjust(20,'+'))
# print(format(text,'>20'))       #格式化函数

    #jion函数以sep作为分隔符，将seq所有的元素合并成一个新的字符串
# parts = ['Is', 'Chicago', 'Not', 'Chicago ?']
# new_parts = '  '.join(parts)
# print(new_parts)

# a = 'Is'
# b = 'Chicago'
# c = 'not Chicago ?'
# print(a + ' '+ b+' '+ c)
# print('{},{}'.format(a,b))
# print(a + ' '+ b+' '+ c)

    #format 函数可以在字符串内插入变量。
# s = "{name} has {nums} messages."
# str_01=s.format(name = 'tom', nums =20)
# print(str_01)

# name = 'Tom'
# nums = 33
# str_02= s.format_map(vars())


    #处理文本中的字符显示长度。缩进。
# s=  "Look into my eyes, look into my eyes, the eyes, the eyes, \
# the eyes, not around the eyes, don't look around the eyes, \
# look into my eyes, you're under."

# import textwrap
# print (textwrap.fill(s,70))
# print('--------------------------------')
# print (textwrap.fill(s,30))
# print('--------------------------------')
# print (textwrap.fill(s,40,initial_indent='   '))     #首行缩进
# print('--------------------------------')
# print(textwrap.fill(s,40,subsequent_indent='    '))   #随后缩进
# print('--------------------------------')
# import os
# columns= os.get_terminal_size().columns          #获取终端屏幕的尺寸
# print(columns)


    #处理字符中的html 和xml。html.escape
# s = 'Elements are written as "<tag>text</tag>".'
# import html
# from xml.sax.saxutils import unescape
# print(s)
# print(html.escape(s))                          #转换为对应的文本
# print(html.escape(s,quote=False))
# print(html.unescape(s))                       #不避开，不用转换


# data =b'hello world'
# print(data[:5])

    
    #round 函数可以进行四舍五入，取最近的偶数。
# print(round(1.234,1))        #取小数点后一位
# print(round(1.234,2))       #取小数点后2位
# print(round(-1.234,1))           

# print(round(12345,-1))         #取个位上的四舍五入
# print(round(12345,-2))         #取十位上的四舍五入

    #format函数，格式化输出。
# x= 1234.56789
# print(format(x,'0.2f'))               #保留小说点后2位
# print(format(x,'>10.1f'))             #右边对齐宽度为10
# print(format(x,'<10.1f'))             #左边对齐宽度为10
# print(format(x,'^10.1f'))             #居中对齐，宽度为10
# print(format(x,','))                  #添加千位符号
# print(format(x,'0,.1f'))              #添加千位符，保留小数点后1位。

    #二、八、十六进制转换。   bin，oct，hex
# x = 1234                   #Decimal表示十进制
# print(bin(x))              #将十进制转化为二进制，0b表示二进制
# print(oct(x))              #将十进制转为八进制，0o表示八进制，o是oct的首字母
# print(hex(x))              #将十进制数转为十六进制，0x表示十六进制

# print(format(x,'b'))        #去掉前缀显示，
# print(format(x,'o'))
# print(format(x,'x'))

    #创建或测试无穷大、负无穷或NaN（非数字）的浮点数
# a = float('inf')
# print(a)


    #分数之间的运算，fractions
# from fractions import Fraction
# a = Fraction(5,4)      #表示分数：5/4
# b = Fraction(7,16)     #表示分数：7/16
# print(a+b)
# print(a*b)
# c = a*b
# print(c.numerator)      #取c的分子
# print(c.denominator)    #取c的分母

    #数组的运算，Numpy模块
# x = [1,2,3,4]
# y = [5,6,7,8]
# print(x * 2)       #将list的值，再copy一份填进list
# # print(x + 10)
# print(x+y)         #拼接list

# import numpy as np 
# ax = np.array([1,2,3,4])
# ay = np.array([5,6,7,8])
# print(ax * 2 )            #将list中每一个值*2
# print(ax + 10)            #将list中每一个值+10
# print(ax + ay)            #将list中每一个值两两相加
# print(ax * ay)            #将list中每一个值两两相乘

    #矩阵的运算    ，numpy
# import numpy as np
# m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
# print (m)
# print(m.T)      #将矩阵行和列转置
# print(m.I)       #显示为矩阵的逆矩阵，逆矩阵就是 AB = BA =E


    #random 函数，随机选择
# import random
# l = [1,2,3,4,5,6,7,8,9,10]
# print(random.choice(l))                 #从l中随机选择1个数
# print(random.sample(l,2))              #从l中随机选择2个数           

# print(random.randint(0,10))             #从0-10生成随机整数

    #基本的日期和时间转换
# from datetime import timedelta

# a  = datetime(2019,4,18)
# print(a + timedelta(days=10))
# import  time
# print(time.time())


# def manual_iter():
#     with open('/etc/passwd') as f:
#         try:
#             while True:
#                 line = next(f)
#                 print(line,end='')
#         except StopIteration:
#             pass            

items = [1,2,3,4]
it = iter(items)

print(next(it))
print(next(it))
print(next(it))
print(next(it))





































































































































































