import time
import requests
from bs4 import BeautifulSoup

# 网站的前两部分 结构一致 ‘创意图片’ 和 ‘矢量图’
# div class='itemWra'->a href √
# 共200页，每页跑完暂停5s，第一行range随时换页码 每页50 可根据目录里文件数量判断页数


#  0-0-0-0-0-0-0-0-0-0-0-0-0-{pageNum}.html
for pageNum in range(36,201):
    url = f'https://www.52112.com/list/116054-0-0-0-0-0-0-0-0-0-0-0-0-{pageNum}.html'
    response = requests.get(url)
    print('下面执行：',url)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    # img_src=soup.find('div', class_='itemWra').find('img').get('data-original')
    divList = soup.findAll('div', class_='itemWra')
    i=0 # 记录每页的图片数量
    for div in divList:
        i+=1
        imgSrc=div.find('img').get('data-original')

        imgResponse=requests.get(imgSrc)

        imgName=imgSrc.split('/')[-1]

        with open('../imgGot2/'+imgName,mode='wb') as f:
            f.write(imgResponse.content)
            print(imgName,':completed,num:',i)
            time.sleep(0.5)
    print('page',pageNum,'completed!')
    time.sleep(5)
print('all completed!')





    # img_response = requests.get(img_src)
    #
    # img_name = img_src.split('/')[-1]
    #
    # with open('imgGot/' + img_name, mode='wb') as f:
    #     f.write(img_response.content)
    #
    # print('okkkkkkkkkkkkkkkkkkkkkkkk')
    #



