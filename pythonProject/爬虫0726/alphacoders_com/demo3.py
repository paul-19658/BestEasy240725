import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver import ActionChains
import subprocess

# plan b selenium+requests

# div class='center' ->a.href.spilt '/' [-1] ------------图片id 所以paln b 我只需要下拉滚动条
# 14：43 滚动加载无效 可能是被网站识别出来了？ 或者网站需要反应时间？就是被网站识别出来了
# 14:53 plan d 手动把图片都加载出来 然后再处理这个html。。。。
# 8/5 9：54 动态加载的url https://alphacoders.com/resolution/7680x4320?page=8&quickload=1  page就到200 可以一个一个整
# 还是决定一个一个的先跑着，多线程来跑，然后再慢慢看抓包
# 18：00 又发现可以selenium，要等加载，先拉到底然后一个一个click，这样可以，然后开始的时候sleep修改下载路径
# 通过cmd启动

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
option.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')

option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")# 从已打开的启动

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(options=option)

driver.get('https://alphacoders.com/resolution/7680x4320')

# 设置窗口大小
# driver.set_window_size(600, 800)
# driver.maximize_window() # 全屏


print('下拉滚动条')
js = "window.scrollTo(0,5000);"
driver.execute_script(js)
time.sleep(10) # 果然 根本就不是什么异步加载拿不到，因为网页加载需要时间，以前都没等，所以只能得到第一页的数据，那要是
buttonList=driver.find_elements(by= By.CLASS_NAME,value='button.button-download')
print(len(buttonList))


# print('源码已保存')
# with open('F:/爬虫202407/ZC_爬虫_0726/alphacoders_com/1.html',mode='w') as f:
#     f.write(html)



# btnDownload=driver.find_element(by= By.XPATH, value="//*[@class='button button-download']")
# btnDownload.click()
# print('点击下载')
# time.sleep(10)
# print('再 手动 关闭一个弹出广告')
# time.sleep(5)

# btnDownloadList=driver.find_elements(by= By.XPATH, value="//*[@class='button button-download']")
# # print(btnDownloadList)
# for btn in btnDownloadList:
#     btn.click()



# a1=driver.find_element(by= By.XPATH,value="/html/body/div/div/div/main/div/div/div/div/div[1]/figure/a")
# # print(a1.get_property('href'))
# path2=a1.get_property('href')
#
# driver.get(path2)
#
# a2=driver.find_element(by= By.XPATH,value="/html/body/div/div/div/main/div/div/div/div/div/a")
# # print(a2.get_property('href'))
# imgSrc =a2.get_property('href')
#
# imgResponse = requests.get(imgSrc)
#
# imgName = imgSrc.split('/')[-1]
#
# with open('F:/爬虫202407/ZC_爬虫_0726/magdeleine_co/imgGot1/' + imgName, mode='wb') as f:
#     f.write(imgResponse.content)
#
# print(imgName, ':completed')