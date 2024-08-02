import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver import ActionChains


# plan b selenium+requests

# div class='center' ->a.href.spilt '/' [-1] ------------图片id 所以paln b 我只需要下拉滚动条
# 14：43 滚动加载无效 可能是被网站识别出来了？ 或者网站需要反应时间？
# 14:53 plan d 手动把图片都加载出来 然后再处理这个html。。。。



# # --创建action对象 处理异步加载问题
#
# browser = webdriver.Chrome()
# action = ActionChains(browser)  # 命名修改


# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(options=option)

driver.get('https://alphacoders.com/resolution/7680x4320')

# 设置窗口大小
# driver.set_window_size(600, 800)
driver.maximize_window() # 全屏


print('下拉滚动条')
js = "window.scrollTo(0,5000);"
driver.execute_script(js)



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