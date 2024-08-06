from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
"""测试headless模式和options设置插件"""


# 创建Chrome选项对象
options = webdriver.ChromeOptions()

options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")


options.add_experimental_option("detach", True)
# 添加插件
plugin_path = r'C:\Users\BESTEASY\AppData\Local\Google\Chrome\User Data\Default\Extensions\meojnmfhjkahlfcecpdcdgjclcilmaij\1.0.5_0.crx'
options.add_extension(plugin_path)
options.add_argument('--headless')
# 启动浏览器并访问一个网页
# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(options=options)

driver.get('https://alphacoders.com/resolution/6000x4000')

js = 'document.documentElement.scrollTop=3000'
js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'

# js = "window.scrollTo(0,5000);"
driver.execute_script(js_all)
time.sleep(15)



# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button.button-download')))

buttonList=driver.find_elements(by= By.CLASS_NAME,value='button.button-download')
print(len(buttonList))