#!/usr/bin/python
# -*-coding=utf-8 -*-
from selenium import webdriver
import time
import re
import requests
import json
import urllib


s = '{"number":"13","chapter":{"id":"6084","courseId":"1288","type":"chapter","parentId":"0","number":"1","seq":"1","title":"\u7b2c\u4e00\u8bfe  \u73af\u5883\u642d\u5efa","createdTime":"1547461079","copyId":"5885","advance":"0","publishTime":"1551319200","picture":""},"title":"\u89c6\u9891\uff1aWindows\u4e0b\u5b89\u88c5Ubuntu\u865a\u62df\u673a\uff08\u9009\u4fee\uff09","summary":null,"type":"tencentVideo","content":null,"status":"published","quizNum":"0","materialNum":"1","mediaId":"0","mediaSource":"self","startTimeFormat":"01-01 08:00","endTimeFormat":"08:00","startTime":"0","endTime":"0","id":"29884","courseId":"1288","videoWatermarkEmbedded":0,"liveProvider":"0","nowDate":1555665435,"testMode":"normal","testStartTime":"0","testStartTimeFormat":"01-01 08:00","replayStatus":"ungenerated","doTimes":"0","redoInterval":"0.0","homeworkOrExerciseNum":0,"isTeacher":false,"isAssistant":false,"mediaUri":"5285890784728845816","preClassReading":"\u003Cp\u003E\u8bfe\u7a0b\u76f8\u5173\u8f6f\u4ef6\u003C\/p\u003E\r\n\r\n\u003Cp\u003EVirtualBox5.2.2:\u003C\/p\u003E\r\n\r\n\u003Cp\u003E\u003Cu\u003E\u003Ca href=\u0022https:\/\/www.virtualbox.org\/wiki\/Downloads\u0022\u003Ehttps:\/\/www.virtualbox.org\/wiki\/Downloads\u003C\/a\u003E\u003C\/u\u003E\u003C\/p\u003E\r\n\r\n\u003Cp\u003EUbuntu VM Image:\u003C\/p\u003E\r\n\r\n\u003Cp\u003E\u003Ca href=\u0022https:\/\/pan.baidu.com\/s\/1qSTZ_rGe7AcJJo7vlVTp1w\u0022\u003Ehttps:\/\/pan.baidu.com\/s\/1qSTZ_rGe7AcJJo7vlVTp1w\u003C\/a\u003E\u003C\/p\u003E\r\n\r\n\u003Cp\u003E\u8bfe\u7a0b\u4ee3\u7801github\u5730\u5740\uff1a\u003C\/p\u003E\r\n\r\n\u003Cp\u003E\u003Ca href=\u0022https:\/\/github.com\/suneri\/junior_spider\u0022\u003Ehttps:\/\/github.com\/suneri\/junior_spider\u003C\/a\u003E\u003C\/p\u003E\r\n","afterClassCase":"","canLearn":{"status":"yes"},"lessonMaterials":[{"id":"25807","courseId":"1288","lessonId":"29884","title":"Windows\u4e0b\u5b89\u88c5Ubuntu\u865a\u62df\u673a.pdf","description":"","link":"","fileId":"10012","fileUri":"","fileMime":"","fileSize":"3407687","source":"coursematerial","userId":"511","createdTime":"1547461081","copyId":"25557","type":"course"}]}'

s1 = re.findall(r'"mediaUri":"([^"]+)"',s)[0]
print(s1)



# s1 = json.dumps(s)

# s2 = json.loads(s1)
# print(type(s2))

# number = s2['mediaUri']
# print(number)


# mediaUri_nums = playvideo_info['mediaUri']
# print(mediaUri_nums)



