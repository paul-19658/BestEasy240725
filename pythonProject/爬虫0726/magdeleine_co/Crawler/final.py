import os
import time
import threading
import requests
from bs4 import BeautifulSoup

#
# 2024/8/1 发现requests够用 再改 跟第一个网站的第一部分结构相似 但数量少 可能用不到2个文件夹
# 14：13 60%吧 能跑了 先跑着 后续筛选 边跑边写
# 15:01 95% 文件夹的话也就用两个没必要加这个功能了 凑合用吧
# https://magdeleine.co/page/176/ 2-176


def filtrate(soup): # 网页中筛选分辨率
    tagPix=soup.find('div',class_='resolution').find('a') # 6000x4000 Px (X-Large)
    str=tagPix.text
    str1=str[0:4]
    str2=str[5:10]
    # print(str1,'x',str2)
    if int(str1)<4000 or int(str2)<4000:
        return False
    else:
        return True

def crawl(startPAGE, endPAGE):
    for pageNum in range(startPAGE, endPAGE):
        pageUrl1 = f'https://magdeleine.co/page/{pageNum}'
        pageResp1 = requests.get(pageUrl1)
        print('下面执行：', pageUrl1)

        html1 = pageResp1.text

        soup1 = BeautifulSoup(html1, 'html.parser')

        aList = soup1.findAll('a', class_='photo-link')
        i = 0  # 记录每页的图片数量
        for a in aList:
            i+=1
            pageUrl2=a.get('href')
            # print(pageUrl2)
            pageResp2 = requests.get(pageUrl2)

            html2=pageResp2.text

            soup2=BeautifulSoup(html2,'html.parser')

            imgSrc=soup2.find('div',class_='download').find('a').get('href')
            # print(imgSrc)
            imgName = imgSrc.split('/')[-1]

            # 先筛选
            if not filtrate(soup2):
                print('不达标！:{},num:{}'.format(imgName,i))
                continue
            imgResponse = requests.get(imgSrc)

            lock.acquire()
            with open('F:/爬虫202407/ZC_爬虫_0726/magdeleine_co/imgGotA/'+imgName,mode='wb') as f:
                f.write(imgResponse.content)
            lock.release()
            time.sleep(3)
            print(imgName,':completed,num:',i)

        print('\n\npage', pageNum, 'completed!\n\n')

    print('page{} to page{} completed!'.format(startPAGE,endPAGE))

if __name__ == '__main__':
    lock = threading.Lock()
    # 100-135
    thread1=threading.Thread(target=crawl,args=(126,135))
    # 135-176
    thread2=threading.Thread(target=crawl,args=(162,177))

    thread1.start()
    thread2.start()