#!/usr/bin/python
# -*-coding=utf-8 -*-
#将小象学院自己账号下的视频下载到本地。

from selenium import webdriver
import time
import re
import requests
import json
import urllib


driver = webdriver.Chrome()
#进入到小象学院登录页面
driver.get('http://www.chinahadoop.cn/login')

#切换到账号密码登录
driver.find_element_by_xpath("//*[@id='content-container']/div/div[1]/b[2]/a").click()
# time.sleep(2)

    #输入账号密码  
    #在sendkey后面输入自己的账号和密码
driver.find_element_by_id('login_username').send_keys('18321316072')
driver.find_element_by_id('login_password').send_keys('renji123')
time.sleep(1)
#点击登录按钮
driver.find_element_by_xpath("//*[@id='login-form']/div[5]/button").click()
#登录成功等待页面加载
time.sleep(5)

#点击我的课程
driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[2]/ul/li[1]/a').click()
# driver.find_element_by_class_name('myCourse').click

#选择爬虫工程师初级课程,点击‘继续学习’按钮
driver.find_element_by_xpath("//*[@id='content-container']/div/div[2]/div/div/ul/li[2]/a[2]").click()

les_url = 'http://www.chinahadoop.cn/course/1288/lesson/'
    #经研究课程的地址的数字值范围是在(29882,34031)之间
for nums in range(29882,29885):
        #这是拼接出课程的url
    lesson_url = les_url + str(nums)
    print(lesson_url)

    driver.get(lesson_url)
    respone_get_playvideo =driver.find_element_by_xpath('/html/body/pre').text
    print(respone_get_playvideo)
        #根据课程的url找出视频的mediaurl
#     respone_get_playvideo=requests.get(lesson_url)
#     print(respone_get_playvideo)
#         #根据请求返回的json串找出media的url对应的后缀数字
#     # playvideo_info = json.loads(respone_get_playvideo.text)
            #使用正则表达式从字符串中找出关键词
    mediaUri_nums = re.findall(r'"mediaUri":"([^"]+)"',respone_get_playvideo)[0]
    print(mediaUri_nums)
#     playvideo_url = 'http://playvideo.qcloud.com/getplayinfo/v2/1253931042/'
#         #拼接出视频下载地址url
#     mediaUri =playvideo_url + str(mediaUri_nums)
#     print(mediaUri)
#     respose = requests.get(mediaUri)
#         #将返回的源码用json格式加载
#     videoInfo = json.loads(respose.text)
#     vide0_url = videoInfo["videoInfo"]["sourceVideo"]["url"]
#     print(vide0_url)
#     video_name = videoInfo['videoInfo']['basicInfo']['name']
#     print(video_name)
#     sourceVideo = requests.get(vide0_url)
#     sourceVideo = sourceVideo.content 
# with open ('d:/download/sourceVideo/'+ video_name +'.mp4','wb+') as f:
#     print('-------开始下载------')
#     f.write(sourceVideo)
#     time.sleep(1)
#     print('-------下载完成------')
    
# driver.quit()