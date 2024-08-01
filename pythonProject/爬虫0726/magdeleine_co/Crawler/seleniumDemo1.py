from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# 2024/8/1 11:42 magdeleine.co 30%
# 还 跳到page2 page2的分辨率检测



# /html/body/div/div/div/main/div/div/div/div/div[1]/figure/a

# 不自动关闭浏览器
# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome()

driver.get('https://magdeleine.co/')

a1=driver.find_element(by= By.XPATH,value="/html/body/div/div/div/main/div/div/div/div/div[1]/figure/a")
# print(a1.get_property('href'))
path2=a1.get_property('href')

driver.get(path2)

a2=driver.find_element(by= By.XPATH,value="/html/body/div/div/div/main/div/div/div/div/div/a")
# print(a2.get_property('href'))
imgSrc =a2.get_property('href')

imgResponse = requests.get(imgSrc)

imgName = imgSrc.split('/')[-1]

with open('F:/爬虫202407/ZC_爬虫_0726/magdeleine_co/imgGot1/' + imgName, mode='wb') as f:
    f.write(imgResponse.content)

print(imgName, ':completed')