# -*- coding=utf-8 -*-    
#原文地址：https://blog.csdn.net/Mazy_ma/article/details/78996103

#1、文件目录结构 
    ├── Zhipin_spider  ＃ 文件夹
│   ├── spider_main.py  # 调度器。是爬虫的入口，管理各个类
│   ├── html_downloader.py # 下载器，负责网页内容的下载
│   ├── html_parser.py # 解析器，负责解析数据，获取有价值的数据
│   └── html_outputer.py # 输出,将获取到的数据输出
--------------------- 

#2、所用依赖：
    采用 Requests 请求数据
    使用 BeautifulSoup 解析数据
    使用 xlsxwriter 框架保存数据到 Excel 文件中
