#!/use/bin/python3
#-*- coding:utf-8 -*-

import requests
import ssl

class HtmlDownload(object):
    #定义函数，设置url，页码，关键词参数。
    def get_page(self,baseURL,page_num,keyword):
        try:
            param = {'query':keyword,"city":"101010100","page":page_num}

            #header
            header ={'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Referer': r'http://www.zhipin.com/job_detail/',
                'Connection': 'keep-alive'}
            #调用requests库，
            result = requests.get(baseURL,params=param,headers=header)
            
            return result.text
        except Exception as err:
            print (err)
            print('------爬取失败------')
            return None
