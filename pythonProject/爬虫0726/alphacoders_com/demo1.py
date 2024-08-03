import time

# https://alphacoders.com/resolution/7680x4320
# https://alphacoders.com/resolution/6000x4000
# 差不多10000张，不需筛选
# https://initiate.alphacoders.com/download/picfiles/514851/jpg
# 可以苦苦全爬然后筛，也可以精准爬但selenium click抓包+滚轮滚动条加载
# 滚动条实现滚动还要调用js 参照标签移动 问题不大
# 8/2 打开网页的第一次click会弹广告，还不是每个第一次都弹广告，
# click不成功的原因是一个广告栏遮挡

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# alphacoders.com/resolution/6000x4000

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(options=option)

driver.get('https://alphacoders.com/resolution/6000x4000')

btnCloseDispaly=driver.find_element(by= By.XPATH,value="//*[@id='closeDisplay']") # 先关闭一个display
btnCloseDispaly.click()
print('先关闭一个display')
time.sleep(1)

btnDownload=driver.find_element(by= By.XPATH, value="//*[@class='button button-download']")
btnDownload.click()
print('点击下载')
time.sleep(1)
while True:
    try:
        btnCloseAd=driver.find_element(by= By.CLASS_NAME, value="ns-g0kc3-e-19 button-common close-button milo-animation delay-4") # 再关闭一个弹出的广告
        btnCloseAd.click()
    except:
        pass
print('再关闭一个弹出广告')

driver.switch_to.alert.dismiss()
print(111)
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