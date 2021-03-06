#coding=utf-8
u''' 
#文件名：_initDriver
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-09-14
#模块描述：selenium的webdriver初始化（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time
from selenium import webdriver
from _fileRead import fileRead

class initDriver:
    u'''web驱动初始化'''
    def open_driver(self):
        #读取test.conf文件内容
        fileList = fileRead().get_ip_address()
        #设定IP地址
        ipAdd = fileList[0].strip('\n')

        if "0" in fileList[1].strip('\n'):
            u'''打开IE驱动'''
            #指定ie的webdriver的路径
#            ieDriver = fileList[1].strip('\n')
            # os.environ["webdriver.ie.driver"] = ieDriver
            # driver = webdriver.Ie(ieDriver)
            driver=webdriver.Ie()
            
        elif "1" in fileList[1].strip('\n'):
            u'''打开google驱动'''
            driver = webdriver.Chrome()
#            driver = webdriver.Chrome(fileList[3].strip('\n'))
            
        else:
            driver = webdriver.Firefox()
#            profileDir = "C:\Users\yy\AppData\Roaming\Mozilla\Firefox\Profiles\k70dxttd.default"
#            isProfile = webdriver.FirefoxProfile(profileDir)
#            time.sleep(5)
#            u'''打开火狐驱动'''
#            driver = webdriver.Firefox(isProfile)
            
            
            
        #IE窗口最大化
        driver.maximize_window()

        #打开IP地址对应的网页
        driver.get("https://" + ipAdd + "/fort")
#        time.sleep(5)
        #https访问时弹出安全警告页面后点击继续，0代表有安全警告，1代表没有安全警告
        if "0"  in fileList[2].strip('\n'):
            driver.get("javascript:document.getElementById('overridelink').click();")
        return driver
        
    def close_driver(self,driver):        
        u'''关闭驱动以及所有被关联的windows进程'''
        driver.close()
        driver.quit()

#yu=initDriver().open_driver()
#initDriver().close_driver(yu)
