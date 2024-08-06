import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver import ActionChains
import subprocess
""" 
8/6 这是一次次把页面最终拉到底以后一个一个click
"""

# plan b selenium+requests

# div class='center' ->a.href.spilt '/' [-1] ------------图片id 所以paln b 我只需要下拉滚动条
# 14：43 滚动加载无效 可能是被网站识别出来了？ 或者网站需要反应时间？就是被网站识别出来了
# 14:53 plan d 手动把图片都加载出来 然后再处理这个html。。。。
# 8/5 9：54 动态加载的url https://alphacoders.com/resolution/7680x4320?page=8&quickload=1  page就到200 可以一个一个整
# 还是决定一个一个的先跑着，多线程来跑，然后再慢慢看抓包
# 18：00 又发现可以selenium，要等加载，先拉到底然后一个一个click，这样可以，然后开始的时候sleep修改下载路径
# 8/6 尝试这个思路 可行 上次手动进度是100页 101x15=1515

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
option.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')

option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")# 从已打开的启动

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(options=option)

driver.get('https://alphacoders.com/resolution/6000x4000')
for t in range(0,50):
    print('修改下载路径和进行人机验证,{}'.format(50-t))
    time.sleep(1)
# 设置窗口大小
# driver.set_window_size(600, 800)
# driver.maximize_window() # 全屏
for i in range(0,350):
    # document.documentElement.scrollTop   指定滚动条的位置
    # document.documentElement.scrollHeight 获取当前页面的最大高度
    js = 'document.documentElement.scrollTop=3000'
    js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    print('下拉滚动条,第{}次'.format(i))
    # js = "window.scrollTo(0,5000);"
    driver.execute_script(js_all)
    time.sleep(5) # 果然 根本就不是什么异步加载拿不到，因为网页加载需要时间，以前都没等，所以只能得到第一页的数据，那要是

print('页面到底了')
buttonList=driver.find_elements(by= By.CLASS_NAME,value='button.button-download')
count=0 # 控制到上次的进度
for button in buttonList:
    if count<=1515:
        print(count)
        count+=1
        continue

    button.click()
    print('进行：',count)
    time.sleep(0.3)


