#!/usr/bin/python
# -*-coding=utf-8 -*-
import re
import requests
import json
import urllib

lesson_url = 'http://www.chinahadoop.cn/course/1288/lesson/'

for nums in range(29882,29885):
        #这是拼接出课程的url
    url = lesson_url + str(nums)
    print(url)
        #根据课程的url找出视频的mediaurl
    respone_get_playvideo=requests.get(url)
    print(respone_get_playvideo)
        #根据请求返回的json串找出media的url对应的后缀数字
    playvideo_info = json.loads(respone_get_playvideo)

    mediaUri_nums = playvideo_info['mediaUri']
    
    playvideo_url = 'http://playvideo.qcloud.com/getplayinfo/v2/1253931042/'
        #拼接出视频下载地址url
    mediaUri =playvideo_url + str(mediaUri_nums)
    print(mediaUri)


    
    # respose = requests.get(mediaUri)
    #     #将返回的源码用json格式加载
    # videoInfo = json.loads(respose.text)
    # url = videoInfo["videoInfo"]["sourceVideo"]["url"]
    # print(url)
    # name = videoInfo['videoInfo']['basicInfo']['name']
    # print(name)
    # sourceVideo = requests.get(url)
    # sourceVideo = sourceVideo.content 





# json_01 = '{"number":"19","chapter":{"id":"6085","courseId":"1288","type":"chapter","parentId":"0","number":"2","seq":"17","title":"\u7b2c\u4e8c\u8bfe  HTML\u57fa\u7840","createdTime":"1547461079","copyId":"5886","advance":"0","publishTime":"1551319200","picture":""},"title":"\u89c6\u9891\uff1aDOM\u5c5e\u6027","summary":null,"type":"tencentVideo","content":null,"status":"published","quizNum":"0","materialNum":"1","mediaId":"0","mediaSource":"self","startTimeFormat":"01-01 08:00","endTimeFormat":"08:00","startTime":"0","endTime":"0","id":"29891","courseId":"1288","videoWatermarkEmbedded":0,"liveProvider":"0","nowDate":1555656716,"testMode":"normal","testStartTime":"0","testStartTimeFormat":"01-01 08:00","replayStatus":"ungenerated","doTimes":"0","redoInterval":"0.0","homeworkOrExerciseNum":0,"isTeacher":false,"isAssistant":false,"mediaUri":"5285890784728708281","preClassReading":"","afterClassCase":"","canLearn":{"status":"yes"},"lessonMaterials":[{"id":"25802","courseId":"1288","lessonId":"29891","title":"02-HTML.pdf","description":"","link":"","fileId":"10008","fileUri":"","fileMime":"","fileSize":"314785","source":"coursematerial","userId":"511","createdTime":"1547461081","copyId":"25562","type":"course"}]}'
# playvideo_info = json.loads(json_01) 
# mediaUri_nums = playvideo_info['mediaUri']
# print(mediaUri_nums)


# target = 'http://playvideo.qcloud.com/getplayinfo/v2/1253931042/5285890784725138456'
# respose = requests.get(target)

