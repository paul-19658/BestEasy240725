import time

# https://alphacoders.com/resolution/7680x4320
# https://alphacoders.com/resolution/6000x4000
# 差不多10000张，不需筛选
# https://initiate.alphacoders.com/download/picfiles/514851/jpg
# 可以苦苦全爬然后筛，也可以精准爬但selenium click抓包+滚轮滚动条加载
# 滚动条实现滚动还要调用js 参照标签移动 问题不大
# 8/2 打开网页的第一次click会弹广告，还不是每个第一次都弹广告，
# click不成功的原因是一个广告栏遮挡

# div class='center' ->a.href.spilt '/' [-1] ------------图片id 所以paln b 我只需要下拉滚动条

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# alphacoders.com/resolution/6000x4000

from selenium.webdriver import ActionChains

# # --创建action对象 处理异步加载问题
#
# browser = webdriver.Chrome()
# action = ActionChains(browser)  # 命名修改


# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(options=option)

driver.get('https://alphacoders.com/resolution/6000x4000')
print('先手动关闭所有的广告哈')
time.sleep(10)
# btnCloseDispaly=driver.find_element(by= By.XPATH,value="//*[@id='closeDisplay']") # 先关闭一个display
# btnCloseDispaly.click()
# print('先关闭一个display')
# time.sleep(1)

btnDownload=driver.find_element(by= By.XPATH, value="//*[@class='button button-download']")
btnDownload.click()
print('点击下载')
time.sleep(10)
print('再 手动 关闭一个弹出广告')
time.sleep(5)

btnDownloadList=driver.find_elements(by= By.XPATH, value="//*[@class='button button-download']")
# print(btnDownloadList)
for btn in btnDownloadList:
    btn.click()



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