import time
import requests
from bs4 import BeautifulSoup

#
# 2024/8/1 发现requests够用 再改 跟第一个网站的第一部分结构相似 但数量少 可能用不到2个文件夹
# 14：13 60%吧 能跑了 先跑着 后续筛选 边跑边写
# https://magdeleine.co/page/176/ 2-176

# 14:53 page15

for pageNum in range(15,177):
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

        imgResponse = requests.get(imgSrc)

        imgName=imgSrc.split('/')[-1]

        with open('F:/爬虫202407/ZC_爬虫_0726/magdeleine_co/imgGot1/'+imgName,mode='wb') as f:
            f.write(imgResponse.content)
        time.sleep(3)
        print(imgName,':completed,num:',i)

    # i=0 # 记录每页的图片数量
#     for div in divList:
#         i+=1
#         imgSrc=div.find('img').get('data-original')
#
#         imgResponse=requests.get(imgSrc)
#
#         imgName=imgSrc.split('/')[-1]
#
#         with open('../imgGot2/'+imgName,mode='wb') as f:
#             f.write(imgResponse.content)
#             print(imgName,':completed,num:',i)
#             time.sleep(0.5)
#     print('page',pageNum,'completed!')
#     time.sleep(5)
# print('all completed!')