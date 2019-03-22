#!/usr/bin/python3
#-*-coding:utf-8 -*-
import re
import requests
import json
import urllib

url = 'http://www.chinahadoop.cn/course/1288/learn#lesson/29883'
target = 'http://playvideo.qcloud.com/getplayinfo/v2/1253931042/5285890784725138456'
respose = requests.get(target)

    #将返回的源码用json格式加载
videoInfo = json.loads(respose.text)
# print(videoInfo)

    #从json中提取数据
    #表示取json串中 videoInfo.sourceVideo.url的值
url = videoInfo["videoInfo"]["sourceVideo"]["url"]
print(url)
name = videoInfo['videoInfo']['basicInfo']['name']
print(name)
    #单个视频url下载
#url = 'http://1253931042.vod2.myqcloud.com/399c539dvodgzp1253931042/d6a87bb65285890784725138456/LsisefnZczMA.mp4'

sourceVideo = requests.get(url)
    #注意字节流，用content保持源码，否则即使下载了，也打不开视频文件
sourceVideo = sourceVideo.content   
with open ('d:/download/sourceVideo/'+ name +'.mp4','wb+') as f:
    print('-------开始下载------')
    f.write(sourceVideo)
    print('-------下载完成------')





