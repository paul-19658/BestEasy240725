import time
import re
import requests
from bs4 import BeautifulSoup


with open('C:/Users/BESTEASY/Desktop/新建文本文档.txt','rb') as f:
    html=f.read()

soup = BeautifulSoup(html, 'html.parser')

# itemList=soup.findAll('div', class_='item')
buttonList=soup.findAll('span', class_='button button-download')

# print(divList)
i=0
for button in buttonList: # 321
    i+=1
    if i < 321:
        continue
    try:
        text = button.get('onclick')
        # print(text)
        id1=text.split("'")[1]
        id2=text.split(',')[1]
        id3=text.split("'")[3]
        # time.sleep(2)
        imgSrc = f'https://initiate.alphacoders.com/download/{id1}/{id2}/{id3}' # 1 picfiles/  2 images7/
        print('执行',imgSrc)
        try:
            imgResponse = requests.get(imgSrc)

            imgName = imgSrc.split('/')[-2] + '.jpg'

            # lock.acquire()
            with open('F:/爬虫202407/ZC_爬虫_0726/alphacoders_com/imgGot2/' + imgName, mode='wb') as f:  # 这里手动换吧
                f.write(imgResponse.content)
            # lock.release()
            print(imgName, ':completed,num:', i)
            time.sleep(0.5)
        except:
            pass
    except:
        pass
