import threading
import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
# 8/5 10：55 搞到动态加载的请求了，直接是返回html格式，所以先跑着
# 11:22 requests会被ban 应该还是浏览器指纹的问题，还是selenium跑
# 多线程需要对应数量的浏览器多开。。
# 好像多开不了
# 13：35 好像是Chrome多开不了，threading不行，我直接运行在不同的py文件里也不行，那一个窗口慢慢跑得了
# 8/5 17:36 该执行page176
# https://alphacoders.com/resolution/7680x4320?page=8&quickload=1  page就到200
# html/body/div/div/div[n]/div/div[2]/div/div/div/span class='button button-download'
def runChrome(port):
    # 似乎独占一个线程，不结束的话，线性的话，后面没法运行
    cmd = r'"C:\Users\BESTEASY\AppData\Local\Google\Chrome\Application\chrome.exe" ' \
          f'--remote-debugging-port={port} '
    subprocess.run(cmd)
    print('run on port:',port)

def runPage(pageStart,pageEnd,port):
    for pageNum in range(pageStart,pageEnd):
        url = f'https://alphacoders.com/resolution/7680x4320?page={pageNum}&quickload=1'

        # 不自动关闭浏览器
        option = webdriver.ChromeOptions()
        # option.add_experimental_option("detach", True)
        option.add_argument(
            'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')

        option.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")  # 从已打开的启动

        # 将option作为参数添加到Chrome中
        driver = webdriver.Chrome(options=option)

        driver.get(url)

        buttonList=driver.find_elements(by= By.CLASS_NAME,value='button.button-download')
        # print(len(buttonList))
        print('\n\n执行page{}\n\n'.format(pageNum))
        i=0
        for button in buttonList:
            i+=1
            try:
                text=button.get_attribute('onclick')
                # print(text)
                id1=text.split("'")[1]
                id2=text.split(',')[1]
                id3=text.split("'")[3]

                # time.sleep(2)
                imgSrc = f'https://initiate.alphacoders.com/download/{id1}/{id2}/{id3}' # 1 picfiles/  2 images7/

                try:
                    imgResponse = requests.get(imgSrc)

                    imgName = imgSrc.split('/')[-2] + '.jpg'

                    lock.acquire()
                    with open('F:/爬虫202407/ZC_爬虫_0726/alphacoders_com/imgGot0806/' + imgName, mode='wb') as f:  # 这里手动换吧
                        f.write(imgResponse.content)
                    lock.release()
                    print(imgName, ':completed,num:', i)
                    time.sleep(0.3)
                except:
                    pass
            except:
                pass

if __name__ == '__main__':
    lock = threading.Lock()
    port1=9222
    port2=9223
    port3=9224
    port4=9225

    # threadChrome1=threading.Thread(target=runChrome(port1))
    # threadChrome2=threading.Thread(target=runChrome(port2))
    # threadChrome3=threading.Thread(target=runChrome(port3))
    # threadChrome4=threading.Thread(target=runChrome(port4))

    thread1=threading.Thread(target=runPage,args=(156,201,port1))
    # thread2=threading.Thread(target=runPage,args=(50,100,port2))
    # thread3=threading.Thread(target=runPage,args=(100,150,port3))
    # thread4=threading.Thread(target=runPage,args=(150,201,port4))

    # threadChrome1.start()
    # threadChrome2.start()
    # threadChrome3.start()
    # threadChrome4.start()

    thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
