import time
import requests
from bs4 import BeautifulSoup


with open('C:/Users/BESTEASY/Desktop/新建文本文档.txt','rb') as f:
    html=f.read()

soup = BeautifulSoup(html, 'html.parser')

itemList=soup.findAll('div', class_='item')

# print(divList)
i=0
for div in itemList:
    print(len(itemList))
    i+=1
    try:
        src = div.find('div').find('div').find('a').get('href')
        # print(src)
        id=src.split('/')[-1]
        # print(id)
        imgSrc = f'https://initiate.alphacoders.com/download/picfiles/{id}/jpg'
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
