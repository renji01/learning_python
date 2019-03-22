#!/usr/bin/python
# -*-coding=utf-8 -*-
#将小象学院自己账号下的视频下载到本地。

from selenium import webdriver
import time
driver = webdriver.Chrome()
#进入到小象学院登录页面
driver.get('http://www.chinahadoop.cn/login')

#切换到账号密码登录
driver.find_element_by_xpath("//*[@id='content-container']/div/div[1]/b[2]/a").click()
# time.sleep(2)

    #输入账号密码  
    #在sendkey后面输入自己的账号和密码
driver.find_element_by_id('login_username').send_keys('login_username')
driver.find_element_by_id('login_password').send_keys('login_password')
time.sleep(1)
#点击登录按钮
driver.find_element_by_xpath("//*[@id='login-form']/div[5]/button").click()
#登录成功等待页面加载
time.sleep(5)

#点击我的课程
driver.find_element_by_class_name('myCourse').click

#选择爬虫工程师初级课程,点击继续学习
driver.find_element_by_xpath("//*[@id='content-container']/div/div[2]/div/div/ul/li[2]/a[2]").click

#获取视频下载列表



driver.quit()